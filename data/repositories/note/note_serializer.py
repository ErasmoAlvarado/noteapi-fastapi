from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from datetime import datetime


class note(BaseModel): #serializer
    id:Optional[int]
    title:str='empty note :)'
    subtitle:str='[¬º-°]¬'
    counter:int
    creation:datetime=datetime.now()
    update:datetime=datetime.now()
    admin:bool=False

    class Config:
        orm_mode=True