# complex number class
class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def __del__(self):
        print(f"complex object{self.real}+{self.imag} i destroyed")

    def __add__(self,other):
        return Complex(self.real+ other.real,self.imag+other.imag)
    
    def display(self):
        print(f"{self.real} +{self.imag } i")

c1=Complex(2,3)
c2=Complex(4,5)
c3=c1+c2
c3.display()