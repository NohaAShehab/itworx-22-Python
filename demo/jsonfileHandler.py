import  json

def loadallBooks():
    try:
        with open("books.json", "r") as bookfile:
            books = json.load(bookfile)
            return books  # list
    except Exception as e :
        return None


def saveAllBooks(books):
    try:
        with open("books.json", "w") as bookfile:
            json.dump(books, bookfile)
            return True
    except Exception as e :
        return None

def saveOneBook(bookData):
    books = loadallBooks()
    if not books:
        books = []
    books.append(bookData)

    added=saveAllBooks(books)
    return added




def deleteBookfromJson(book_id):
    books = loadallBooks()
    books_after_delete = list(filter(lambda book:book['id']!= book_id, books))
    if len(books) == len(books_after_delete):
        print("=== book not found ==== ")
        return  False

    else:
        deleted=saveAllBooks(books_after_delete)
        return  deleted