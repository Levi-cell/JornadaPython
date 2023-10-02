from asyncio import ensure_future, gather, get_event_loop
from aiohttp import ClientSession


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.json()


async def run():
    tasks = []
    async with ClientSession() as session:
        for pokemon in range(1, 501):
            task = ensure_future(
                fetch(
                    session,
                    f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
                )
            )
            tasks.append(task)

        responses = await gather(*tasks)
        [print(resp["id"], resp["name"]) for resp in responses]

loop = get_event_loop()
future = ensure_future(run())
loop.run_until_complete(future)

