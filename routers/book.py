from typing import List

from fastapi import HTTPException
from fastapi_restful.cbv import cbv
from pydantic import BaseModel, ConfigDict, Field

from sqlalchemy.orm import Session
from fastapi.params import Depends

import models
from database import get_db
from fastapi import APIRouter

from routers.base import BaseAPI

class BookBase(BaseModel):
    isbn: str
    title: str
    author: str
    publisher: str
    publishedYear: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    isAvailable: bool


router = APIRouter(prefix="/books", tags=["Book"])

@cbv(router)
class BookAPI(BaseAPI):
    db: Session = Depends(get_db)

    @router.get("/", response_model=List[Book], status_code=200)
    def GetAllBooks(self, q: str | None = None):
        if q is None:
            return self.db.query(models.DBBook).all()
        return self.db.query(models.DBBook).filter(models.DBBook.title.like(f"%{q}%")).all()

    @router.get("/{id}", response_model=Book, status_code=200)
    def GetBookById(self, id: int):
        return self.db.query(models.DBBook).filter(models.DBBook.id == id).first()

    @router.post("/", response_model=Book, status_code=201)
    def CreateBook(self, book: BookCreate):
        self.db.add(book)
        self.db.commit()
        self.db.refresh(book)
        return book

    @router.delete("/{id}", status_code=204)
    def DeleteBook(self, id: int):
        self.db.query(models.DBBook).filter(models.DBBook.id == id).delete()

            




