import boto3
import os
from dotenv import load_dotenv

load_dotenv()

from botocore.exceptions import NoCredentialsError

def upload_to_s3(file_name, bucket, object_name=None):
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
    )

    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        s3.upload_file(file_name, bucket, object_name)
        print(f"✅ Successfully uploaded '{file_name}' to S3 bucket '{bucket}' as '{object_name}'")
    except FileNotFoundError:
        print("❌ The file was not found.")
    except NoCredentialsError:
        print("❌ AWS credentials not available.")

if __name__ == "__main__":
    file_path = input("📁 Enter the path of the file to upload: ")
    bucket_name = input("☁️  Enter your S3 bucket name: ")
    upload_to_s3(file_path, bucket_name)
