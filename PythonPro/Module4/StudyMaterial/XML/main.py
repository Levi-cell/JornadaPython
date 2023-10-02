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
tags = [tag.attrib for tag in root.findall("python")]
print(tags)
print("sem .attrib:")
tags = [tag for tag in root.findall("python")]
print(tags)

tags = [tag.find("modulos").text for tag in root.findall("python")]
print(tags)
