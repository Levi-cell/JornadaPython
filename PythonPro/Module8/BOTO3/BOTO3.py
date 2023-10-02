from boto3 import resource, client

"""Comente sempre que fizer um comando de criação de instância para
não criar outra instância"""
ec2 = resource("ec2", region_name="us-east-1")  # Região que você está na AWS
#
# # Criando instancia ec2
# # pegue o ID da AMI do sistema operacional ubuntu irá estar ao lado de arquitetura quando você for criar uma instância
# ec2.create_instances(ImageId="ami-053b0d53c279acc90", InstanceType="t2.micro", MinCount=1, MaxCount=1)

# note que na aws a instância foi criada

# Pegando informações da instância:
dados_instancia = ec2.meta.client.describe_instance_status()
print(dados_instancia)

# pegando informações mais completas:
aws = client("ec2", region_name="us-east-1")
dados_completos = aws.describe_instances()
print(dados_completos)

"""Comandos que alteram o estado da instância devem ser sempre
comentados depois de utilizados"""

# Parando a instância

# pegue o id da instância no site

print(ec2.instances.filter(InstanceIds=['i-0b85585f70b01e438']).stop())

# Encerrando a instância

print(ec2.instances.filter(InstanceIds=['i-0b85585f70b01e438']).terminate())



