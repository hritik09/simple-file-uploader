import sys
import unittest
import uuid

import requests
import validators

sys.path.append('../')

from utils.s3_uploader import get_url_and_id_for_upload, get_download_link


class UtilTestCases(unittest.TestCase):
    def test_return_types__get_url_and_id_for_upload(self):
        url, uid = get_url_and_id_for_upload()
        assert validators.uuid(uid)
        assert validators.url(url)

    def test_uploadable__get_url_and_id_for_upload(self):
        url, uid = get_url_and_id_for_upload()
        r = requests.put(url, data=open('tmp.txt', 'rb'))
        assert r.status_code == 200

    def test_return_types__get_download_link(self):
        uid = str(uuid.uuid4())
        url = get_download_link(uid, expiry=10)
        assert validators.url(url)

    def test_downloadable__get_download_link(self):
        upload_url, uid = get_url_and_id_for_upload()
        r = requests.put(upload_url, data=open('tmp.txt', 'rb'))
        assert r.status_code == 200
        download_url = get_download_link(uid, expiry=10)
        res = requests.get(download_url)
        assert res.status_code == 200
        assert res.text == 'test data'


def main():
    unittest.main()


if __name__ == "__main__":
    main()
