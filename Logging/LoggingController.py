

import uvicorn
from fastapi import FastAPI, APIRouter

from pydantic import BaseModel
from LoggingService import  LoggingService



class Item(BaseModel):
    id:int
    content : str


class LoggingController():

    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/", self.get_request, methods=["GET"])
        self.router.add_api_route("/", self.post_request, methods=["POST"])
        self.ls = LoggingService()
    async def get_request(self):
        print(f"Received get in logging...")
        list = self.ls.getLogs()
        return list

    async def post_request(self, item: Item):
        print(f"Received post: \"{item.content}\" in logging...")
        r = self.ls.addMessage(item)

        return item.content


if __name__ == "__main__":
    facade_port = 8002
    localhost = "127.0.0.1"
    app = FastAPI()
    fcd_cntrllr = LoggingController()
    app.include_router(fcd_cntrllr.router)
    uvicorn.run(app, host=localhost, port=facade_port)