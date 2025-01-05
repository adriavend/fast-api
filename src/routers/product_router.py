from fastapi import Path, Query, APIRouter
from fastapi.responses import JSONResponse
from typing import Optional, List

from src.models.product_model import Product, ProductCreate, ProductUpdate

products: List[Product] = []

product_router = APIRouter()

@product_router.get('/products', tags=['Products'], 
    status_code=200, #status code by default
    response_description='This should return a json response') 
def get_products() -> List[Product]:
    # return products
    resp = [product.model_dump() for product in products]
    return JSONResponse(content=resp, status_code=200)
    # return content


@product_router.get('/products/{id}', tags=['Products'])
def get_product(id: int = Path(gt=0)) -> Product | dict:
    for p in products:
        if p.id == id:
            return JSONResponse(content=p.model_dump(), status_code=200)
    return JSONResponse(content={}, status_code=404)

# query params
# @product_router.get('/products/', tags=['Products'], response_model=List[Product])
# def get_product_by_category_id(category_id: int = Path(gt=0)) -> List[Product]:
#     return [product for product in products if product['category_id'] == category_id]

@product_router.get('/products/', tags=['Products'], response_model=Product)
def get_product_by_name(name: str = Query(min_length=2, max_length=50)) -> Product | dict:
    for p in products:
        if p.name == name:
            return JSONResponse(content=p.model_dump(), status_code=200)
    return JSONResponse(content={}, status_code=404)

@product_router.post('/products', tags=['Products'])
def create_product(product: ProductCreate) -> List[Product]:
    product.id = len(products) + 1
    products.append(product)
    resp = [p.model_dump() for p in products]
    return JSONResponse(content=resp)
    # return RedirectResponse(url='/products', status_code=303)

@product_router.put('/products/{id}', tags=['Products'])
def update_product(id: int, product: ProductUpdate) -> Product:
    for p in products:
        if p.id == id:
            p.name = product.name
            p.description = product.description
            p.price = product.price
            p.category_id = product.category_id
            p.is_active = product.is_active
            return JSONResponse(content=p.model_dump())
    return JSONResponse(content={}, status_code=404)

@product_router.delete('/products/{id}', tags=['Products'])
def delete_product(id: int) -> List[Product]:
    for p in products:
        if p.id == id:
            products.remove(p)
    resp = [product.model_dump() for product in products]
    return JSONResponse(content=resp)
