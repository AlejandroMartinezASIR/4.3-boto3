import boto3

# Crear cliente de EC2
ec2 = boto3.client('ec2')

# Describir direcciones IP elásticas
response = ec2.describe_addresses()

# Extraer IDs de asignación de IP elásticas
elastic_ip_ids = [address['AllocationId'] for address in response['Addresses']]

# Liberar direcciones IP elásticas
for allocation_id in elastic_ip_ids:
    print(f'Eliminando {allocation_id} ...')
    ec2.release_address(AllocationId=allocation_id)