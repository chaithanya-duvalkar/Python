'''to print PASS if marks is more than 50 else FAIL '''
marks=int(input())

if marks>50:
    print("PASS")
else:
    print("FAIL")


'''prints the greatest among two numbers'''
a=int(input())
b=int(input())

if a>b:
    print(a)
else:
    print(b)    


'''eligibility for election'''
age=int(input())

if age<18:
    print("Not Eligible")
else:
    print("Eligible")


'''to print relationship between X nad Y'''
X=int(input())
Y=int(input())

if X<Y:
    print("X < Y")
else:
    print("X >= Y")


'''to check two numbers are equal'''
a=int(input())
b=int(input())

if a==b:
    print("Equal")
else:
    print("Not Equal")


'''to check square or rectangle'''
L=int(input())
B=int(input())

if L==B:
    print("Square")
else:
    print("Rectangle")



'''to check whether given temperature is suitable or not to go for a walk'''
temp=int(input())

if temp>15 and temp<40:
    print("Can go for a walk")
else:
    print("Cannot go for a walk") 


'''buying of book no buy if book size is regular small'''
S=input()
C=int(input())

if S=="large" or C>=300:
    print("Buy a Book")
else:
    print("Do Not Buy a Book")



'''to check both A & B are <= 1000 or B is > 500'''
A=int(input())
B=int(input())

if (A<=1000 and B<=1000) or (B>500):
    print("Pair")
else:
    print("Not a Pair")



'''reads the scores A and B of two players'''
A=int(input())
B=int(input())

if (A>300 or B>300) and (A+B<500):
    print("Can team up")
else:
    print("Cannot team up")
    


'''to check given number is positive or zero'''
A=int(input())

if A==0:
    print("Zero")
else:
    print("Positive")


'''to check if the given number is 0,+,-''' 
A=int(input())

if A<0:
    print("Negative")
elif A>0:
    print("Positive")
else:
    print("Zero")


'''to read a number and convert it into a positive number'''
A=int(input())

if A<0:
    A=A*(-1)
    print(A)
else:    
    print(A)    
           