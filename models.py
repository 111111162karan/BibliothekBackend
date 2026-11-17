from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Float, Text
from sqlalchemy.orm import relationship

from database import Base


class DBBook(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    isbn = Column(String, unique=True)
    title = Column(String)
    author = Column(String)
    publisher = Column(String)
    publishedYear = Column(Integer)
    isAvailable = Column(Boolean)

class DBLoans(Base):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True)
    bookId = Column(Integer, ForeignKey('books.id'), nullable=False)
    userId = Column(Integer, ForeignKey('users.id'), nullable=False)
    borrowedAt = Column(DateTime)
    dueDate = Column(DateTime)
    returnedAt = Column(DateTime, nullable=True)
    status = Column(String)

    # Relationships
    book = relationship("DBBook", back_populates="loans")
    user = relationship("DBUser", back_populates="loans")


class DBUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password_hashed = Column(String)




