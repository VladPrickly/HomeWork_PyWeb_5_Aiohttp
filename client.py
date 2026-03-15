import asyncio

from aiohttp import ClientSession


async def main():

    async with ClientSession() as session:
        # response = await session.post(
        #     "http://localhost:8080/hello/world/42?some_key1=some_val1&some_key2=some_val2",
        #     json={"key_1": "val_1"},
        #     headers={"token": "xxxxx"}
        # )
        # print(response.status)
        # print(await response.text())

        # response = await session.post(
        #     "http://localhost:8080/users",
        #     json={"name": "user_2", "password": "1234"},
        # )
        # print(response.status)
        # print(await response.text())

        # response = await session.get(
        #     "http://localhost:8080/users/6",
        # )
        # print(response.status)
        # print(await response.text())

        # response = await session.get(
        #     "http://localhost:8080/users/2",
        # )
        # print(response.status)
        # print(await response.text())

        # response = await session.patch(
        #     "http://localhost:8080/users/4",
        #     json={"name": "new_user_name"},
        # )
        # print(response.status)
        # print(await response.text())

        # response = await session.get(
        #     "http://localhost:8080/users/4",
        # )
        # print(response.status)
        # print(await response.text())

        # response = await session.delete(
        #     "http://localhost:8080/users/4",
        # )
        # print(response.status)
        # print(await response.text())

        response = await session.get(
            "http://localhost:8080/users/4",
        )
        print(response.status)
        print(await response.text())


asyncio.run(main())


# import requests


# response = requests.post("http://127.0.0.1:5000/adv/",
#                          json={"title": "bike", "description": "it's a new one", "owner": "Andy"}
#                          )
# print(response.status_code)
# print(response.json())

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