import base64
import requests


# api endpoints and values
URL = "https://auth.sandbox.tripleup.dev/oauth2/token"
triple_id = ""
triple_secret = ""
grant_type = "client_credentials"

# authorization key must be base64 encoded and concatenate triple_id:triple_secret
byte_key = triple_id + ":" + triple_secret
byte_key = byte_key.encode("ascii")
triple_authorization_key = base64.b64encode(byte_key)
triple_authorization_key = triple_authorization_key.decode("ascii")


# making the request
def token_request():
    r = requests.post(
        URL,
        data={"grant_type": grant_type},
        headers={"Authorization": "Basic " + triple_authorization_key,
                 "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}
    )

    response = r.json()
    return {"token": response["access_token"]}
