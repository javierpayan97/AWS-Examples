
import boto3
from s3_encryption.client import S3EncryptionClient

REGION = 'us-east-1'
BUCKET = 'encryption-client-s3-fun-jp-314324235'
key = 'hello.txt'

s3e = S3EncryptionClient(encryption_key=key, region_name=REGION)
s3e.put_object(Body='this is a test', Bucket=BUCKET, Key=key)
s3e.client.put_object(Body='handshake', Bucket=BUCKET, Key=key + '.key')