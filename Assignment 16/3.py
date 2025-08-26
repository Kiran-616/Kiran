# class shirt
class Shirt:
    def __init__(self,sid=0,sname="unknow",stype="formal",price=0,size="M"):
        

            self.sid=sid
            self.sname=sname
            self.stype=stype
            self.price=price
            self.size=size
        
    
    def showShirt(self):
        print(f"shirt ID: {self.sid},Name:{self.sname},Type:{self.stype},Price:{self.price},Size:{self.size}")

        #@staticmethod
    def ChangePriceBySize(base_price,size):
        if size.lower()== "small":
            return base_price
        elif size.lower()== "medium":
            return base_price+100
        elif size.lower()=="larger":
            return base_price + 200
        elif size.lower()=="xlarge":
            return base_price + 300
        else:
            return base_price
        
            
# ----test-----
s1 = Shirt(301,"Raymond","Formal",1000,"Large")
s1.showShirt()
print("Updated Price:", Shirt.ChangePriceBySize(s1.price,s1.size))

