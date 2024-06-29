from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field
from typing import Optional, List
import datetime

import time
from datetime import date

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category_id: int
    is_active: bool
    date: datetime

class ProductCreate(BaseModel):
    id: int
    name: str #= Field(min_length=5, max_length=15)
    description: str #= Field(min_length=5, max_length=50)
    price: float
    category_id: int #= Field(ge=1)
    is_active: bool
    date: datetime #= Field(le=datetime.date.today())

# gt, ge, lt, le

class ProductUpdate(BaseModel):
    #id: Optional[int] = None # or -> id: int | None = None
    name: str
    description: str
    price: float
    category_id: int
    is_active: bool

app.title = "My first app with FastAPI"
app.version = "2.0.0"

products = [
    {
        "id": 1,
        "name": "mouse",
        "description": "optic mouse",
        "price": 7.5,
        "category_id": 1,
        "is_active": True,
        "date": date.today()
    },
    {
        "id": 2,
        "name": "keyboard",
        "description": "mechanic keyboard",
        "price": 6.5,
        "category_id": 1,
        "is_active": True,
        "date": date.today()
    },
    {
        "id": 3,
        "name": "test",
        "description": "test test",
        "price": 5.5,
        "category_id": 2,
        "is_active": True,
        "date": date.today()
    }
]

@app.get('/', tags=['Home'])
def home():
    return "Hello World!"


@app.get('/products', tags=['Products'])
def get_products() -> List[Product]:
    # return html
    #return HTMLResponse('<h1>Hello World</h1>')
    return products


@app.get('/products/{id}', tags=['Products'])
def get_product(id: int) -> Product:
    for p in products:
        if p['id'] == id:
            return p
    return None

# query params
@app.get('/products/', tags=['Products'])
def get_product_by_category_id(category_id: int) -> Product:
    return [product for product in products if product['category_id'] == category_id]

@app.post('/products', tags=['Products'])
def create_product(product: ProductCreate) -> List[Product]:
    products.append(product.model_dump())
    return products

@app.put('/products/{id}', tags=['Products'])
def update_product(id: int, product: ProductUpdate) -> Product:
    for p in products:
        if p['id'] == id:
            p['name'] = product.name
            p['description'] = product.description
            p['price'] = product.price
            p['category_id'] = product.category_id
            p['is_active'] = product.is_active
            return p
    return None

@app.delete('/products/{id}', tags=['Products'])
def delete_product(id: int) -> List[Product]:
    for p in products:
        if p['id'] == id:
            products.remove(p)
    
    return products
