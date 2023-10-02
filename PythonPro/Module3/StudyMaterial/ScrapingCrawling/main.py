from requests import get
from bs4 import BeautifulSoup


# Fazendo respagem do código de um site para termos um conteúdo para trabalhar

resposta = get("https://www.python.org/jobs/")

# Vamos utilizar o Beatiful Soup para mapear o conteúdo do código HTML

tags = BeautifulSoup(resposta.text, "html5lib")
help(tags)

# Para começar, vamos localizar a tag Title

title = tags.find("title")

print(title)

print(title.text)

# Agora vamos tentar extrair os títulos de cada vaga

subtitles = tags.find_all("h2")
x = [h2.text for h2 in subtitles]

print(x)

# Podemos fazer ficar mais claro se selecionarmos pela classe correta e navegarmos pelas tags

subtitles = tags.find_all("h2", attrs={"class": "listing-company"})
x = [h2.a.tex for h2 in subtitles]
print(x)

# Podemos construir um Web Crawler extraindo os links de cada vaga
# Perceba que utilizamos o subtitles
paraVisitar = ["https://www.python.org" + h2.a["href"] for h2 in subtitles]

print(paraVisitar)

sites = []
for pv in paraVisitar:
    acesso = get(pv)
    sites.append(get(pv))

print(sites)


"""Uma dica importante é que a separação por classes e a padronização do HTML depende dos desenvolvedores
do site. Então, pode ser que em alguns sites seja difícil navegar, pois não foram seguidas as boas práticas de
desenvolvimento """