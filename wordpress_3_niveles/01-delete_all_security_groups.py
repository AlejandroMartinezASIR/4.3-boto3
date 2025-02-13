import boto3

# Crear cliente de EC2
ec2 = boto3.client('ec2')

# Describir grupos de seguridad
response = ec2.describe_security_groups()

# Extraer IDs de los grupos de seguridad
sg_id_list = [sg['GroupId'] for sg in response['SecurityGroups']]

# Eliminar grupos de seguridad
for sg_id in sg_id_list:
    print(f'Eliminando {sg_id} ...')
    ec2.delete_security_group(GroupId=sg_id)