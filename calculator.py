class Calculator:
    def __init__(self):
        self.first_number=''
        self.second_number=''
        while True:
            try:
                if type(self.first_number)!=type(1):
                    self.first_number=int(input('ENTER FIRST NUMBER :'))
                if type(self.second_number)!= type(1):
                    self.second_number=int(input('ENTER SECOND NUMBER :'))
            except ValueError:
                print("PLEASE INPUT NUMERIC VALUES ONLY")
            else:
                break
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def subtract(a,b):
        return a-b
    @staticmethod
    def multiply(a,b):
        return a*b
    @staticmethod
    def divide(a,b):
        return a/b
    @staticmethod
    def modulo(a,b):
        return a%b
    @staticmethod
    def pow(a,b):
        return a**b
    def calculate(self):
        print("PLEASE CHOOSE AN OPTION")
        print("1) ADD(+)","2) SUBTRACT(-)","3) MULTIPLY(x)","4) DIVIDE(/)","5) MODULO(%)","6) POW(**)",sep="\n")
        choice=''
        try:
            choice=int(input("ENTER YOUR CHOICE :"))
            while choice not in [1,2,3,4,5,6]:
                print("PLEASE CHOOSE FROM THE GIVEN OPTIONS. TRY AGAIN!")
                choice=int(input("ENTER YOUR CHOICE :"))
        except ValueError:
            print("PLEASE INPUT NUMERIC VALUES ONLY")
        if choice==1:
             print("SUM is",Calculator.add(self.first_number,self.second_number))
        elif choice==2:
            print("DIFFERENCE is",Calculator.subtract(self.first_number, self.second_number))
        elif choice==3:
            print("MULTIPLICATION is",Calculator.multiply(self.first_number, self.second_number))
        elif choice==4:
            print("DIVISION is",Calculator.divide(self.first_number, self.second_number))
        elif choice==5:
            print("MODULO is",Calculator.modulo(self.first_number, self.second_number))
        else:
            print("POW is",Calculator.pow(self.first_number, self.second_number))
obj=Calculator()
obj.calculate()

