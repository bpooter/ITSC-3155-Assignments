# Import TestClient to simulate API requests
from urllib import response

from fastapi.testclient import TestClient

# Import the FastAPI app instance from the controller module
from main import app

# Create a TestClient instance for the FastAPI app
client = TestClient(app)

def test_read_sheep():

    # Send a GET request to the endpoint "/sheep/1"
    response = client.get("/sheep/1")

    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200

    # Assert that the response JSON matches the expected data
    assert response.json() == {
        # Expected JSON structure
        "id":1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

def test_add_sheep():

    # New sheep data to be added
    new_sheep = {
        "id": 7,
        "name": "William",
        "breed": "Hebridean",
        "sex": "ram"
    }

    # send sheep data to POST endpoint
    response = client.post("/sheep", json=new_sheep)

    # assert that status_code is 201 created successful
    assert response.status_code == 201

    # assert sheep attributes match passed sheep data
    assert response.json() == new_sheep

    # checking the attributes of sheep with id 7
    success = client.get("/sheep/7")

    # assert status_code is OK
    assert success.status_code == 200

def test_delete_sheep():

    # Send a request to find sheep exists
    sheep_found = client.get("/sheep/1")

    # assert status_code is OK
    assert sheep_found.status_code == 200

    # assert that sheep is found
    assert sheep_found.json() == {
        "id": 1,
        "name": "Spice",
        "breed": "Gotland",
        "sex": "ewe"
    }

    # delete the sheep with id 1
    delete_response = client.delete("/sheep/1")

    # assert that no content found
    assert delete_response.status_code == 204

    # checking that sheep with id 1 is deleted using another delete
    deleted_check = client.delete("/sheep/1")

    # assert that 404 not found is status_code ensuring deletion
    assert deleted_check.status_code == 404


def test_update_sheep():

    # values to update sheep
    update = {"id": 2,
              "name" : "Test",
              "breed" : "Test",
              "sex" : "Test"}

    # update_response variable for testing
    update_response = client.put("/sheep/2", json=update)

    assert update_response.status_code == 200
    assert update_response.json() == {
        "id": 2,
        "name": "Test",
        "breed": "Test",
        "sex": "Test"
    }



def test_read_all_sheep():
    response = client.get("/sheep/")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 2,
            "name": "Test",
            "breed": "Test",
            "sex": "Test"
        },
        {
            "id": 3,
            "name": "Deedee",
            "breed": "Jacobs Four Horns",
            "sex": "ram"
        },
        {
            "id": 4,
            "name": "Rommy",
            "breed": "Romney",
            "sex": "ewe"
        },
        {
            "id": 5,
            "name": "Vala",
            "breed": "Valais Blacknose",
            "sex": "ewe"
        },
        {
            "id": 6,
            "name": "Esther",
            "breed": "Border Leicester",
            "sex": "ewe"
        },
        {
            "id": 7,
            "name": "William",
            "breed": "Hebridean",
            "sex": "ram"
        }
    ]
