#!/usr/bin/env python3
import boto3
from datetime import datetime

BUCKET_NAME = "devops-storage-07097795"
LOCAL_FILE = "reporte_recursos.txt"
S3_KEY = f"reportes/reporte_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

s3 = boto3.client('s3')
s3.upload_file(LOCAL_FILE, BUCKET_NAME, S3_KEY)
print(f"Subido a s3://{BUCKET_NAME}/{S3_KEY}")