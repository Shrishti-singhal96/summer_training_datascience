#oops
'''class account():
    pass
a1=account()
a2=account()
a3=account()
print(a1)
print(a2)
print(a3)'''



#QUES1
'''class student:
   def get_data(obj):
      obj.name=input("enter name= ")
      obj.roll_number=int(input("enter roll number= "))
      obj.marks1=int(input("enter marks of maths= "))
      obj.marks2=int(input("enter marks of english= "))
      obj.marks3=int(input("enter marks of science= "))

   def display_data(obj):
      print("name is ",obj.name)
      print("roll no ",obj.roll_number)
      print("marks in maths ",obj.marks1)
      print("marks in english ",obj.marks2)
      print("marks in science ",obj.marks3)
      
   def calculate_percentage(obj):
      percentage=((obj.marks1+obj.marks2+obj.marks3)/300)*100
      print("your percentage is ",percentage,"%")

s=student()
s.get_data()
s.display_data()
s.calculate_percentage()'''






#QUES2
'''class bank_account():
    def get_data(paise):
        paise.accname=input("enter account holder name= ")
        paise.accno=int(input("enter your account number= "))
        paise.bal=int(input("enter your balance= "))

    def deposit(paise):
        paise.deposit=int(input("enter the amount you want to deposit"))
        if paise.deposit>0:
            paise.bal= paise.bal+paise.deposit
            print("balance after deposit",paise.bal)
        else: print("deposit positive amount")
    
    def withdraw(paise):
        paise.w=int(input("enter the amount you want to withdraw: "))
        if paise.bal >=paise.w:
            paise.bal=paise.bal- paise.w
            print("balance after withdraw",paise.bal)
        else: print("insufficient balance")

    def display_balance(paise):
        print("your balance is",paise.bal)

ruppee=bank_account()
ruppee.get_data()
ruppee.deposit()
ruppee.withdraw()
ruppee.display_balance()'''



#QUES3
'''class employee():
    def getdata(e):
        e.id=int(input("enter employee id: "))
        e.name=input("enter employee name:")
        e.salary=int(input("enter basic salary: "))
          
    def HRA(e):
        e.hra=(20*e.salary)/100

    def DA(e):
        e.da=(10*e.salary)/100
    
    def gross_salary(e):
        e.gsal=e.salary+e.hra+e.da

    def display(e):
        print("employee name is ",e.name ,"with employee id ",e.id)
        print("basic salary is ",e.salary)
        print("allowances such as HRA AND DA are",e.hra,"and",e.da,"respectively")
        print("gross salary is ",e.gsal)

emp=employee()
emp.getdata()
emp.HRA()
emp.DA()
emp.gross_salary()
emp.display()


print("\n","\n")'''

#QUES4
'''class Rectangle:
    def getdata(r):
        r.l=int(input("enter length: "))
        r.b=int(input("enter breadth: "))

    def area(r):
        r.area=r.l*r.b
        print("area of rectangle is ",r.area)

    def perimeter(r):
        r.peri=2*(r.l+r.b)
        print("perimeter of rectangle is ",r.peri)

    def check_square(r):
        if r.l==r.b:
            print("rectangle is a square")
        else: print("length and breadth are different hence not a square")

rec=Rectangle()
rec.getdata()
rec.area()
rec.perimeter()
rec.check_square()
'''



#QUES5

'''class vehicle:
    def getdata(gddi):
        gddi.b=input("enter vehicle brand: ")
        gddi.m=input("enter vehicle model: ")

class car(vehicle):
    def fuel_type(gddi):
        gddi.f=input("enter fuel type of your car: ")

    def display(gddi):
        print("vehicle is a car")
        print("brand of car is ",gddi.b)
        print("model of car is ",gddi.m)
        print("fueltype of car is ",gddi.f)

class bike(vehicle):
    def engine_type(gddi):
        gddi.e=input("enter engine type of your bike: ")


    def display(gddi):
        print("vehicle is a bike")
        print("brand of bike is ",gddi.b)
        print("model of bike is ",gddi.m)
        print("engine type of bike is ",gddi.e)


c=car()
c.getdata()
c.fuel_type()
c.display()

b=bike()
b.getdata()
b.engine_type()
b.display()


print("\n")
'''

