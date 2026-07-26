from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Restaurant(BaseModel):
    id: int
    name: str

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Welcome! to restaurant API"}


restaurants = [
    {"id": 1, "name": "Domino's"},
    {"id": 2, "name": "Pizza hut"},
    {"id": 3, "name": "Burger king"}
]

@app.get("/restaurants")
def get_restaurant():
    return restaurants

@app.get("/restaurants/{restaurants_id}")
def get_restaurants(restaurants_id: int):

    for restaurant in restaurants:
        if(restaurant["id"] == restaurants_id):
            return restaurant

    return {"message": "Restaurant no found"}

@app.post("/restaurants")
def add_restaurant(restaurant: Restaurant):
    restaurants.append(restaurant.model_dump())
    return {
        "message": "Restaurant added successfully"
    }

@app.put("/restaurants/{restaurant_id}")
def update_restaurant(restaurant_id: int, updated_restaurant: Restaurant):

    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            restaurants[restaurants.index(restaurant)] = updated_restaurant.model_dump()
            return {
                "message": "Restaurant updated successfully"
            }
    return {
        "message": "Restaurant not found"
    }

@app.delete("/restaurants/{restaurant_id}")
def delete_restaurant(restaurant_id: int):
    for restaurant in restaurants:
        if restaurant["id"] == restaurant_id:
            restaurants.remove(restaurant)

            return {
                "message": "Restaurant deleted successfully"
            }
    return {
        "message": "Restaurant not found"
    }







        
    

