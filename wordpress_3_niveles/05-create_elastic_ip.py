import boto3
import os
from dotenv import load_dotenv

load_dotenv()

INSTANCE_NAME_FRONTEND = os.getenv('INSTANCE_NAME_FRONTEND')

ec2 = boto3.client('ec2')

# Describe instances to get the instance ID
response = ec2.describe_instances(
    Filters=[
        {'Name': 'tag:Name', 'Values': [INSTANCE_NAME_FRONTEND]},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]
)

instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']

# Allocate Elastic IP
allocation = ec2.allocate_address(Domain='vpc')
elastic_ip = allocation['PublicIp']

# Associate Elastic IP with the instance
ec2.associate_address(InstanceId=instance_id, PublicIp=elastic_ip)

print(f'Elastic IP {elastic_ip} associated with instance {instance_id}')