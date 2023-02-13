from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# your database
engine=create_engine('',
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
