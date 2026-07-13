from typing import Dict

from models.models import Sheep

class FakeDB:
    def __init__(self):
        self.data: Dict[int, Sheep] = {}

    def get_sheep(self, id: int) -> Sheep:
        return self.data.get(id)

    def add_sheep(self, sheep: Sheep) -> Sheep:

        # Check if the sheep ID already exists
        if sheep.id in self.data:
            raise ValueError(f"Sheep with id {sheep.id} already exists")
        # Add the new sheep to the database
        self.data[sheep.id] = sheep
        return sheep

    def delete_sheep(self, id: int):

        # Check if the sheep ID exists
        if id not in self.data:
            raise ValueError(f"Sheep with id {id} does not exist")

        # If found remove the id from the dictionary
        self.data.pop(id)

    def update_sheep(self, id: int, name: str, breed: str, sex: str) -> Sheep:

        # throw exception if given id not found
        if id not in self.data:
            raise ValueError(f"Sheep with id {id} does not exist")

        # initialize sheep object with sheep matching given id
        sheep = self.data.get(id)

        # assign values to sheep object
        sheep.name = name
        sheep.breed = breed
        sheep.sex = sex

        # return for showing endpoint
        return sheep

    def read_all_sheep(self):
        return list(self.data.values())


db = FakeDB()

db.data = {
    1: Sheep(id=1, name="Spice", breed="Gotland", sex="ewe"),
    2: Sheep(id=2, name="Blondie", breed="Polypay", sex="ram"),
    3: Sheep(id=3, name="Deedee", breed="Jacobs Four Horns", sex="ram"),
    4: Sheep(id=4, name="Rommy", breed="Romney", sex="ewe"),
    5: Sheep(id=5, name="Vala", breed="Valais Blacknose", sex="ewe"),
    6: Sheep(id=6, name="Esther", breed="Border Leicester", sex="ewe")
}