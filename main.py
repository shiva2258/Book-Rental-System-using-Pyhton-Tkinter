import tkinter as t
from tkinter import scrolledtext as sct

import Borrow_gui as Borrow
import Return_gui as Return
import Addbook_gui as addbook
import ListSplit_gui as ListSplit

global scrollt
global strbook

# accessing book details from Listsplit_gui.py in form of a List
book_list = ListSplit.listSplit()

strbook = ""


# when user adds new books,borrow books,return books then
# this function will update the scrolltext with the new information
def display_books():
    global scrollt, strbook

    # delete is used to remove old information from scrolltext in order to add updated information
    scrollt.delete(1.0, float(len(strbook)))
    scrollt.update()
    strbook = ""
    strbook += "\t------Books Available------\n"
    book_list = ListSplit.listSplit()
    for i in range(ListSplit.count1):
        strbook += "Book name:" + book_list[0][i] + "\n" + "\tAuthor:" + book_list[1][i] + "\n" + "\tQuantity:" + str(
            book_list[2][i]) + "\n" + "\tPrice:Rs" + str(book_list[3][i]) + "\n"

    # insert is used to display updated information stored in strbook
    scrollt.insert(t.INSERT, strbook)


def load_borrow():
    # calling b_window() method from Borrow_gui.py
    Borrow.b_window()


def load_return():
    # calling r_window() method from Return_gui.py
    Return.r_window()


window = t.Tk()
window.title("Book Rental system")
window.geometry("550x250")

# resizable prevents the user from maximizing or resizing the window size
window.resizable(0, 0)

#####################

# Gets the requested values of the height and width.
windowWidth = 600  # change this values to understand how it works
windowHeight = 400

# Gets both half the screen width/height and window width/height
positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)

# Positions the window in the center of the page.
window.geometry("+{}+{}".format(positionRight, positionDown))
window.geometry("550x250")

######################

l1 = t.Label(window, text="Menu", font=("Times New Roman", 20, "bold"))
l1.grid(row=0, columnspan=2, pady=10)

b1 = t.Button(window, text="Update list", width=15, command=display_books)
b1.grid(row=1, sticky="W", padx=4)

b2 = t.Button(window, text="Borrow Books", width=15, command=load_borrow)
b2.grid(row=2, sticky="W", padx=4, pady=4)

b3 = t.Button(window, text="Return Books", width=15, command=load_return)
b3.grid(row=3, sticky="W", padx=4, pady=4)

b4 = t.Button(window, text="Add books", width=15, command=addbook.addbook)
b4.grid(row=4, sticky="W", padx=4, pady=4)

scrollt = sct.ScrolledText(window, width=50, height=10)
scrollt.grid(row=1, column=1, rowspan=4, columnspan=1)

strbook += "\t------Books Available------\n"
for i in range(ListSplit.count1):
    strbook += "Book name:" + book_list[0][i] + "\n" + "\tAuthor:" + book_list[1][i] + "\n" + "\tQuantity:" + \
               book_list[2][i] + "\n" + "\tPrice:Rs" + book_list[3][i] + "\n"

scrollt.insert(t.INSERT, strbook)

window.mainloop()

