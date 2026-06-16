from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Food(BaseModel):
    id: int
    category: str
    name: str
    price: float


food_instance = [Food(id=1, category="meat", name="ham", price=5.2), Food(id=4, category="meat", name="turkey", price=5.5), Food(id=2, category="bread", name="white", price=2.5), Food(id=5, category="bread", name="whole-grain", price=2.5), Food(id=3, category="cheese", name="provolone", price=1.5), Food(id=6, category="cheese", name="american", price=.95)]


@app.get("/")
def read_all():
    return food_instance


@app.get("/items/id/{item_id}")
def read_item(item_id: int):
    for item in food_instance:
        if item.id == item_id:
            return item
    return "Item not Found!"

@app.get("/items/category/{item_category}")
def read_item(item_category: str):
    return [
        item for item in food_instance
        if item.category == item_category
    ]

@app.post("/items")
def write_item(food: Food):
    food_instance.append(food)
    return food_instance


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Food):
    is_found = False
    for index, instance in enumerate(food_instance):
        if instance.id == item_id:
            food_instance[index] = Food(id=item.id, category=item.category, name=item.name, price=item.price)
            is_found = True
            break
    if not is_found:
        return "Item not Found!"

    return food_instance


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    is_found = False
    for index, instance in enumerate(food_instance):
        if instance.id == item_id:
            del food_instance[index]
            is_found = True
            break
    if not is_found:
        return "Item not Found!"

    return food_instance
