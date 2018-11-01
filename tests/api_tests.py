import sys
import unittest
import uuid

import requests
import validators

sys.path.append('../')

from settings import PORT_NUMBER

req_asset_url = 'http://localhost:{}/asset'
asset_url = 'http://localhost:{}/asset/{}'


class ApiTestCases(unittest.TestCase):
    def test_request_upload_url_and_asset_id(self):
        res = requests.post(req_asset_url.format(PORT_NUMBER))
        assert res.status_code == 200
        data = res.json()
        assert validators.uuid(data['id'])
        assert validators.url(data['upload_url'])
        r = requests.put(data['upload_url'], data=open('tmp.txt', 'rb'))
        assert r.status_code == 200

    def test_mark_upload_complete_for_random_asset_id(self):
        uid = str(uuid.uuid4())
        res = requests.put(asset_url.format(PORT_NUMBER, uid), data={'status': 'uploaded'})
        assert res.status_code == 400
        assert res.text == 'asset {} does not exist'.format(uid)

    def test_mark_upload_complete_for_available_asset_id(self):
        res = requests.post(req_asset_url.format(PORT_NUMBER))
        assert res.status_code == 200
        data = res.json()
        res1 = requests.put(asset_url.format(PORT_NUMBER, data['id']), data={'status': 'uploaded'})
        assert res1.status_code == 200
        assert res1.text == 'asset {} marked as upload complete'.format(data['id'])

    def test_get_asset_download_url_for_random_asset_id(self):
        uid = str(uuid.uuid4())
        res = requests.get(asset_url.format(PORT_NUMBER, uid))
        assert res.status_code == 400
        assert res.text == 'asset {} does not exist'.format(uid)

    def test_get_asset_download_url_for_unmarked_asset_id(self):
        res = requests.post(req_asset_url.format(PORT_NUMBER))
        assert res.status_code == 200
        data = res.json()
        res1 = requests.get(asset_url.format(PORT_NUMBER, data['id']))
        assert res1.status_code == 422
        assert res1.text == 'Please mark completion of upload before requesting download link'

    def test_get_asset_download_url_for_available_asset_id(self):
        res = requests.post(req_asset_url.format(PORT_NUMBER))
        assert res.status_code == 200
        data = res.json()
        res1 = requests.put(data['upload_url'], data=open('tmp.txt', 'rb'))
        assert res1.status_code == 200
        res2 = requests.put(asset_url.format(PORT_NUMBER, data['id']), data={'status': 'uploaded'})
        assert res2.status_code == 200
        res3 = requests.get(asset_url.format(PORT_NUMBER, data['id']))
        assert res3.status_code == 200
        res4 = requests.get(res3.json()['download_url'])
        assert res4.status_code == 200
        assert res4.text == 'test data'


def main():
    unittest.main()


if __name__ == "__main__":
    main()
