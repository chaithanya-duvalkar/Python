#wap to ask the user to enter names of their 3 fvt movies and store them in a list
#wap to check if a list contains a palindrome of elements(use copy() method)
#wap to count the number of students with the "A" grade in the following tuple
#store the above values in a list & sort them from "A" to "D"
#store following word meanings in a python dictionary:
        #table:"a piece of furniture","list of facts and figures"
        #cat:"a small animal"
dictionary={
    "table":["a piece of furniture","list of facts and figures"],
    "cat":"a small animal"
}
print(dictionary)

#You are given a list of subjects for students. Assume one classroom is reuired for 1 subject.
  #how many classrooms are needed by all students.
    #"python","java","c++","python","js","java","python","java","c++","c"
subjects={
    "python","java","c++","python","js","java","python","java","c++","c"
}
print(subjects)
print(len(subjects))

#wap to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dict and add one by one.
    #use sub name as key and marks as value
marks={}

x=int(input("enter phy: "))
marks.update({"phy":x})

x=int(input("enter chem: "))
marks.update({"chem":x})

x=int(input("enter maths: "))
marks.update({"maths":x})

print(marks)


#figure out a way to store 9 and 9.0 as separate values in the set.(take built-in data types)
values={"7.0",9,9.0,8,8.0,"9.0"}
print(values)

value={
    ("float",9.0),
    ("int",9)
}
print(value)

#create student class that takes name and marks of 3 subjects as arguments in constructor.
#then create a method to print the average

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    @staticmethod   #decorator
    def hello():
        print("hello")
        
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print("hi",self.name,"!:) Your avg score is: ",sum/3)
    
s1=student("chai",[99,98,97])
s1.get_avg()
        
s1.name="chukki"
s1.get_avg()
    
s1.hello()

#create account class with 2 attributes- balance and account no.
#create methods for debit, credit and printing the balance
class account:
    def __init__(self,bal,acc):
        self.balance=bal 
        self.account_no=acc 

    def debit(self,amount):
        self.balance-=amount  
        print("rs. ",amount,"was debited")
        print("total balance=",self.get_balance())

    def credit(self,amount):
        self.balance+=amount  
        print("rs. ",amount,"was credited")
        print("total balance=",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1=account(10000,12345)
acc1.debit(1000)
acc1.credit(5000)
acc1.debit(10)
acc1.credit(5000)