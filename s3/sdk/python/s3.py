import boto3
import string
from random import randint, choice
import os

def create_file(path):
    """
    Creates an empty file at the specified path. If the file already exists,
    it updates the file's timestamp without modifying its content.

    Parameters:
    path (str): The path where the file will be created or the timestamp will be updated.
    """
    with open(path, 'a'):
        os.utime(path, None)

def write_file(filename):
    """
    Writes a random string composed of 7 digits and 19 alphabetic characters to the specified file.

    Parameters:
    filename (str): The name of the file where the random string will be written.
    """
    digits = "".join([choice(string.digits) for _ in range(7)])
    chars = "".join([choice(string.ascii_letters) for _ in range(19)])
    string_r = digits + chars
    with open(filename, 'a') as f:
        f.write(string_r)

def create_s3_bucket(client, bucket_name):
    """
    Creates an S3 bucket with the specified name using the provided Boto3 S3 client.

    Parameters:
    client (boto3.client): The Boto3 S3 client used to interact with the S3 service.
    bucket_name (str): The name of the S3 bucket to be created.

    Returns:
    str or None: The name of the created S3 bucket if successful, otherwise None.
    """
    try:
        client.create_bucket(Bucket=bucket_name)
        print(f"S3 bucket '{bucket_name}' created successfully in region '{region}'.")
        return bucket_name
    except Exception as e:
        print(f"An error occurred while creating the S3 bucket: {e}")
        return None

def put_s3_object(client, bucket_name):
    """
    Creates a random number of files (between 1 and 10), writes random strings to them,
    and uploads them to the specified S3 bucket.

    Parameters:
    client (boto3.client): The Boto3 S3 client used to interact with the S3 service.
    bucket_name (str): The name of the S3 bucket where the files will be uploaded.
    """
    number_of_files = randint(1, 11)
    for i in range(number_of_files):
        filename = f'file_{i}.txt'
        output_path = f'/tmp/{filename}'
        create_file(output_path)
        write_file(output_path)
        client.upload_file(output_path, bucket_name, filename)

# Main execution
region = 'us-east-1'
client = boto3.client('s3', region_name=region)
bucket_name = input("Enter your bucket name: ")
create_s3_bucket(client, bucket_name)
put_s3_object(client, bucket_name)