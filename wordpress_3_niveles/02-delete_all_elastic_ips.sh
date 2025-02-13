import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Describe Elastic IP addresses
response = ec2.describe_addresses()

# Extract Elastic IP allocation IDs
elastic_ip_ids = [address['AllocationId'] for address in response['Addresses']]

# Release Elastic IP addresses
for allocation_id in elastic_ip_ids:
    print(f'Eliminando {allocation_id} ...')
    ec2.release_address(AllocationId=allocation_id)