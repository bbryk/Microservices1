

import uvicorn
from fastapi import FastAPI, APIRouter

from pydantic import BaseModel



class Item(BaseModel):
    id:int
    content : str


class LoggingRepository():
    def __init__(self):
        self.map = dict()
    def addToMap(self,msg:Item):
        self.map[msg.id] = msg.content
        print(self.map)


    def getLogsFromMap(self):
        return ", ".join(self.map.values())
