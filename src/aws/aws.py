import boto3
from utils.config import Config

def upload_to_s3(temp_path,object_name):
    session = boto3.Session()
    s3_client = session.client('s3')

    with open(temp_path,'rb') as body:
        s3_client.put_object(
            Body = body,
            Bucket = Config.config['BUCKET'],
            Key = object_name
        )