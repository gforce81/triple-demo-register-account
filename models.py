from pydantic import BaseModel, Field
from typing import Optional
import uuid
import datetime


class TokenResponse(BaseModel):
    token: str = Field(title="Triple Publisher Token")


class CreateCardAccount(BaseModel):
    external_id: str = Field(title="The external/publisher given ID for the card account")
    default_postal_code: str = Field(title="The default postal code for the card account")

