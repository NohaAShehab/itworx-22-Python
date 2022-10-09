from bookhandler import  createNewBook, listallbooks, deleteBook, editbook
def mainmenu():
    choice = input("""
please enter n for new,
l for listing all, 
d for delete, 
e for edit, 
x for exit:  """)

    if choice == "x":
        exit()
    elif choice == 'n':
        createNewBook()
    elif choice == 'l':
        listallbooks()
    elif choice == 'd':
        deleteBook()
    elif choice =='e':
        editbook()

    return mainmenu()


mainmenu()