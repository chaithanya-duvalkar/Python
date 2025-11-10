class car:
    color="yellow"
    brand="tata"

car1=car()
print(car1.color)
print(car1.brand)
 
class student:

    #default constructor
    def __init__(self):
        pass

    @staticmethod   #decorator
    def hello():
        print("hellooo chaiii!")
    #parameter constructor
    def __init__(self,fname):
        self.name=fname
        print("adding new student into DB")

s1=student("chai")
print(s1.name)

s2=student("chukki")
print(s2.name)

s1.hello()


class car:
    def _init_(self):
        self.acc=False
        self.brk=False
        self.clutch=False 
    
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started..")

car1=car()
car1.start()


class student:
    def __init__(self,name):
        self.name=name
s1=student("chaii")
print(s1.name)
# del s1.name    
# print(s1.name)


###public 
class account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.acc_pass=acc_pass

acc1=account("1234","abcde")
print(acc1.acc_no)
print(acc1.acc_pass)


###private
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass

    def reset_pass(self):
        print(self.__acc_pass)

acc1=Account("1234","abcde")
print(acc1.acc_no)
print(acc1.reset_pass())
# print(acc1.__acc_pass)


class car:
    @staticmethod
    def start():
        print("car started..")
    @staticmethod
    def stop():
        print("car stopped..")

class toyotacar(car):
    def __init__(self,name):
        self.name=name 

car1=toyotacar("nexon")
car2=toyotacar("punch")

print(car1.name)
print(car1.start())
print(car2.stop())