# Book-Rental-System-using-Pyhton-Tkinter
A file system should be developed to store the details of all Books. The details must include the Book name, Author, Quantity and unit price. The record of all books must be displayed when required. An admin must be able to add a new book and the necessary details. Admin must be able to view all the records in the file. When a book is borrowed/returned, the stock of books available should be updated.

Tools:
1. IDE: PyCharm
2. Language: Python

Software Requirements:
•	Operating System type: Windows 10, 64-bit version 1903
•	PyCharm 2021.1.3
•	Python 3.8

Hardware Requirements:
•	Processor: Intel core i5-3470 clocked @3.20Ghz
•	RAM: minimum 4GB, 8GB recommended
•	Processor: Intel® CoreTM i5-6500 CPU @ 3.20GHz pr greater

Functional Requirements:
•	Whenever an admin adds a item, a new record should be inserted into the file containing the details of the books.
•	New record should be inserted and the details are entered.
•	Admin should be able to view the details of the new book record inserted.
•	In the display, the book details like book name, author name, quantity, price are displayed.
•	The system must respond to user requests for the operations supported by the system.

List of Modules:
1.	Add Books - This module implements adding new book to the rental system
2.	Borrow Books - This module implements structure for borrowing the book for user. It takes care of valid usernames.
3.	Return Books - This module provides user with the facility of returning the book. Important feature of this module is that it finds the total bill for the overdue along with original rent.
4.	Update List - This module supports the admin with updating the stock upon a borrow/return transaction.
