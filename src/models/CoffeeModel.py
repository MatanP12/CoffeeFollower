from sqlmodel import Field, SQLModel
from .CoffeeType import CoffeeType
from datetime import datetime

class CoffeBaseModel(SQLModel):
    type: CoffeeType
    creation_time : datetime = datetime.now()

class Coffee(CoffeBaseModel, table=True):
    id: int | None = Field(default=None,primary_key=True)

class CoffeeView(CoffeBaseModel):
    id: int

class CoffeeCreate(CoffeBaseModel):
    pass

class CoffeeUpdate(CoffeBaseModel):
    type: CoffeeType | None = None
    creation_time: datetime | None = None