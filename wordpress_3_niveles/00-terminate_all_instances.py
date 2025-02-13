import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Describe running instances
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]
)

# Extract instance IDs
instance_ids = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]

# Terminate instances
if instance_ids:
    ec2.terminate_instances(InstanceIds=instance_ids)
    print(f'Terminated instances: {instance_ids}')
else:
    print('No running instances found.')