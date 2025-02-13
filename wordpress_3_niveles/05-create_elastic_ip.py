import boto3
import os
from dotenv import load_dotenv

load_dotenv()

INSTANCE_NAME_FRONTEND = os.getenv('INSTANCE_NAME_FRONTEND')

ec2 = boto3.client('ec2')

# Describe las instancias para obtener la ID de la instancia
response = ec2.describe_instances(
    Filters=[
        {'Name': 'tag:Name', 'Values': [INSTANCE_NAME_FRONTEND]},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]
)

instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']

# Asigna una nueva dirección IP elástica
allocation = ec2.allocate_address(Domain='vpc')
elastic_ip = allocation['PublicIp']

# Asocia la dirección IP elástica con la instancia
ec2.associate_address(InstanceId=instance_id, PublicIp=elastic_ip)

print(f'Dirección IP elástica {elastic_ip} asociada con la instancia {instance_id}')