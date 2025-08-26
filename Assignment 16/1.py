# class book
class Book:
    # static variable for count
    count=0
    def __init__(self,bid=None,bname=None,price=0,author=None):
        if bid is not None and bname is not None and price !=0 and author is not None:


            self.bid=bid
            self.bname=bname
            self.price=price
            self.author=author
        
        else:
            self.bid=0
            self.bname="Unknown"
            self.price=0
            self.author="Unknown"

        Book.count +=1 # increase count when object created
    
    def showBook(self):
        print(f"Book ID: {self.bid},Name:{self.bname},price:{self.price},Author:{self.author}")

    def __del__(self):
        Book.count -=1  # decrease count when object deleted
        print("Book object destroyed!")

b1 = Book(101,"Python Basics",500,"Aditi")
b2 = Book()
b1.showBook()
b2.showBook()

print("Total Objects:",Book.count)

             

            