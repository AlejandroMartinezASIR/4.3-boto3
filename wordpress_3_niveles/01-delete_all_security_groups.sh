import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Describe security groups
response = ec2.describe_security_groups()

# Extract security group IDs
sg_id_list = [sg['GroupId'] for sg in response['SecurityGroups']]

# Delete security groups
for sg_id in sg_id_list:
    print(f'Eliminando {sg_id} ...')
    ec2.delete_security_group(GroupId=sg_id)