#QUES 6
'''class person:
    def getdata(p):
        p.name=input("enter name: ")
        p.age =int(input("enter age: "))
    
class teacher(person):
    def subject(p):
        p.sub=input("enter subject: ")

class principal(teacher):
    def school_name(p):
        p.schl = input("enter school name: ")

    def display(p):
        print("The details are as follows:")
        print("Name is",p.name)
        print("age is",p.age)
        print("he teaches",p.sub)
        print("School name is",p.schl)

p=principal()
p.getdata()
p.subject()
p.school_name()
p.display()

print("\n")'''

#QUES 7
'''class shape:
    def area(s):
        print("area of shape")

class circle(shape):
    def getdata(s):
        s.r=float(input("enter radius of circle: "))
    
    def area(s):
        s.a=3.14*s.r*s.r
        print("area of circle",s.a)

class rectangle(shape):
    def getdata(s):
        s.l=float(input("enter length of rectangle: "))
        s.b=float(input("enter breadth of rectangle: "))

    def area(s):
        s.a=s.l*s.b
        print("area of reatangle is",s.a)

class triangle(shape):
    def getdata(s):
        s.ba=float(input("enter base of triangle: "))
        s.h=float(input("enter height of triangle: "))

    def area(s):
        s.a=s.ba*s.h*0.5
        print("area of triangle is",s.a)

c=circle()
c.getdata()
c.area()

r=rectangle()
r.getdata()
r.area()

t=triangle()
t.getdata()
t.area()
'''

#QUES 8 you can use super.pay() in child classes to print (you want to pay ,amoount) while using c.pay()
'''class payment:
    def has(amount):
    amount.total_balance=100000
    amount.cpin=1234
    amount.upi_pin=6767
    amount.username="hero"
    amount.password=3333
    
    def getdata(amount):
        amount.p=int(input("enter payable amount"))
    
    def pay(amount):
        print("you want to pay",amount.p)

class creditcard(payment):
    def display(amount):
        print("CREDIT CARD")
    def pay(amount):
        #super.pay()
        amount.pin=int(input("enter credit card pin: "))
        if amount.pin==amount.cpin:
            amount.total_balance=amount.total_balance-amount.p
            print("remaining balance",amount.total_balance)
        else: print("wrong pin ")

class upi(payment):
    def display(amount):
        print("UPI")
    def pay(amount):
        amount.up=int(input("enter upi pin: "))
        if amount.up==amount.upi_pin:
            amount.total_balance=amount.total_balance-amount.p
            print("remaining balance",amount.total_balance)
        else: print("wrong pin ")


class netbanking(payment):
    def display(amount):
        print("NET BANKING")
    def pay(amount):
        amount.n=input("enter your username: ")
        amount.nb=int(input("enter netbanking password: "))
        if amount.nb==amount.password and amount.n==amount.username:
            amount.total_balance=amount.total_balance-amount.p
            print("remaining balance",amount.total_balance)
        else: print("wrong pass or username")
c=creditcard()
c.display()
c.getdata()
c.pay()

u=upi()
u.display()
u.getdata()
u.pay()


n=netbanking()
n.display()
n.getdata()
n.pay()'''

#QUES 9
'''class library:
    def issue_book(i):
        print("issue a book")

class studentlibrary(library):
    def display(i):
        print("STUDENT LIBRARY")

    def issue_book(i):
        i.book=input("enter the subjects of which you want to borrow book: ")#output is hindi,eng
        #i.b=list(i.book) [can't use this as it considers all subject entered as one string so i splits the characters to make list as h i n d i , e n g etc so use split (",")to split it with comma]
        i.b=i.book.split(",") #make a list as["hindi","eng"]
        print(i.b)
        if len(i.b)<3:
            print("you can issue wanted books")
        else: print("issue two books max at once")

class facultylibrary(library):
    def display(i):
        print("FACUTLY LIBRARY") 

    def issue_book(i):
        i.fbook=input("enter the subjects of which you want to issue books of: ")
        i.f=i.fbook.split(",")
        if len(i.f)>6:
            print("you can issue wanted books")
        else: print("you can issue atmost 5 books at once")

s=studentlibrary()
s.display()
s.issue_book()  

f=facultylibrary()
f.display()
f.issue_book()
'''




