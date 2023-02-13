from sqlalchemy import Column,String,Integer,DateTime,Boolean
from data.db.db_create import Base
from datetime import datetime


class note(Base):
    __tablename__ = "notes"
    id=Column(Integer, primary_key=True)
    title = Column(String)
    subtitle =Column(String)
    counter=Column(Integer,default=0, onupdate=0)
    creation=Column(DateTime,default=datetime.now(), onupdate=datetime.now())
    update=Column(DateTime,default=datetime.now(), onupdate=datetime.now())
    admin=Column(Boolean,default=False,onupdate=False)

    def get_data(self):
        return f"id:{self.index}\n title:{self.title}\nsubtitle{self.subtitle},\ncounter{self.counter}"