from fastapi import FastAPI
from data.db.db_init import init_db
from data.router.note_router import router
from fastapi.middleware.cors import CORSMiddleware


init_db()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router) 




