import boto3

# Crear cliente de EC2
ec2 = boto3.client('ec2')

# Describir instancias en ejecución
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)

# Extraer IDs de las instancias
instance_ids = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]

# Terminar instancias
if instance_ids:
    ec2.terminate_instances(InstanceIds=instance_ids)
    print(f'Instancias terminadas: {instance_ids}')
else:
    print('No se encontraron instancias en ejecución.')