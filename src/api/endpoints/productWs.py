from fastapi import APIRouter

routeur = APIRouter()

@routeur.get("/")
async def hello_world(username: str):
    return {"message": f"Hello {username}"}
