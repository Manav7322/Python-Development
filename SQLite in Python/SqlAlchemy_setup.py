from sqlalchemy import create_engine , Column, Integer, String, func
from sqlalchemy.orm import declarative_base, sessionmaker

base = declarative_base()

engine= create_engine("sqlite:///books.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

class Book(base):
    __tablename__="books"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer,nullable=True)

base.metadata.create_all(engine)

# new_book = Book(title= "Python 101", author= "Guido", year=2023)
# session.add(new_book)
# session.commit()

books = session.query(Book).all()
for book in books:
    print(book.id, book.title, book.author, book.year)

books1 = session.query(Book).filter(func.length(Book.title)<12).all()
for book in books1:
    print(book.title,book.year)

# Update
book_update = session.query(Book).filter_by(id = 2).first()
book_update.title = "Light"
session.commit()

print(book_update.title,book_update.year)

book_delete = session.query(Book).filter_by(id=2).first()
session.delete(book_delete)
session.commit()

for book in books:
    print(book.id, book.title, book.author, book.year)