from xml.etree import ElementTree

# Leitura do arquivo de exemplo do XML

parsedXml = ElementTree.parse("Exemplo de arquivo.xml")
print(parsedXml)

# Para extrair qual tag é a raiz do XML utilizamos a função getroot

root = parsedXml.getroot()

print(root.tag)
print(root.attrib)
print(root.attrib.get("year"))

# podemos buscar por tags especificas com a função findall
# sem o .attrib você irá retornar apenas o código hash do objeto
tags = []
for tag in root.findall("python"):
    tags.append(tag.tag)
    tags.append(tag.attrib)

print(tags)

tagas1 = []
for tag in root.findall("python"):
    tagas1.append(tag.find("modulos").text)

print(tagas1)
