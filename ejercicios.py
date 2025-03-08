import boto3

# Ejercicio 1: Crear un grupo de seguridad
ec2 = boto3.client('ec2')

# Crear el grupo de seguridad
response = ec2.create_security_group(
    GroupName='Grupo-ejercicio',
    Description='Grupo de seguridad para backend'
)
security_group_id = response['GroupId']

# Añadir reglas al grupo de seguridad
ec2.authorize_security_group_ingress(
    GroupId=security_group_id,
    IpPermissions=[
        {
            'IpProtocol': 'tcp',
            'FromPort': 22,
            'ToPort': 22,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        },
        {
            'IpProtocol': 'tcp',
            'FromPort': 3306,
            'ToPort': 3306,
            'IpRanges': [{'CidrIp': '0.0.0.0/0'}]
        }
    ]
)

print(f"Grupo de seguridad 'Grupo-ejercicio' creado con ID: {security_group_id}")

# Ejercicio 2: Crear una instancia EC2
response = ec2.run_instances(
    ImageId='ami-04b4f1a9cf54c11d0',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='vockey',
    SecurityGroupIds=[security_group_id],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Instancia-ejercicio'
                }
            ]
        }
    ]
)

instance_id = response['Instances'][0]['InstanceId']
print(f"Instancia EC2 'Instancia-ejercicio' creada con ID: {instance_id}")