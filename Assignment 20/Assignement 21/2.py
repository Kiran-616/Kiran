# television class with exception handling

class Television:
    def __init__(self):
        self.model_no=0
        self.screen_size=0
        self.price=0

    def get_data(self):
        try:
            self.model_no=int(input("enter model number:"))
            self.screen_size=int(input("enter screen size (inches):"))
            self.price=float(input("enter price (rs):"))


            if self.model_no < 1000 or self.model_no > 9999:
                raise ValueError("invalid model number ! must be 4 digits.")
            if self.screen_size < 12 or self.screen_size > 70:
                raise ValueError("invalid screen size! must be between 12 and 70.")
            if self.price<0 or self.price >5000:
                raise ValueError("invalid price! must be between 0 and 5000")
        except Exception as e:
            print("error:",e)
            print("resetting all values to 0 ...")


            self.model_no =0
            self.screen_size=0
            self.price=0
    def display_data(self):
        print("\n----Television details ----")
        print(f"model number : {self.model_no}")
        print(f"screen size : {self.screen_size} inches")
        print(f"price : rs.{self.price}")

if __name__ == "__main__":
    tv = Television()
    tv.display_data()
        
        