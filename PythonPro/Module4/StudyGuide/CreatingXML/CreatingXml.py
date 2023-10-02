import xml.etree.cElementTree as ET

# vamos criar o root (raiz) que é a macração pela qual outras maracações vão ser criadas:
root = ET.Element("xml")

"""Em seguida, vamos criar os elementos nome, telefone e endereço. Para elemento um texto relacionado a ele
será definido. Além disso, os elementos criados serão adicionados"""

nome = ET.Element("Nome")
nome.text = "Fulano da Silva"
root.append(nome)

telefone = ET.Element("Telefone")
telefone.text = "11 999999999"
root.append(telefone)

endereco = ET.Element("Endereco")
endereco.text = "Rua xyz,423"
root.append(endereco)

# Pronto, agora vamos criar o documento xml e salva-lo com o nome meu PrimeiroXML.xml

tree = ET.ElementTree(root)

tree.write("meuPrimeiroXML.xml")