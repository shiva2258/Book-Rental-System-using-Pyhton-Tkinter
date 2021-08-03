import tkinter as t
from tkinter import scrolledtext as sct
from tkinter import messagebox, DoubleVar, ttk
import datetime as dt
import ListSplit_gui as ListSplit

# these widgets and variables are declared global because they are
# used in multiple methods
global entry1
global entry2
global combo1
global scrollt
global btn
global btn1
global book_counter

window = t.Tk()

window.title("Welcome")
label = t.Label(window, text="Welcome to Book Rentals!")
label.grid(row=0, sticky="w" and "s", padx=40, pady=30)

# placing this window to center as per main window
windowWidth = 250  # change this values to understand how it works
windowHeight = 250
positionRight = int(window.winfo_screenwidth() / 2 - windowWidth / 2)
positionDown = int(window.winfo_screenheight() / 2 - windowHeight / 2)

# positionDown,positionRight are the posotion co-ordinates of window
window.geometry("+{}+{}".format(positionRight, positionDown))

# 150x100 is size of window
window.geometry("220x100")
window.withdraw()
window.deiconify()

# every global variable must be initialized before using
book_counter = 0

entry1 = t.Entry()
entry2 = t.Entry()

btn = t.Button()
btn1 = t.Button()

combo1 = ttk.Combobox()
scrollt = sct.ScrolledText()

entry1_v = DoubleVar
entry2_v = DoubleVar

# accessing book details from Listsplit_gui.py in form of a List
book_list = ListSplit.listSplit()


# b_window method generates the window used for book borrowing
def b_window():
    global entry1
    global entry2
    global combo1
    global scrollt
    global btn
    global btn1, book_counter

    book_counter = 0

    window = t.Tk()
    window.geometry("350x450")
    window.title("Book Rental System")
    window.resizable(0, 1)

    l1 = t.Label(window, text="First Name", width=10).grid(row=0, pady=2, padx=4)

    entry1 = t.Entry(window, width=30, textvariable=entry1_v)
    entry1.grid(row=0, column=1)

    l2 = t.Label(window, text="Last Name", width=10).grid(row=1, pady=2, padx=4)

    entry2 = t.Entry(window, width=30, textvariable=entry2_v)
    entry2.grid(row=1, column=1)

    btn = t.Button(window, text="Validate", command=validate, width=20)
    btn.grid(row=2, columnspan=2, pady=2, padx=4)

    combo1 = ttk.Combobox(window, values=ListSplit.bookname, state="readonly" and t.DISABLED, width=30)
    combo1.grid(row=3, columnspan=3, padx=4, pady=2)
    combo1.current(0)
    # bind() is used to set method invokation when user selects any book from combobox
    combo1.bind("<<ComboboxSelected>>", onBookSelect)

    scrollt = sct.ScrolledText(window, width=35, height=10)
    scrollt.grid(row=4, rowspan=4, columnspan=3, padx=20, pady=2)

    btn1 = t.Button(window, text="close", command=window.destroy, width=20)
    btn1.grid(row=8, columnspan=2, pady=2, padx=4)

    window.mainloop()


# validate method is used to validate the borrower name and create his file
def validate():
    global entry1
    global entry2
    global combo1
    global scrollt
    global btn

    # retriving text entered in entry
    firstName = str(entry1.get())
    lastName = str(entry2.get())

    # checking if the firstname and lastname contains only charachters and not numbers
    if firstName.isalpha() and lastName.isalpha():

        # btn is disabled in order to prevent user from creating multiple files at the same-time
        btn['state'] = t.DISABLED
        combo1['state'] = t.NORMAL

        t.messagebox.showinfo(message="Name Verified successfully")

        # Creating a file of borrower name in order to save the borrowed bookk details
        filename = "Details/Borrow-" + firstName + " " + lastName + ".txt"
        with open(filename, "a+") as f:
            # f.write("               Library Management System  \n")
            # f.write("                   Borrowed By: " + firstName + " " + lastName + "\n")
            f.write("S.N. \t\t Bookname \t\t      Authorname \t\t Date\n")

    else:
        t.messagebox.showwarning(message="Please input only alphabets from A-Z")


# bookselect will be invoked when user will select a book from combobox
def onBookSelect(event):
    global entry1
    global entry2
    global combo1
    global scrollt, book_counter

    firstName = str(entry1.get())
    lastName = str(entry2.get())

    filename = "Details/Borrow-" + firstName + " " + lastName + ".txt"
    # book_counter<=3 condition is defined to
    # prevent user from borrowing more that 4 books
    # User will not be able to borrow more than 4 books.
    if book_counter <= 3:
        try:
            a = combo1.current()
            try:
                # ListSplit.quantity[a])>0 condition checks if book is available or not
                if (int(ListSplit.quantity[a]) > 0):
                    t.messagebox.showinfo(message="book borrowed")
                    book_counter += 1

                    # Displaying borrowed book in scrolledtext
                    scrollt.insert(t.INSERT,
                                   str(book_counter) + "." + ListSplit.bookname[a] + "-" + ListSplit.authorname[
                                       a] + "\n")

                    # writing borrowed book details to borrowers file
                    with open(filename, "a") as f:
                        f.write(str(book_counter) + ". \t\t" + ListSplit.bookname[a] + "\t\t  " + ListSplit.authorname[
                            a] + "\t\t" + str(dt.datetime.now()) + "\n")

                    # substracting 1 book from quantity after borrowing
                    ListSplit.quantity[a] = int(ListSplit.quantity[a]) - 1

                    # rewritting the stocks file with new book quantity
                    with open("Stock.txt", "w+") as f:
                        for i in range(ListSplit.count1):
                            f.write(ListSplit.bookname[i] + "," + ListSplit.authorname[i] + "," + str(
                                ListSplit.quantity[i]) + "," + "Rs" + ListSplit.cost[i] + "\n")
                else:
                    t.messagebox.showwarning(message="book not available")
            except IndexError:
                t.messagebox.showerror(message="error occured while selecting books")
        except ValueError:
            t.messagebox.showwarning(message="Invalid book selected")
    else:
        t.messagebox.showerror(title="Overflow", message="Can not borrow more than 4 books")


