from yaml import load, FullLoader, dump

# abrindo arquivo
with open("ExemploYAML.yml") as file:
    yamlFile = load(file, Loader=FullLoader)
# Note que ele imprime em formato dicionario
print(yamlFile)

# Agora vamos criar um arquivo YAML

dict2Yaml = {
    "formatos" : [
        "json",
        "yaml"
    ],
    "markup languages": [
        "html",
        "xml",
        "sgml"
    ]
}

with open("novoYaml.yml", "w") as file:
    dump(dict2Yaml, file)

print(dict2Yaml)