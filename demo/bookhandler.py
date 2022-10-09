
from validationModule import askForNoneEmptyString, askForInt
import time

from jsonfileHandler import  saveOneBook, loadallBooks, deleteBookfromJson, saveAllBooks
def ask_for_book_info():
    title = askForNoneEmptyString("please enter book title: ")
    author_name = askForNoneEmptyString("Please enter author name: ")
    no_of_pages = askForInt("Please enter number of pages : ")
    return title, author_name, no_of_pages

def generateID():
    id = round(time.time())
    return id

def createNewBook():
    print("----------- creating new book ------")
    book_details = ask_for_book_info()
    id = generateID()
    print(book_details)
    bookdata = {
        "id":id,
        'title': book_details[0],
        'description': book_details[1],
        'no_of_pages': book_details[2]
    }
    saveOneBook(bookdata)


def listallbooks():
    print("=======================All books =================================")
    books = loadallBooks()
    print(type(books))
    print(books)
    return books


def deleteBook():
    listallbooks()
    book_id = askForInt("please enter the id of the book you want to delete ")
    deleted = deleteBookfromJson(int(book_id))
    if deleted:
        print("book deleted successfully")

def displayUpdateMenu(updated_book):
    for k in updated_book:
        if k != 'id':
            choice = input(f"""please enter n for adding another value for {k} 
    else old value will be kept """)
            if choice == 'n':
                if k == 'no_of_pages':
                    updated_book[k] = askForInt(f"please enter {k}:")
                else:
                    updated_book[k] = askForNoneEmptyString(f"please enter {k}:")

    return updated_book


def editbook():
    books=listallbooks()
    book_id = askForInt("please enter the id of the book you want to edit ")
    selected_book = list(filter(lambda  book:book["id"]==int(book_id), books))
    updated_book = selected_book[0]
    updated_book = displayUpdateMenu(updated_book)
    print(updated_book)
    ####
    for index, book in enumerate(books) :
        if book["id"]==int(book_id):
            books[index] = updated_book
            break

    updated= saveAllBooks(books)
    print("---- book updated successfully ----")


