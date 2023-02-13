from data.db.db_create import Base,engine
from data.repositories.note.note_model import note


def init_db():
    print('creating db....')
    Base.metadata.create_all(bind=engine)
    print(':)')