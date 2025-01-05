from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

import time
from datetime import date

app = FastAPI()

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
def get_products():
    # return html
    #return HTMLResponse('<h1>Hello World</h1>')
    return products


@app.get('/products/{id}', tags=['Products'])
def get_product(id: int):
    for p in products:
        if p['id'] == id:
            return p
    return None

# query params
@app.get('/products/', tags=['Products'])
def get_product_by_category_id(category_id: int):
    return [product for product in products if product['category_id'] == category_id]

@app.post('/products', tags=['Products'])
def create_product(
        id: int = Body(), 
        name: str = Body(), 
        description: str = Body(), 
        price: float = Body(), 
        category_id: int = Body()
    ):
    products.append({
        "id": id,
        "name": name,
        "description": description,
        "rating": price,
        "category_id": category_id,
        "is_active": True,
        "date": date.today()
    })
    return products

@app.put('/products/{id}', tags=['Products'])
def update_product(
        id: int,
        name: str = Body(), 
        description: str = Body(), 
        price: float = Body(), 
        category_id: int = Body(),
        is_active: bool = Body()
    ):
    for p in products:
        if p['id'] == id:
            p['name'] = name
            p['description'] = description
            p['price'] = price
            p['category_id'] = category_id
            p['is_active'] = is_active
            return p
    return None

@app.delete('/products/{id}', tags=['Products'])
def delete_product(id: int):
    for p in products:
        if p['id'] == id:
            products.remove(p)
    
    return products
