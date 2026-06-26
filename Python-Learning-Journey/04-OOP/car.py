
class car:
    def __init__(self, model, year, color, for_sale):
        self.module = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def drive(self):
        print(f"You Drive the {self.color} {self.module}")

    def stop(self):
        print(f"You Stop the {self.color} {self.module}")

    def describe(self):
        print(f"{self.year} {self.color} {self.module}")
