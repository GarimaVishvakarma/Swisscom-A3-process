import boto3
import os

s3 = boto3.client("s3")

files = os.listdir(r"files")
for file in files:
    s3.upload_file(
        Filename=r"C:\Users\Z004CW1W\Desktop\SwisscomAssignment\Assignment3\Solution\files\{}".format(file),
        Bucket="swisscom-assignment-bucket",
        Key=file
    )

