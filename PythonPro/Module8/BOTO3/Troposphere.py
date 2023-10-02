from troposphere import Ref, Template, ec2
from pprint import pprint

template = Template()
# Image ID e Instance Type confira-os no site da AWS
instancia = ec2.Instance(
    "pythonproserver",
    ImageId="ami-053b0d53c279acc90",
    InstanceType="t2.micro"
)

print(template.add_resource(instancia))

"""É normal nada acontecer, o troposphere não estabelece conexão com a AWS
Ele apenas gera arquivos com parâmetros para serem seguidos por aplicações de gerenciamento
de serviços na nuvem como o AWS CloudFormation e o Terraform

A biblioteca e função pprint irá converter o template para o tipo de 
arquivo desejado e irá printar na tela"""

pprint(template.to_yaml())
print("    ")
pprint(template.to_json())
