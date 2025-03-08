import boto3
import os
from dotenv import load_dotenv

load_dotenv()

AMI_ID = os.getenv('AMI_ID')
COUNT = int(os.getenv('COUNT'))
INSTANCE_TYPE = os.getenv('INSTANCE_TYPE')
KEY_NAME = os.getenv('KEY_NAME')
SECURITY_GROUP_FRONTEND = os.getenv('SECURITY_GROUP_FRONTEND')
SECURITY_GROUP_BACKEND = os.getenv('SECURITY_GROUP_BACKEND')
SECURITY_GROUP_NFS = os.getenv('SECURITY_GROUP_NFS')
SECURITY_GROUP_BALANCEADOR = os.getenv('SECURITY_GROUP_BALANCEADOR')
INSTANCE_NAME_FRONTEND = os.getenv('INSTANCE_NAME_FRONTEND')
INSTANCE_NAME_BACKEND = os.getenv('INSTANCE_NAME_BACKEND')
INSTANCE_NAME_NFS = os.getenv('INSTANCE_NAME_NFS')
INSTANCE_NAME_BALANCEADOR = os.getenv('INSTANCE_NAME_BALANCEADOR')

ec2 = boto3.client('ec2')

def run_instance(image_id, count, instance_type, key_name, security_group, instance_name):
    ec2.run_instances(
        ImageId=image_id,
        MinCount=count,
        MaxCount=count,
        InstanceType=instance_type,
        KeyName=key_name,
        SecurityGroups=[security_group],
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {'Key': 'Name', 'Value': instance_name}
                ]
            }
        ]
    )

# Frontend 1
run_instance(AMI_ID, COUNT, INSTANCE_TYPE, KEY_NAME, SECURITY_GROUP_FRONTEND, INSTANCE_NAME_FRONTEND)
print(f"Instancia EC2 '{INSTANCE_NAME_FRONTEND}' creada")
# Frontend 2
run_instance(AMI_ID, COUNT, INSTANCE_TYPE, KEY_NAME, SECURITY_GROUP_FRONTEND, INSTANCE_NAME_FRONTEND)
print
# Backend
run_instance(AMI_ID, COUNT, INSTANCE_TYPE, KEY_NAME, SECURITY_GROUP_BACKEND, INSTANCE_NAME_BACKEND)
print(f"Instancia EC2 '{INSTANCE_NAME_BACKEND}' creada")
# NFS
run_instance(AMI_ID, COUNT, INSTANCE_TYPE, KEY_NAME, SECURITY_GROUP_NFS, INSTANCE_NAME_NFS)
print(f"Instancia EC2 '{INSTANCE_NAME_NFS}' creada")
# Balanceador
run_instance(AMI_ID, COUNT, INSTANCE_TYPE, KEY_NAME, SECURITY_GROUP_BALANCEADOR, INSTANCE_NAME_BALANCEADOR)
print(f"Instancia EC2 '{INSTANCE_NAME_BALANCEADOR}' creada")
print("Todas las instancias han sido creadas")