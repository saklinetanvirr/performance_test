# from fastapi.testclient import TestClient
# from main import app, tasks

# client = TestClient(app)

# def setup_function():
#     tasks.clear()


# def test_create_task():
#     response = client.post("/tasks", json={"id": 1, "title": "Test Task"})
#     assert response.status_code == 200
#     assert response.json() == {"id": 1, "title": "Test Task", "done": False}


# def test_get_tasks():
#     # create a task first
#     client.post("/tasks", json={"id": 1, "title": "Test Task"})
#     response = client.get("/tasks")
#     assert response.status_code == 200
#     assert response.json() == [{"id": 1, "title": "Test Task", "done": False}]


# def test_mark_done():
#     client.post("/tasks", json={"id": 1, "title": "Test Task"})
#     response = client.put("/tasks/1")
#     assert response.status_code == 200
#     assert response.json()["done"] is True


# def test_delete_task():
#     client.post("/tasks", json={"id": 1, "title": "Test Task"})
#     response = client.delete("/tasks/1")
#     assert response.status_code == 200
#     assert response.json() == {"message": "Task deleted"}


# def test_duplicate_task_id():
#     # create the first task
#     client.post("/tasks", json={"id": 1, "title": "Task One"})
#     # try creating the same task again
#     response = client.post("/tasks", json={"id": 1, "title": "Task One"})
#     assert response.status_code == 400
#     assert response.json()["detail"] == "Task with this ID already exists"








import pytest
from fastapi.testclient import TestClient
from main import api, Book  # Adjust the import based on the file name of your FastAPI app

client = TestClient(api)

# Sample test data
sample_book = {
    "id": 1,
    "name": "Test Book",
    "description": "A book for testing",
    "isAvailable": True
}

updated_book = {
    "id": 1,
    "name": "Updated Test Book",
    "description": "Updated description",
    "isAvailable": False
}

def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Book Management System"}

def test_get_books_empty():
    response = client.get("/book")
    assert response.status_code == 200
    assert response.json() == []

def test_add_book():
    response = client.post("/book", json=sample_book)
    assert response.status_code == 200
    assert len(response.json()) == 1  # Check that the book was added
    assert response.json()[0]["name"] == sample_book["name"]

def test_update_book():
    # First, add a book
    client.post("/book", json=sample_book)
    
    # Now, update the book
    response = client.put("/book/1", json=updated_book)
    assert response.status_code == 200
    assert response.json()["name"] == updated_book["name"]
    assert response.json()["description"] == updated_book["description"]
    assert response.json()["isAvailable"] == updated_book["isAvailable"]

def test_update_book_not_found():
    response = client.put("/book/999", json=updated_book)
    assert response.status_code == 200
    assert response.json() == {"error": "Book Not Found"}

def test_delete_book():
    # First, add a book
    client.post("/book", json=sample_book)
    
    # Now, delete the book
    response = client.delete("/book/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

def test_delete_book_not_found():
    response = client.delete("/book/999")
    assert response.status_code == 200
    assert response.json() == {"error": "Book not found, deletion failed"}
