import xml.etree.ElementTree as ET


tree = ET.parse("meuPrimeiroXML.xml")
root = tree.getroot()

# Para recuperar os dados que queremos, por exemplo o nome, fazemos:

print(tree.find('Nome').text)