import json

from aiohttp import web
from sqlalchemy.exc import IntegrityError
from db import Session, Advertisement, close_orm, init_orm

app = web.Application()

async def orm_context(app: web.Application):
    print("START")
    await init_orm()
    yield
    await close_orm()
    print("FINISH")


app.cleanup_ctx.append(orm_context)



class HttpError(Exception):  # Класс для обработки ошибок
    def __init__(self, status_code: int, message: dict | list | str):
        self.status_code = status_code
        self.message = message



class AdvView(web.View):


    async def get(self):
        adv_id = int(self.request.match_info["adv_id"])
        async with Session() as session:
            adv = await session.get(Advertisement, adv_id)
            if adv is None:
                raise web.HTTPNotFound(
                    text=json.dumps({"error": "Adv with id # {adv_id} doesn't exist"}),
                    content_type="application/json",
                )
            return web.json_response(adv.to_dict)


    async def post(self):
        json_data = await self.request.json()
        async with Session() as session:
            adv = Advertisement(**json_data)
            session.add(adv)
            try:
                await session.commit()
                # session.refresh(adv)
            except IntegrityError:
                raise web.HTTPConflict(
                    text=json.dumps({"error": "Adv with id # {adv_id} already exist"}),
                    content_type="application/json",
                )
            return web.json_response(adv.to_dict)

#
#
#     def delete(self, adv_id: int):
#         with Session() as session:
#             adv = get_adv(session, adv_id)
#             session.delete(adv)
#             session.commit()
#             return jsonify({'status': 'completed'})
#
#



app.add_routes(
    [
        web.post("/adv", AdvView),
        web.get(r"/adv/{adv_id:\d+}", AdvView),
        # web.delete(r"/users/{user_id:\d+}", AdvView),
    ]
)

#
if __name__ == '__main__':
    web.run_app(app, host='0.0.0.0', port=8080)

