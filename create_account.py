import requests
import os
import pytz
import datetime
from pymongo import MongoClient
from token_request import token_request


# Database connection
mongodb_client = MongoClient(os.environ["MONGODB_URI"])
database = mongodb_client[os.environ["MONGODB_PREFERENCES_DB"]]
collection = database[os.environ["MONGODB_PREFERENCES_COLLECTION"]]


# Triple api endpoints and values
URL = "https://api.sandbox.tripleup.dev/partner/card-accounts/"


def register_mongo_user(card_account):
    current_date = datetime.datetime.now()

    data = {
        "card_account": card_account,
        "last_updated":current_date,
        "liked_offers": [],
        "disliked_offers": [],
        "recommended_offers": []
    }

    new_user = collection.insert_one(data)
    created_user = collection.find_one({"_id": new_user.inserted_id})
    return created_user


def create_card_account(params):
    token = token_request()

    requestURL = "https://api.sandbox.tripleup.dev/partner/card-accounts"
    data = {
        "card_program_external_id": "gauthier-card-program-01",
        "default_country_code": "US",
        "default_postal_code": params['default_postal_code'],
        "external_id": params['external_id'],
    }

    r = requests.post(
        requestURL,
        json = data,
        headers={"Authorization": "Bearer " + token["token"],
                 "Content-Type": "application/json"}
    )

    response = r.json()
    register_mongo_user(response['id'])
    return response

