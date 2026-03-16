import asyncio

from aiohttp import ClientSession


async def main():

    async with ClientSession() as session:

        # response = await session.post(
        #     "http://localhost:8080/adv",
        #     json={"title": "bike", "description": "it's a new one", "owner": "Andy"},
        # )
        # print('\nPOST')
        # print(response.status)
        # print(await response.json())
        #
        #
        response = await session.post(
            "http://localhost:8080/adv",
            json={"title": "auto", "description": "BMW", "owner": "Bob"}
        )
        print('\nPOST')
        print(response.status)
        print(await response.json())


        response = await session.get(
            "http://localhost:8080/adv/3",
        )
        print('\nGET')
        print(response.status)
        print(await response.text())

        #
        # response = await session.delete(
        #     "http://localhost:8080/adv/1",
        # )
        # print('\nDELETE')
        # print(response.status)
        # print(await response.text())


asyncio.run(main())
