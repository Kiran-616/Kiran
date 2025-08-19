# Product class
class Product:
    def __init__(self,pid=None,pname=None,price=None,quantity=None):
        self.pid = pid
        self.pname= pname
        self.price = price
        self.quantity = quantity
        print("product object created!")

    def showProduct(self):
        print("----product details----")
        print("product ID :",self.pid)
        print("product Name :", self.pname)
        print("price :",self.price)
        print("quantity :",self.quantity)

print("------------------------")
def __del__(self):
    print("product object destroyed")

p1 = Product()
p1.showProduct()

p2 = Product(201,"laptop" , 55000,10)
p2.showProduct()
