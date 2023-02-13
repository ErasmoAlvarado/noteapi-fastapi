from fastapi import APIRouter, HTTPException
from data.db.db_create import SessionLocal
from data.repositories.note import note_model,note_serializer
from datetime import datetime


router = APIRouter()
db = SessionLocal()


@router.get('/notes')
def get_all_notes():
    data = db.query(note_model.note).all()
    return data

@router.get('/notes/{id}')
def get_note(id:int):
    data = db.query(note_model.note).filter(note_model.note.id == id).first()

    if data is None:
        raise HTTPException(detail="your id does't exist",status_code=400) 

    return data

@router.post('/notes')
def add_note(note:note_serializer.note):
    data= db.query(note_model.note).filter(note_model.note.id == note.id).first()

    if data is not None:
        return HTTPException(detail="your note already existed",status_code=400)

    new_note=note_model.note(
        title = note.title,
        subtitle = note.subtitle,
        counter = note.counter,
        admin = note.admin,
        creation = datetime.now(),
        update = datetime.now()
    )
    db.add(new_note)
    db.commit()
    return ':)'
    
@router.put('/notes/{note_id}')
def change_note(note:note_serializer.note, note_id:int):
    data = db.query(note_model.note).filter(note_model.note.id == note_id).first()

    if data is None:
        raise HTTPException(detail="your id does't exist",status_code=400) 
    
    data.title = note.title
    data.subtitle = note.subtitle
    data.counter = note.counter
    data.update = datetime.now()
    data.admin = note.admin
    return ':)'
    
@router.delete('/notes/{id}')
def deleta_note(id:int):
    data = db.query(note_model.note).filter(note_model.note.id == id).first()

    if data is None:
        raise HTTPException(detail="your id does't exist",status_code=400)
    
    db.delete(data)
    db.commit()
 

