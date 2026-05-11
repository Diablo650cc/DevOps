#!/usr/bin/env python3
import boto3
from datetime import datetime

ec2 = boto3.client('ec2', region_name='us-east-1')

response = ec2.describe_instances()
with open('reporte_recursos.txt', 'w') as f:
    f.write(f"Reporte EC2 - {datetime.now()}\n")
    for r in response['Reservations']:
        for i in r['Instances']:
            f.write(f"ID: {i['InstanceId']}, Estado: {i['State']['Name']}, Tipo: {i['InstanceType']}\n")

print("Reporte generado: reporte_recursos.txt")