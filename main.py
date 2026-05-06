from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel , Field 

app = FastAPI()

books = [
    {
        'id': 1,
        'title': 'Ассинхронность в Python',
        'author': 'Мэтью'
    },
    {
        'id': 2,
        'title': 'Backend Разработка на Python',
        'author': 'Артем'
    }
]



@app.get("/books", summary="Основные Книги которые Имеются", tags=["Книги"])
def read_books():
    return books

@app.get("/books/{book_id}", summary="Поиск Книг по ID", tags=["Поиск Книг"])
def get_book(book_id:int):
    for book in books:
        if book["id"] == book_id:
            return book["title"]
    raise HTTPException(status_code=404, detail="Книга не найдено")

class NewBook(BaseModel):
    title: str
    author: str = Field()


@app.post("/books", summary="Добавление Книги в Список Книг", tags=['Добавление Книги'])
def create_book(new_book:NewBook):
    books.append({
        id: len(books) + 1,
        "title": new_book.title,
        "author": new_book.author
    })
    return {"Success": True}
  
if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)