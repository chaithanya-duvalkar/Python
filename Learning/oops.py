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