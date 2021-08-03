import tkinter as t
from tkinter import scrolledtext as sct
from tkinter import messagebox, DoubleVar, ttk
import datetime as dt
import ListSplit_gui as ListSplit
import Borrow_details as BD

# these widgets and variables are declared global because they are
# used in multiple methods
global entry1, entry3
global entry2
global combo1
global scrollt
global btn
global btn1
global book_counter

book_counter = 0

entry1 = t.Entry()
entry2 = t.Entry()
entry3 = t.Entry()

btn = t.Button()
btn1 = t.Button()

combo1 = ttk.Combobox()
scrollt = sct.ScrolledText()

entry1_v = DoubleVar
entry2_v = DoubleVar
entry3_v = t.IntVar

# every global variable must be initialized before using
book_list = ListSplit.listSplit()


# r_window method generates the window used for book returning
def r_window():
    global entry1
    global entry2
    global entry3
    global combo1
    global scrollt
    global btn
    global btn1

    book_counter = 0

    window = t.Tk()
    window.geometry("530x450")
    window.title("Book Rental System")
    window.resizable(0, 1)

    l1 = t.Label(window, text="First Name", width=10).grid(row=0, pady=2, padx=4)

    entry1 = t.Entry(window, width=30, textvariable=entry1_v)
    entry1.grid(row=0, column=1)

    l2 = t.Label(window, text="Last Name", width=10).grid(row=1, pady=2, padx=4)

    entry2 = t.Entry(window, width=30, textvariable=entry2_v)
    entry2.grid(row=1, column=1)

    btn = t.Button(window, text="Validate", command=validate,
                   width=20)  # validate() will be invoked when this button is clicked
    btn.grid(row=2, columnspan=2, pady=5, padx=4)

    scrollt = sct.ScrolledText(window, width=60, height=10)
    scrollt.grid(row=4, rowspan=4, columnspan=3, padx=20, pady=2)

    l3 = t.Label(window, text="how many days was the book returned late").grid(row=8, pady=2, padx=4)

    entry3 = t.Entry(window, width=30, textvariable=entry3_v)
    entry3.grid(row=8, column=1)

    btn1 = t.Button(window, text="Return", command=book_return, state=t.DISABLED,
                    width=20)  # winodw will be destroyed when this button is clicked
    btn1.grid(row=9, columnspan=2, pady=2, padx=4)

    window.mainloop()


# validate method is used to validate the returner's name and create his file
def validate():
    global entry1
    global entry2
    global combo1
    global scrollt
    global btn, btn1

    # retriving text entered in entry
    firstName = str(entry1.get())
    lastName = str(entry2.get())

    a = "Details/Borrow-" + firstName + " " + lastName + ".txt"
    b = "Details/Return-" + firstName + " " + lastName + ".txt"

    # checking if the firstname and lastname contains only charachters and not numbers
    if firstName.isalpha() and lastName.isalpha():

        # checking if the user has borrowed any books or not

        try:
            # checking if borrowers file exists
            with open(a, "r") as f:
                lines = f.readlines()

            # opening borrowers file
            with open(a, "r") as f:
                scrollt.delete(1.0, float(2000))
                scrollt.update()
                data = f.read()
                scrollt.insert(t.INSERT, data)
                t.messagebox.showinfo(message="File Opened successfully")

                # checking if the borrower has returned the books or not

                try:
                    # checking if returner's file exists
                    with open(b, "r") as f:
                        lines = f.readlines()

                    # opening the return and borrow files of user
                    with open(b, "r") as f, open(a, "r") as f1:
                        scrollt.delete(1.0, float(2000))
                        scrollt.update()
                        data = f1.read()
                        scrollt.insert(t.INSERT, data)
                        scrollt.insert(t.INSERT, "\n-------------------------------------------------------\n")
                        data1 = f.read()
                        scrollt.insert(t.INSERT, data1)
                        t.messagebox.showinfo(message="The borrower has already returned the books")

                except:
                    t.messagebox.showwarning(message="The borrower has not returned the books")
                    # activating the return button as borrower has not returned the books
                    btn1['state'] = t.NORMAL
        except:
            # if borrower's file does not exists the name will be incorrect
            t.messagebox.showwarning(message="The borrower name is incorrect")

    else:
        t.messagebox.showwarning(message="please input only alphabets from A-Z")


def book_return():
    global entry1
    global entry2, entry3
    global combo1
    global scrollt
    global btn, btn1

    firstName = str(entry1.get())
    lastName = str(entry2.get())

    a = "Details/Borrow-" + firstName + " " + lastName + ".txt"
    b = "Details/Return-" + firstName + " " + lastName + ".txt"

    # reading users book borrow file
    with open(a, "r") as f1:
        data2 = f1.read()

    # creating users book return file
    with open(b, "w+")as f:
        # f.write("                Library Management System \n")
        # f.write("                   Returned By: " + firstName + " " + lastName + "\n")
        f.write("S.N.\t\tBookname\t\tCost\tDate\n")
    total = 0.0

    book_borrowed = BD.borrow_details(firstName, lastName)
    count = 0
    for i in book_borrowed:
        for j in range(ListSplit.count1):
            if i == ListSplit.bookname[j]:
                count += 1
                with open(b, "a") as f:
                    f.write(str(count) + "\t\t" + ListSplit.bookname[j] + "\t\tRs" + ListSplit.cost[j] + "\n")
                    # adding 1 to book quntity on return
                ListSplit.quantity[j] = int(ListSplit.quantity[j]) + 1
                total += float(ListSplit.cost[j])

    if len(entry3.get()) == 0:
        day = 0
    else:
        day = int(entry3.get())
    fine = 5 * day

    # appending the fine to the users book return file
    with open(b, "a")as f:
        f.write("\nDate: " + str(dt.datetime.now()) + "\nFine: Rs" + str(fine))
    total = total + fine

    t.messagebox.showinfo(title="Overflow", message="Total bill:" + str(total))

    # appending the total cost to the users book return file
    with open(b, "a")as f:
        f.write("\t\t\t\t\tTotal: Rs" + str(total))

    # rewriting stocks after return of book
    with open("Stock.txt", "w+") as f:
        for i in range(ListSplit.count1):
            f.write(ListSplit.bookname[i] + "," + ListSplit.authorname[i] + "," + str(ListSplit.quantity[i]) + ","
                    + "Rs" + ListSplit.cost[i] + "\n")

    # displaying the book return file of user in scrolledtext
    b = "Details/Return-" + firstName + " " + lastName + ".txt"
    with open(b, "r") as f:
        scrollt.delete(1.0, float(2000))
        scrollt.update()
        data = f.read()
        scrollt.insert(t.INSERT, data)

    # when user returns the books the return button will be disabled
    btn1['state'] = t.DISABLED
