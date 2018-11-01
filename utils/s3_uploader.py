import uuid

import boto3
from settings import BUCKET_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


def get_url_and_id_for_upload():
    asset_id = str(uuid.uuid4())
    presigned_url = s3.generate_presigned_url('put_object', Params={"Bucket": BUCKET_NAME, "Key": asset_id},
                                              HttpMethod='PUT')
    return presigned_url, asset_id


def get_download_link(asset_id, expiry=3600):
    return s3.generate_presigned_url(ClientMethod='get_object', ExpiresIn=expiry,
                                     Params={"Bucket": BUCKET_NAME, "Key": asset_id})
