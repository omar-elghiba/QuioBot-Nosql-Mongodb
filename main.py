from fastapi import FastAPI
from src.app.routers.customer import router

app = FastAPI()

app.include_router(router, tags=["Customer"], prefix="/customer")

@app.get('/')
def Hello():
    return('Welcome To FastApi And MongoDB')






