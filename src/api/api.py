from fastapi import APIRouter
from src.api.endpoints import ProductWs, CatalogWS, SalesWS

routeur = APIRouter()
routeur.include_router(
    productWs.routeur,
    prefix='/product',
    tags=["product"],
    responses={404: {"description": "Impossible"}}
)

routeur.include_router(
    CatalogWS.routeur,
    prefix='/catalog',
    tags=["catalog"],
    responses={404: {"description": "Impossible"}}
)

routeur.include_router(
    SalesWS.routeur,
    prefix='/sales',
    tags=["sales"],
    responses={404: {"description": "Impossible"}}
)

