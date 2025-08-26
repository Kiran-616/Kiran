# class product
class Product:
    # static member discount
    discount = 0.1 # 10% default discount

    def __init__(self,pid=None,pname=None,price=0,quantity=0):
        if pid is not None and pname is not None:

            self.pid=pid
            self.pname=pname
            self.price=price
            self.quantity=quantity

        else:
            self.pid=0
            self.pname="Unknown"
            self.price=0
            self.quantity=0

    def showProduct(self):
        print(f"product ID: {self.pid},Name:{self.pname},price:{self.price},Quantity:{self.quantity}")
    
    def applyDiscount(self):
        discounted_price = self.price - (self.price * Product.discount)
        return discounted_price
    
    def __del__(self):
        print("Product object destroyed!")

        # ------ test ------
p1 = Product(201,"Mobile",15000,2)
p1.showProduct()
print("Discounted Price:",p1.applyDiscount())
    