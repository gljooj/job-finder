from typing import Annotated

from fastapi import FastAPI, Depends
from fastapi.security import HTTPBasicCredentials, HTTPBasic

from app.router import vendor, job
from config.auth import users

app = FastAPI(
    debug=True,
    title="Vendo Smart",
)

security = HTTPBasic()


@app.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    users.update({"username": credentials.username, "password": credentials.password})
    return {"username": credentials.username, "password": credentials.password}


app.include_router(vendor.router)
app.include_router(job.router)
