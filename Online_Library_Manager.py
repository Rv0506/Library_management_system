

class Library:

    def __init__(self, list_of_books, lib_name):
        self.list_of_books = list_of_books
        self.lib_name = lib_name

    def display_Books(self, book):

        print(
            f"The book {book}  is with  {inst_a.list_of_books[book]}")

    def lend_Books(self, book, name):
        if(book in self.list_of_books):
            if (self.list_of_books[book] == ' '):
                print(f"Here is your book {book}. Happy Reading!!")
                self.list_of_books[book] = name
            else:
                print(
                    f"Sorry the book has already been lent by {self.list_of_books[book]}")
        else:
            print(
                "This Book is not available,please enter the name of Book from available list of Books")

    def add_Books():
        book = input(
            "Please enter the name of the book you want to donate:-\n")
        inst_a.list_of_books[book] = ' '
        print(f"Thank you for donating the book {book}")
        return inst_a.list_of_books

    def return_Book(self, book):
        if(book in self.list_of_books and self.list_of_books[book] != ' '):
            self.list_of_books[book] = ' '
            print(f"Thank you for returning the book {book}")
        else:
            print("This book has not been lent by anyone")
        return inst_a.list_of_books


inst_a = Library(
    {"Name of Book1": " ", "Name of Book2": " "}, "Fiction")


usr_name = input("Please enter your name:-\n")
print(f"Welcome to the Online Library {usr_name}\n")
def main():

    act = int(input("Please enter what you want to do,\nEnter 1 to display the books,Enter 2 to lend the books, Enter 3 to donate a book, Enter 4 to return the book and Enter 5 to exit:\n"))
    if(act == 1):
        for item in inst_a.list_of_books:
            inst_a.display_Books(item)
    elif(act == 2):
        inst_a.book = input(
            "Please enter the name of the book you want to lend:-\n")
        inst_a.name = input("Please enter your name:-\n")
        inst_a.lend_Books(inst_a.book, inst_a.name)
    elif(act == 3):
        Library.add_Books()
    elif(act == 4):
        book = input(
            "Please enter the name of the book you want to return:-\n")
        inst_a.return_Book(book)
    elif(act == 5):
        return 5
    else:
        print("Please enter a valid input")


if __name__ == '__main__':
    while True:
        a = main()
        if(a == 5):
            print("Thank you for using Online Library")
            break
