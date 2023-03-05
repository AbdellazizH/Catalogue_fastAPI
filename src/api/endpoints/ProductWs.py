from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.core import schemas
from src.core.database.database import get_db
from src.core.models.Product import Product
from src.core.schemas.Product import Product
from src.core.service import ProductService

routeur = APIRouter()


# obtention de tous les produits
@routeur.get("/", response_model=list[schemas.Product])
async def get_all_products(db: Session = Depends(get_db)):
    return ProductService.get_all_products(db)


# obtention d'un produit via son ID
@routeur.get("/{id}", response_model=list[schemas.Product])
async def get_product_by_id(id: int):
    print('test')


# modification d'un produit via son ID
@routeur.put("/{id}")
async def update_product_by_id(product: Product, id: int):
    print('test')


# suppression d'un produit via son ID
@routeur.delete("/{id}")
async def delete_product_by_id(id: int):
    print('test')


# création d'un produit
@routeur.post("/")
async def create_product(product: Product):
    print("test")
