from fastapi import HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

users = {
    "test": {
        "password": "Pass@123",
        "token": "",
        "priviliged": True
    }
}


def verification(creds: HTTPBasicCredentials = Depends(security)):
    username = creds.username
    password = creds.password
    if username in users and password == users[username]["password"]:
        print("User Validated")
        return True
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="user or password",
            headers={"WWW-Authenticate": "Basic"},
        )
