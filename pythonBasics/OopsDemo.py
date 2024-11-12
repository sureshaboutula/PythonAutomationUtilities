
class Calculator:
    num = 100 # class variable

    #Default Constructor
    def __init__(self, a, b):
        self.firstNum = a # Instance variables
        self.secondNum = b
        print("I am called automatically when object is created")

    def getData(self):
        print("I am now executing as method in class")

    def Summation(self):
        #return self.firstNum + self.secondNum + self.num
        return self.firstNum + self.secondNum + Calculator.num


obj = Calculator(2, 3)
obj.getData()
print(obj.Summation())

obj = Calculator(4, 5)
obj.getData()
print(obj.Summation())

