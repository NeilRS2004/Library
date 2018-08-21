import sys

class Library:
    def ___int___(self,listofbooks):
        self.availablebooks=listofbooks

    def displayAvailablebooks(self):
        print("THe books we have in our library are:")
        for book in self.availabebooks:
            print(book)
    def lendBook(self,requestedBook):
        if requestedBook in self.availablebooks:
            print("you have now borrowed it")
        else:
            print("Sorry, it's not in the library at this moment")

    
class Student:
    def requestBook(self):
        print("Enter the name of the book you would like to check out... dummy.")
        self.book=input()
        return self.book

    def returnBook(self):
        print("Enter the book you would like to return:")
        self.book=input()
        return self.book

def main():
    print("in main")
    library=Library["Donald Trump's Huge Hands","The Garden Behind the Sword","Pokemon Battle Legends"] 
    student=Student()
    done=False
    while done==False:
        print("""======LIBRARY MENU======
1. Display all available books
2. Request a book
3. Return a book
4. Exit
""")
        choice=int(input("Enter Choice:"))
        if choice==1:
            library.displayAvailablebooks()
        elif choice==2:
            library.lendBook(student.requestBook())
        elif choice==3:
            library.addBook(student.returnBook())
        elif choice==4:
            sys.exit


if __name__ == "__main__":
    main()

