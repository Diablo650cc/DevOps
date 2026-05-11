#!/usr/bin/env python3
import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

instances = ec2.run_instances(
    ImageId='ami-0c02fb55956c7d316',
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    IamInstanceProfile={'Name': 'LabInstanceProfile'},
    TagSpecifications=[{
        'ResourceType': 'instance',
        'Tags': [{'Key': 'Name', 'Value': 'DevOps-Auto'}]
    }]
)

print(f"Instancia lanzada: {instances['Instances'][0]['InstanceId']}")