#QUES10 use double undersquare_ before name to declare private variable and method
'''class atm:
    
    __pin=1234
    __balance=50000   

    def verify_pin(p):
        print("verifying pin")
        p.pin=int(input("enter pin: "))
        if p.pin==p.__pin:
            print("pin verified")  
        else: print("pls enter correct pin")

    def deposit(p):
        print("depositing")
        p.deposit=int(input("enter the amount you want to deposit: "))
        p.pin=int(input("enter pin: "))
        if p.pin==p.__pin:
            if p.deposit>0:
                p.__balance=p.__balance+p.deposit
                print("balance after deposit is: ",p.__balance)
            else: print("not allowable ")
        else: print("wrong pin")

    def withdraw(p):
        print("withdrawing")
        p.withdraw=int(input("enter the amount you want to deposit: "))
        p.pin=int(input("enter pin: "))
        if p.pin==p.__pin:
           if p.__balance>=p.withdraw:
               p.__balance=p.__balance-p.withdraw
               print("balance after withdrawal is:",p.__balance)
           else: print("insufficient balance ")
        else: print("wrong pin")

    def change_pin(p):
        print("changing pin")
        p.newpin=int(input("enter new pin: "))
        if p.newpin==p.__pin:
            print("new pin cannot be same as old pin")
        else: print("new pin is successfully generated")

    def display_balance(p):
        print("displaying balance")
        print("existing balance is",p.__balance)
a=atm()
#a.__init() cannot access private method through obj

a.verify_pin()
a.deposit()
a.withdraw()
a.change_pin()
a.display_balance()'''




#QUES11 to declare abstract class import abc from ABC,abstractmethod and then write ABC in bracket of the class which u want to abstract and write @abstractmethod before method you want to abstract
# abstract classes are the ones whose objects cannot be created and abstract method don't have any implementationof its own contain 'pass' they are being used in child class by overriding
'''from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(s):
        pass
    @abstractmethod
    def display():
        pass
class FullTimeEmployee(Employee):
    def getdata(s):
        s.name=input("enter name of full time employee: ")
        s.sal=int(input("enter salary of full time employee: "))
    def calculate_salary(s):
        print("calculated salary of full time employee is:",s.sal)
    def display(s):
        print("name of full time employee is",s.name)
class PartTimeEmployee(Employee):
    def getdata(s):
        s.name=input("enter name of part time employee: ")
        s.sal=int(input("enter salary of part time employee: "))
    def calculate_salary(s):
        print("calculated salary of part time employee is:",s.sal)
    def display(s):
        print("name of full part employee is",s.name)
e=Employee()
e.calculate_salary()
f=FullTimeEmployee()
f.getdata()
f.display()
f.calculate_salary()

print("\n")
p=PartTimeEmployee()
p.getdata()
p.display()
p.calculate_salary() 
'''



#QUES12
from abc import ABC,abstractmethod
class Product(ABC):
    
    @abstractmethod
    def discount(self):
        pass

    @abstractmethod
    def display(self):
        pass

    def getdata(self):
        self.__productid=int(input("enter product id: "))
        self.__price=int(input("enter price"))


    def getprice(self):
        return self.__price
    
    def getid(self):
        return self.__productid
    

class electronics(Product):
    def discount(self):
        self.bill=self.getprice()-(self.getprice()*10/100)
    def display(self):
        print("ELECTRONICS")
        print("product id is",self.getid())
        print("original amount was",self.getprice())
        print("bill amount after 10% discount on electronics is",self.bill)

class clothing(Product):
    def discount(self):
        self.bill=self.getprice()-(self.getprice()*10/100)
    def display(self):
        print("CLOTHING")
        print("product id is",self.getid())
        print("original amount was",self.getprice())
        print("bill amount after 20% discount on clothing is",self.bill)

class grocery(Product):
    def discount(self):
        self.bill=self.getprice()-(self.getprice()*10/100)
    def display(self):
        print("GROCERY")
        print("product id is",self.getid())
        print("original amount was",self.getprice())
        print("bill amount after 5% discount on grocery is",self.bill)

print("BUYING ELECTRONICS")
e=electronics()
e.getdata()
e.discount()
e.display()

print("BUYING CLOTHING")
c=clothing()
c.getdata()
e.discount()
e.display()

print("BUYING GROCERY")
g=grocery()
g.getdata()
g.discount()
g.display()