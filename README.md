# WORDPRESS EN TRES NIVELES CON PYTHON
Si queremos utilizar las credenciales de **AWS Academy** solo tenemos que copiar en el archivo `~/.aws/credentials` los datos que nos aparecen en el apartado **AWS Details** -> **Cloud Access** -> **AWS CLI**, dentro del **Learner Lab** de **AWS Academy**.

## 00-terminate_all_instances.py
Este script utiliza **boto3** para terminar instancias en ejecución:
- **`boto3.client('ec2')`**: Crea un cliente de EC2.
- **`ec2.describe_instances`**: Describe las instancias en ejecución.
- **`ec2.terminate_instances`**: Termina las instancias especificadas.

## 01-delete_all_security_groups.py
Este script sirve para eliminar todos los grupos de seguridad existentes en la cuenta de **AWS**.
- **`boto3.client('ec2')`**: Crea un cliente de EC2.
- **`ec2.describe_security_groups`**: Describe los grupos de seguridad.
- **`ec2.delete_security_group`**: Elimina el grupo de seguridad especificado.

## 02-delete_all_elastic_ips.py
Este script sirve para liberar todas las direcciones **IP elásticas** asociadas en la cuenta de **AWS**.
- **`boto3.client('ec2')`**: Crea un cliente de EC2.
- **`ec2.describe_addresses`**: Describe las direcciones IP elásticas.
- **`ec2.release_address`**: Libera la dirección IP elástica especificada.

## 03-create_security_groups.py
Este script utiliza **boto3** para crear grupos de seguridad y definir reglas de acceso para **Frontend**, **Backend**, **NFS** y **Balanceador** especificados en el archivo `.env`.
- **`boto3.client('ec2')`**: Crea un cliente de EC2.
- **`ec2.create_security_group`**: Crea un grupo de seguridad.
- **`ec2.authorize_security_group_ingress`**: Define reglas de acceso para el grupo de seguridad.

## 04-create_instances.py
Estas secciones del script utilizan **boto3** para lanzar instancias en **AWS**, especificando diferentes grupos de seguridad y etiquetas para cada tipo de instancia **Frontend**, **Backend**, **NFS** y **Balanceador**.
- **`boto3.client('ec2')`**: Crea un cliente de EC2.
- **`ec2.run_instances`**: Lanza una instancia con los parámetros especificados.

## 05-create_elastic_ip.py
Este script utiliza **boto3** para realizar las siguientes acciones:
1. Obtiene la **ID** de la instancia con un nombre específico y que está en estado **"running"**.
2. Asigna una nueva dirección **IP elástica**.
3. Asocia la dirección **IP elástica** recién asignada con la **instancia** identificada anteriormente.
- **`boto3.client('ec2')`**: Crea un cliente de EC2.
- **`ec2.describe_instances`**: Describe las instancias para obtener la ID de la instancia.
- **`ec2.allocate_address`**: Asigna una nueva dirección IP elástica.
- **`ec2.associate_address`**: Asocia la dirección IP elástica con la instancia especificada.