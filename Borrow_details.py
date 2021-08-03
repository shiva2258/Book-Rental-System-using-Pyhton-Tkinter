# borrow_details is used to get the book names borrowed by the user
def borrow_details(firstname, lastname):
    a = "Details/Borrow-" + firstname + " " + lastname + ".txt"

    with open(a, "r") as f:
        lines = f.readlines()

        # removing '\n' from left and right
        lines = [x.strip('\n') for x in lines]

        # removing extra spaces from left and right
        lines = [x.strip() for x in lines]

        # removing unneccessary lines from the list
        #lines.remove("Library Management System")
        #lines.remove("Borrowed By: " + firstname + " " + lastname)
        lines.remove("S.N. \t\t Bookname \t\t      Authorname \t\t Date")

        l1 = list()
        # splitting the list as per '\t' and then the third element will be book name
        for i in range(0, len(lines)):
            str_book = " "
            a = lines[i].split("\t")
            l1.append(a[2])

    return l1

