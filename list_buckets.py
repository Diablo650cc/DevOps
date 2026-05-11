#!/usr/bin/env python3
import boto3

s3 = boto3.client('s3')
buckets = s3.list_buckets()

print("Buckets S3:")
for bucket in buckets['Buckets']:
    print(f" - {bucket['Name']} ({bucket['CreationDate']})")