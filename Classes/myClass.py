
class MyClass(object):
    def __init__(self,name,date,shares,price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price
    
    def calc(self):
        return self.shares * self.price