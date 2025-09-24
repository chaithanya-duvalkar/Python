'''to check N is >5'''
N=int(input())

if N>10:
    result=N+5
    print(result)
else:
    result=N+1
    print(result)



'''to check sum of 3 angles of the triangle is == 180'''
A=int(input())
B=int(input())
C=int(input())

if A+B+C == 180:
    print("*")
    print("**")
    print("***")
else:
    print("Not a Valid Triangle")


'''to check all 3 numbers are greater than 100'''
A=int(input())
B=int(input())
C=int(input())

if (A>100 and B>100 and C>100):
    print("All are greater than 100")
else:
    print("Not all are greater than 100")



'''to check if the number in the given room number is less than 30->room number format R1,R35 etc'''
N=input()
RN=int(N[1:])
if RN<30:
    print("Ground Floor")
else:
    print("Not Ground Floor")


'''to check difference between the three numbers'''
A=int(input())
B=int(input())
C=int(input())

if (A-B<25 and B-C<25 and C-A<25):
    print("Difference is less than 25")
else:
    print("Difference is not less than 25")


'''to check if the sum of any two sides of the triangle is always greater than the third side'''
A=int(input())
B=int(input())
C=int(input())

if (A+B>C and B+C>A and C+A>B):
    print("It's a Triangle")
else:
    print("It's not a Triangle")


'''to check the given string is valid or not'''
S=input()

if (len(S)<7 and len(S)>2) or (S[0]!="a"):
    print("Valid String")
else:
    print("Not a Valid String")



'''to check any of the two numbers are btwn 40 and 140'''
A=int(input())
B=int(input())

if (40<A<140) or (40<B<140):
    print("Between 40 and 140: Yes")
else:
    print("Between 40 and 140: No")


'''to check below any of two conditions are true'''
A=int(input())
B=int(input())

if (A<20 or B<20) or (30<A+B<50):
    sum=A+B
    print(sum)
else:
    print(A)
    print(B)       


'''to check below conditions are satisfied'''
A=int(input())
B=int(input())

if (A==6 or B==6) or (A+B==6) or (B-A==6 or A-B==6):
    print("Lucky")
else:
    print("Not Lucky")


'''greatest of three numbers'''
A=int(input())
B=int(input())
C=int(input())

if (A>B):
    largest=A 
else:    
    largest=B   
    
if (largest<C):
    largest=C 
    
print(largest)    


'''A company decided to give a bonus of 5% to an employee if his/her years of service is more than five years.
Write a program that reads an employee's salary and years of service and decides whether the employee gets the bonus or not.'''

salary=int(input())
year=int(input())

if year<5:
    print("No Bonus")
else:
    bonus=salary*0.05
    print(bonus)    

'''the given angles of triangle is valid or not'''
A=int(input())
B=int(input())
C=int(input())

if (A+B+C== 180):
    print("It's a Triangle")
else:
    print("It's not a Triangle")        


