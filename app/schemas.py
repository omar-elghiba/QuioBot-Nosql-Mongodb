from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class CustomerSchema(BaseModel):
    username: str = Field(...)
    full_name: str = Field(...)
    email: EmailStr = Field(...)
    year: int = Field(..., gt=0, lt=99)

    class Config:
        schema_extra = {
            "example": {
                "username": "JohnDoe",
                "full_name": "John Doe",
                "email": "jdoe@x.edu.ng",
                "year": 22,
            }
        }


class UpdateCustomer(BaseModel):
    username: Optional[str]
    email: Optional[EmailStr]
    year: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "username": "John Doe",
                "email": "jdoe@x.edu.ng",
                "year": 22,
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
