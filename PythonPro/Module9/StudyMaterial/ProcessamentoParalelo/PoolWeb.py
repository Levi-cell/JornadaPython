"""Agora vamos criar um pool de requisições para realizar um web scraping
"""

from multiprocessing import Pool
from requests import get


def scraper(url):
    res = get(url)
    I_got_a = res.json()
    print(I_got_a["name"], I_got_a["id"])


urls = [f"https://pokeapi.co/api/v2/pokemon/{pokemon}" for pokemon in range(1, 501)]
p = Pool(20)
p.map(scraper, urls)
p.terminate()
p.join()