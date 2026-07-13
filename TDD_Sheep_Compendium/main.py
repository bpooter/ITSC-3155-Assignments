from typing import List

from fastapi import FastAPI, HTTPException, status

from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    return db.get_sheep(id)

@app.post("/sheep/", response_model=Sheep, status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):

    # Check if the sheep ID already exists to avoid duplicates
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this id already exists")

    # Add new sheep to the database
    db.data[sheep.id] = sheep
    return sheep

@app.delete("/sheep/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_sheep(id: int):

    # raise 404 not found exception if the sheep is not in database
    if id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep with this id does not exist")

    # delete the sheep using the given id
    db.delete_sheep(id)

@app.put("/sheep/{id}",response_model=Sheep, status_code=status.HTTP_200_OK)
def update_sheep(id: int, sheep: Sheep):

    # raise 404 not found exception if the sheep is not in the database
    if id not in db.data:
        raise HTTPException(status_code=404, detail="Sheep with this id does not exist")

    # if found call update_sheep() in db.py
    return db.update_sheep(id, sheep.name, sheep.breed, sheep.sex)

#TODO look for a way to remove the id in the request body, should not be updating ID's

# response_model anticipates a list from this endpoint
@app.get("/sheep/", response_model=List[Sheep], status_code=status.HTTP_200_OK)
def read_all_sheep():

    # returns a list of all stored sheep
    return db.read_all_sheep()