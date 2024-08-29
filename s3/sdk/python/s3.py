import boto3
from random import randint
import os

def touch(path):
    with open(path, 'a'):
        os.utime(path, None)

def create_s3_bucket(client,bucket_name):
    try:
        client.create_bucket(Bucket=bucket_name)
        print(f"S3 bucket '{bucket_name}' created successfully in region '{region}'.")
        return bucket_name
    except Exception as e:
        print(f"An error occurred while creating the S3 bucket: {e}")
        return None

def put_s3_object(client,bucket_name):
    number_of_files = int(1+randint(0,10))
    for i in range(number_of_files):
        filename = f"file_{i}.txt"
        output_path = f"/tmp/{filename}"
        touch(output_path)
        response = client.put_object(Key=output_path,Bucket=bucket_name)

region="us-east-1"
client = boto3.client('s3',region_name=region)    
bucket_name = input("your bucket name: ")
create_s3_bucket(client,bucket_name)
put_s3_object(client,bucket_name)