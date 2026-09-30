from fastapi import FastAPI, HTTPException, Response, status
from pydantic import BaseModel

app = FastAPI(title="Book API")


class BookCreate(BaseModel):
    title: str
    author: str
    year: int


books = {
    1: {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien", "year": 1937},
    2: {"id": 2, "title": "Kindred", "author": "Octavia E. Butler", "year": 1979},
}
next_book_id = 3


@app.get("/")
def read_root():
    return {"message": "Book API"}


@app.get("/books")
def list_books():
    pass


@app.get("/books/{book_id}")
def get_book(book_id: int):
    pass


@app.post("/books", status_code=status.HTTP_201_CREATED)
def create_book(book: BookCreate):
    pass


@app.put("/books/{book_id}")
def update_book(book_id: int, book: BookCreate):
    pass


@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int):
    pass