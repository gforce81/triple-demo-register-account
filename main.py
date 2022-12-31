import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router as recs_router
from pymongo import MongoClient
from dotenv import dotenv_values


app = FastAPI()

config = dotenv_values(".env")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.on_event("startup")
async def startup_function():
    app.mongodb_client = MongoClient(os.environ["MONGODB_URI"])
    app.database = app.mongodb_client[os.environ["MONGODB_PREFERENCES_DB"]]


@app.on_event("shutdown")
async def shutdown_function():
    app.mongodb_client.close()

app.include_router(recs_router, tags=["triple"])
