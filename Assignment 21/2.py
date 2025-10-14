# television class with exception handling

class Television:
    def __init__(self):
        self.model_no=0
        self.screen_size=0
        self.price=0
    def get_data(self):
        try:
            self.model_no=int(input("enter model number:"))
            self.screen_size=int(input("enter screen size(inches):"))
            self.price=float(input("enter price(rs):"))

            if self.model_no >9999:
                raise ValueError("model number must be 4 digits or less!")
            if self.screen_size <12 or self.screen_size >70:
                raise ValueError("screen size must be between 12 and 70 inches!")
            if self.price < 0 or self.price > 5000:
                raise ValueError("price must be between 0 and 5000 rs!")
        except Exception as e:
            print("error:")