import asyncio
from asyncio import coroutine, get_event_loop
from requests import get
from time import time
from asgiref.sync import sync_to_async

url_list = [
    "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
    "https://books.toscrape.com/catalogue/category/books/mystery_3/index.html",
    "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html",
    "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
]



def concorrente():
    @coroutine
    def web_scrape():
        loop = get_event_loop()
        scrape_list = [loop.run_in_executor(None, get, url) for url in url_list]
        for scrape in scrape_list:
            resp = yield from scrape
            print(resp.ok)

    loop = get_event_loop()
    loop.run_until_complete(web_scrape())


def comum():
    for url in url_list:
        print(get(url).ok)


start = time()
concorrente()  # use comum ou concorrente
print(f"Tempo total: {abs(int(time() - start))}")