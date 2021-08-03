import tkinter as tk
import ListSplit_gui as ListSplit
from tkinter import DoubleVar
from tkinter import scrolledtext as sct

global entry1, entry2, entry3, entry3, entry4
global scrollt

entry1 = tk.Entry()
entry2 = tk.Entry()
entry3 = tk.Entry()
entry4 = tk.Entry()
scrollt = sct.ScrolledText()

entry1_v = DoubleVar
entry2_v = DoubleVar
entry3_v = DoubleVar
entry4_v = DoubleVar

book_list = ListSplit.listSplit()


def addbook():
    global entry1, entry2, entry3, entry3, entry4, scrollt
    window = tk.Tk()
    window.geometry("450x500")
    window.title("Add New Books")
    window.resizable(0, 0)
    ListSplit.listSplit()

    i = ListSplit.count1
    label1 = tk.Label(window, text="Books Available:\t" + str(i))
    label1.grid(row=0, padx=4, sticky="W", pady=4, columnspan=2)
    label2 = tk.Label(window, text="Total cost of Books:\tRs." + str(ListSplit.totalcost))
    label2.grid(row=1, padx=4, sticky="W", pady=4, columnspan=2)

    label3 = tk.Label(window, text="Enter Book-name:")
    label3.grid(row=2, padx=4, sticky="W", pady=4)
    entry1 = tk.Entry(window, width=40, textvariable=entry1_v)
    entry1.grid(row=2, column=1, padx=4)

    label4 = tk.Label(window, text="Enter author-name:")
    label4.grid(row=3, padx=4, sticky="W", pady=4)
    entry2 = tk.Entry(window, width=40, textvariable=entry2_v)
    entry2.grid(row=3, column=1, padx=4)

    label5 = tk.Label(window, text="Enter quantity of books:")
    label5.grid(row=4, padx=4, sticky="W", pady=4)
    entry3 = tk.Entry(window, width=40, textvariable=entry3_v)
    entry3.grid(row=4, column=1, padx=4)

    label6 = tk.Label(window, text="Enter price of 1 unit:")
    label6.grid(row=5, padx=4, sticky="W", pady=4)
    entry4 = tk.Entry(window, width=40, textvariable=entry4_v)
    entry4.grid(row=5, column=1, padx=4)

    button1 = tk.Button(window, text="Add Stock", command=click, width=40)
    button1.grid(row=6, columnspan=2, pady=20)

    scrollt = sct.ScrolledText(window, height=10, width=52)
    scrollt.grid(row=7, columnspan=2, padx=8)
    strbook = ""
    strbook += "\t----Books Available----\n"
    book_list = ListSplit.listSplit()

    # displaying available books in scrolledtext
    for i in range(ListSplit.count1):
        strbook += "Book name:" + book_list[0][i] + "\n" + "\tAuthor:" + book_list[1][i] + "\n" + "\tQuantity:" + \
                   book_list[2][i] + "\n" + "\tPrice:Rs" + book_list[3][i] + "\n"
    scrollt.insert(tk.INSERT, strbook)

    window.mainloop()


# click method checks if user has entered proper information
def click():
    global entry1, entry2, entry3, entry3, entry4, scrollt

    bookname = str(entry1.get())
    authorname = str(entry2.get())
    quantity = str(entry3.get())
    cost = str(entry4.get())

    if bookname == "" or authorname == "" or quantity == "" or cost == "":
        tk.messagebox.showwarning(title="Warning", message="Please fill all the information!")
    elif quantity.isalpha() == True or cost.isalpha() == True:
        print(bookname.isalpha(), authorname.isalpha(), quantity.isalpha(), cost.isalpha())
        tk.messagebox.showwarning(title="Warning", message="filled information is incorrect!")
    else:
        try:
            with open("Stock.txt", "a+") as f:
                f.write(bookname + "," + authorname + "," + quantity + "," + "Rs" + cost + "\n")
                tk.messagebox.showinfo(title="Info", message="Book added to stocks")
            strbook = ""
            strbook += "\t----Books Available----\n"
            book_list = ListSplit.listSplit()
            scrollt.delete(1.0, float(10000))
            scrollt.update()
            for i in range(ListSplit.count1):
                strbook += "Book name:" + book_list[0][i] + "\n" + "\tAuthor:" + book_list[1][
                    i] + "\n" + "\tQuantity:" + str(book_list[2][i]) + "\n" + "\tPrice:Rs" + str(book_list[3][i]) + "\n"
            scrollt.insert(tk.INSERT, strbook)
        except:
            tk.messagebox.showerror(title="Error", message="Enable to add book to stocks")

        # try:
        #     with open("StockHash.txt", "a+") as f:
        #         temp = str
        #         i = 0
        #         hashpos = (abs(hash(bookname)) % 25) * 60
        #         # print(hashpos)
        #         f.seek(0)
        #         while i < hashpos:
        #             i += 60
        #             f.read(temp, 60, "\n")
        #             if f.fail():
        #                 f.seek(i)
        #             else:
        #                 f.write("\n")
        #                 f.seek(i)
        #             if i == hashpos:
        #                 break
        #
        #         if i == hashpos:
        #             while 1:
        #                 f.seek(i, 0)
        #                 f.read(temp, 60, "\n")
        #                 if f.fail():
        #                     f.write(bookname + "|" + authorname + "|" + quantity + "|" + cost + "\n")
        #                     break
        #                 else:
        #                     f.seek(60, 1)

        try:
            with open("StockHash.txt", "a+") as f:
                hashpos = (abs(hash(bookname)) % 25) * 60
                # print(hashpos)
                f.seek(hashpos, 0)
                tk.messagebox.showinfo(title="info",message="Hash Position is: "+str(hashpos))
                f.write(bookname + "|" + authorname + "|" + quantity + "|" + cost + "\n")
        except:
            tk.messagebox.showerror(title="Error", message="Unable to add book to stockhash")

        # print("Hash Position is: " + hashpos)


