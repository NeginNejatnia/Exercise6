from fractions import Fraction as frac
class cal:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
      return self.a+self.b
    def multiply(self):
      return self.a*self.b
    def divide(self):
      return self.a/self.b
    def subtract(self):
      return self.a-self.b     


a = frac(input("Enter first number: "))
b = frac(input("Enter second number: "))
my_instance = cal(a,b)
choice = 1

while choice!=0:
    print('1.add(+)')
    print('2.subtract(-)')
    print('3.multiply(*)')
    print('4.divide(/)')
    print()
    choice = int(input("Enter your choice: "))
    if  choice ==1:
        print('Result is : ',my_instance.add())
    elif choice ==2:
        print('Result is : ',my_instance.subtract())
    elif choice ==3:
        print('Result is : ',my_instance.multiply())
    elif choice ==4:
        print('Result is : ',my_instance.divide())
    else:
        print('Sorry, invalid your choice!')
    break   # if you want choice more, you can remove this line
    
print()
