from flask import Flask, Response, request, jsonify
from gevent import monkey
from gevent.pywsgi import WSGIServer

monkey.patch_all()

from settings import PORT_NUMBER, APP_NAME
from utils.logging_helper import get_logger
from utils.s3_uploader import get_url_and_id_for_upload, get_download_link

app = Flask(APP_NAME)
app.debug = True
logger = get_logger(__name__)
asset_map = {}


@app.route('/asset/<asset_id>', methods=["GET"])
def get_asset_download_url(asset_id):
    if asset_id not in asset_map:
        return Response(response='asset {} does not exist'.format(asset_id), status=400)

    if asset_map[asset_id]:
        timeout = request.args.get('timeout', 3600)
        try:
            download_url = get_download_link(asset_id, expiry=timeout)
        except Exception:
            logger.exception('Failed to fetch download url for asset {}'.format(asset_id))
            return Response(response='Something bad happened, please retry in a while', status=500)

        return jsonify({'download_url': download_url})
    else:
        return Response(response='Please mark completion of upload before requesting download link', status=422)


@app.route('/asset/<asset_id>', methods=["PUT"])
def update_upload_status(asset_id):
    if asset_id not in asset_map:
        return Response(response='asset {} does not exist'.format(asset_id), status=400)

    if 'status' not in request.form:
        return Response(response='must pass status in body', status=400)
    else:
        status = request.form['status']
        if status != 'uploaded':
            return Response(response='This url is only to mark upload completion of asset. status should be "uploaded"',
                            status=422)
        else:
            try:
                asset_map[asset_id] = True
                return Response(response='asset {} marked as upload complete'.format(asset_id))
            except KeyError:
                return Response(response='asset {} does not exist'.format(asset_id), status=400)


@app.route('/asset', methods=["POST"])
def request_new_upload_url():
    try:
        upload_url, asset_id = get_url_and_id_for_upload()
    except Exception:
        logger.exception('Failed to get upload url and asset id')
        return Response(response='Something bad happened, please retry in a while', status=500)
    asset_map[asset_id] = False
    return jsonify({'upload_url': upload_url, 'id': asset_id})


def main():
    "Start gevent WSGI server"
    # using gevent WSGI server instead of the Flask for async handling of requests with greenlets
    try:
        logger.debug('starting server on port {}'.format(PORT_NUMBER))
        http = WSGIServer(('', PORT_NUMBER), app.wsgi_app)
        http.serve_forever()
    except KeyboardInterrupt:
        logger.error('^C received, shutting down the web server')
        http.stop()


if __name__ == '__main__':
    main()