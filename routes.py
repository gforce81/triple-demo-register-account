from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from dotenv import dotenv_values
import os
from models import CreateCardAccount
from token_request import token_request
from create_account import create_card_account


router = APIRouter()


@router.post("/create_card_account")
async def register_card_account(request: Request, createcardaccount: CreateCardAccount = Body(...)):
    try:
        createcardaccount = jsonable_encoder(createcardaccount)
        return create_card_account(createcardaccount)
    except Exception as e:
        print(str(e))
        raise HTTPException(status_code=500, detail="Error creating card account",
                            headers={"X-Header-Error": "Error creating card account"})

