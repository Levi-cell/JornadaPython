"""Importando as bibliotecas"""
from pprint import pprint
from troposphere import Template, ec2
import yaml


# Função para criar instância

def gera_instancia(nome, image_id, instance_type, ):
    """Aqui a ideia é pedir como argumento
     os dados da instância e retornara instância criada com esses dados
     """
    instancia = ec2.Instance(
        nome,
        ImageId=image_id,
        InstanceType=instance_type
    )
    return instancia


def gera_template():
    """Aqui iremos definir os paramêtros e chamar a função que
     irá gerar a instância e em seguida geraremos o template"""
    temp = Template()

    # Fazendo imagens desejadas

    image_id = "ami-053b0d53c279acc90"
    image_id2 = "ami-053b0d53c279acc90"
    image_id3 = "ami-053b0d53c279acc90"

    instance_type = "t2.micro"
    instance_type2 = "t2.micro"
    instance_type3 = "t2.micro"

    instancia1 = gera_instancia("Atividade", image_id, instance_type)
    instancia2 = gera_instancia("Atividade2", image_id2, instance_type2)
    instancia3 = gera_instancia("Atividade3", image_id3, instance_type3)

    temp.add_resource(instancia1)
    temp.add_resource(instancia2)
    temp.add_resource(instancia3)

    pprint(temp.to_yaml())
    print("    ")
    pprint(temp.to_json())
    print("    ")

    return temp


def generate_yaml_from_template(template_exemplo):
    """Gerando arquivo yaml com o template"""
    return yaml.safe_dump(template_exemplo.to_dict(), default_flow_style=False)


if __name__ == "__main__":
    template = gera_template()
    yaml_file = generate_yaml_from_template(template)

    with open("dados.yaml", "w", encoding="ISO-8859-1 (Latin-1)") as yaml_config:
        yaml_config.write(yaml_file)

    print("Arquivo config.yaml foi gerado com sucesso" + "\n")

    with open("dados.yaml", "r", encoding="ISO-8859-1 (Latin-1)") as yaml_config:
        print(yaml_config.read())
