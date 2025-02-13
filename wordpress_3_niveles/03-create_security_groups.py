import boto3

# Load environment variables
import os
from dotenv import load_dotenv

load_dotenv()

SECURITY_GROUP_FRONTEND = os.getenv('SECURITY_GROUP_FRONTEND')
SECURITY_GROUP_BACKEND = os.getenv('SECURITY_GROUP_BACKEND')
SECURITY_GROUP_NFS = os.getenv('SECURITY_GROUP_NFS')
SECURITY_GROUP_BALANCEADOR = os.getenv('SECURITY_GROUP_BALANCEADOR')

# Create EC2 client
ec2 = boto3.client('ec2')

def create_security_group(group_name, description):
    response = ec2.create_security_group(
        GroupName=group_name,
        Description=description
    )
    return response['GroupId']

def authorize_ingress(group_name, protocol, port, cidr):
    ec2.authorize_security_group_ingress(
        GroupName=group_name,
        IpProtocol=protocol,
        FromPort=port,
        ToPort=port,
        CidrIp=cidr
    )

# Frontend
create_security_group(SECURITY_GROUP_FRONTEND, "Reglas para el frontend")
authorize_ingress(SECURITY_GROUP_FRONTEND, 'tcp', 22, '0.0.0.0/0')
authorize_ingress(SECURITY_GROUP_FRONTEND, 'tcp', 80, '0.0.0.0/0')
authorize_ingress(SECURITY_GROUP_FRONTEND, 'tcp', 443, '0.0.0.0/0')

# Backend
create_security_group(SECURITY_GROUP_BACKEND, "Reglas para el backend")
authorize_ingress(SECURITY_GROUP_BACKEND, 'tcp', 22, '0.0.0.0/0')
authorize_ingress(SECURITY_GROUP_BACKEND, 'tcp', 3306, '0.0.0.0/0')

# NFS
create_security_group(SECURITY_GROUP_NFS, "Reglas para el nfs")
authorize_ingress(SECURITY_GROUP_NFS, 'tcp', 22, '0.0.0.0/0')
authorize_ingress(SECURITY_GROUP_NFS, 'tcp', 2049, '0.0.0.0/0')

# Balanceador
create_security_group(SECURITY_GROUP_BALANCEADOR, "Reglas para el balanceador")
authorize_ingress(SECURITY_GROUP_BALANCEADOR, 'tcp', 22, '0.0.0.0/0')
authorize_ingress(SECURITY_GROUP_BALANCEADOR, 'tcp', 80, '0.0.0.0/0')
authorize_ingress(SECURITY_GROUP_BALANCEADOR, 'tcp', 443, '0.0.0.0/0')