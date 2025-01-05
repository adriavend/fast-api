from pydantic import BaseModel, Field, validator
from datetime import date

# gt, ge, lt, le

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category_id: int
    is_active: bool
    date: date

class ProductCreate(BaseModel):
    id: int
    name: str #= Field(min_length=5, max_length=15)
    description: str #= Field(min_length=5, max_length=50)
    price: float
    category_id: int #= Field(ge=1)
    is_active: bool
    date: str #= Field(le=datetime.date.today())

    # example value
    model_config = {
        'json_schema_extra': {
            'example':
            {
                'id': 0,
                'name': 'My Product',
                'description': 'Product description',
                'price': 10.9,
                'category_id': 1,
                'is_active': True,
                'date': date.today().strftime('%Y-%m-%d')
            }
        }
    }

    # custom error validators
    @validator('name')
    def validate_name(cls, value):
        if len(value) < 5:
            raise ValueError('Name filed must have a minimun length of 5 characters')
        if len(value) > 15:
            raise ValueError('Name filed must have a maximun length of 15 characters')
        return value


class ProductUpdate(BaseModel):
    #id: Optional[int] = None # or -> id: int | None = None
    name: str
    description: str
    price: float
    category_id: int
    is_active: bool
