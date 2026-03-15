import asyncio

from aiohttp import ClientSession


async def main():

    async with ClientSession() as session:

        response = await session.post(
            "http://localhost:8080/adv",
            json={"title": "bike", "description": "it's a new one", "owner": "Andy"},
        )
        print(response.status)
        print(await response.json())


        response = await session.post(
            "http://localhost:8080/adv",
            json={"title": "auto", "description": "BMW", "owner": "Bob"}
        )
        print(response.status)
        print(await response.json())

        # response = await session.get(
        #     "http://localhost:8080/adv/1",
        # )
        # print(response.status)
        # print(await response.text())


        # response = await session.delete(
        #     "http://localhost:8080/adv/1",
        # )
        # print(response.status)
        # print(await response.text())



asyncio.run(main())



# response = requests.post("http://127.0.0.1:5000/adv/",
#                          json={"title": "auto", "description": "BMW", "owner": "Bob"}
#                          )
# print(response.status_code)
# print(response.json())


# response = requests.get("http://127.0.0.1:5000/adv/2")
# print(response.status_code)
# print(response.json())

# response = requests.delete("http://127.0.0.1:5000/adv/2")
# print(response.status_code)
# print(response.json())