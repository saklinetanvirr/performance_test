# # from fastapi import FastAPI
# # from pydantic import BaseModel
# # from typing import List

# # api = FastAPI()

# # @api.get("/")
# # def inventory():
# #     return {"Message": "welcome"}

# # class Product(BaseModel):
# #     id: int
# #     name: str
# #     descrption: str
# #     price: int
# #     qnt: int

# # product: List[Product] = []

# # @app.get("/get", response_model = Product)
# # def get_all_products():
# #     return product

# # @app.get("/get/{product_id}", response_model=Product)
# # def get_product(product_id:int):
# #     for p in product:
# #         if p.id == product_id:
# #             return product

# # @app.post("/post")
# # def create_product(new_product: Product):
# #     for p in product:
# #         if p.id == new_product.id:
# #             return {"already exists"}
# #         product.append(new_product)
# #         return {"seccessful"}

# # @app.put("/put")
# # def update_product(product_id: int, updated_product: Product):
# #     for i, product in enumerate(product):
# #         if p.id == product_id:
# #             product[i] = updated_product
# #             return {"Product updated successfully"}
# #     return {"message": "Product not found"}

# # @api.delete("/delete/{product_id}")
# # def delete_product(product_id: int):
# #     for i, p in enumerate(product):
# #         if p.id == product_id:
# #             product.pop(i)
# #             return{"message": "Product deleted successfully"}
# #     return{"message": "product not found"}
    


# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from typing import List

# app = FastAPI()

# # Task model
# class Task(BaseModel):
#     id: int
#     title: str
#     done: bool = False

# @app.get("/")
# def home():
#     return {"message": "Hello World"}

# # In-memory storage
# tasks: List[Task] = []


# # Create a task
# @app.post("/tasks", response_model=Task)
# def create_task(task: Task):
#     if any(t.id == task.id for t in tasks):
#         raise HTTPException(status_code=400, detail="Task with this ID already exists")
#     tasks.append(task)
#     return task

# # Get all tasks
# @app.get("/tasks", response_model=List[Task])
# def get_tasks():
#     return tasks

# # Mark task as done
# @app.put("/tasks/{task_id}", response_model=Task)
# def mark_done(task_id: int):
#     for task in tasks:
#         if task.id == task_id:
#             task.done = True
#             return task
#     raise HTTPException(status_code=404, detail="Task not found")

# # Delete a task
# @app.delete("/tasks/{task_id}")
# def delete_task(task_id: int):
#     for task in tasks:
#         if task.id == task_id:
#             tasks.remove(task)
#             return {"message": "Task deleted"}
#     raise HTTPException(status_code=404, detail="Task not found")






from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

api = FastAPI()

class Book(BaseModel):
    id: int
    name: str
    description: str
    isAvailable: bool

books: List[Book] = []

@api.get("/")
def index():
    return {"Message": "Welcome to the Book Management System"}

@api.get("/book")
def get_books():
    return books

@api.post("/book")
def add_book(book: Book):
    books.append(book)
    return books

@api.put("/book/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = updated_book
            return updated_book
    return {"error": "Book Not Found"}

@api.delete("/book/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            deleted_book = books.pop(index)
            return deleted_book
    return {"error": "Book not found, deletion failed"}