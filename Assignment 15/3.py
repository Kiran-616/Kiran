# Shirt class
class Shirt:
    def __init__(self,sid=None,sname=None,stype=None,price=None,size=None):
         self.sid = sid
         self.sname = sname
         self.stype= stype
         self.price = price
         self.size = size
         print("shirt object created!")

    def showShirt(self):
         print("----shirt details-----")
         print("shirt Id :",self.sid)
         print("shirt name :",self.sname)
         print("type :", self.stype)
         print("price :",self.price)
         print("size :",self.size)
         print("------------------------")

    def __del__(self):
         print("shirt object destroyed!")

s1 = Shirt()
s1.showShirt()

s2 = Shirt(301,"peter England","Formal", 1200,"Large")
s2.showShirt()