
'''to check if each of the given numbers  is > 5'''
A=int(input())
B=int(input())
C=int(input())
print(A>5 and B>5 and C>5)


'''to check if each number is greater than or equal to 20'''
A=int(input())
B=int(input())
C=int(input())
print(A>=20 and B>=20 and C>=20)



'''to check given number is greater than 25 and first digit is greater than second'''
A=input()
print(int(A)>25 and A[0]>A[1])


'''to check whether the sum and product of two numbers are less than 3digit number'''
A=input()
B=input()
print(((int(A)+int(B))<100 and (int(A)*int(B))<100))


'''to check given number contains 0'''
A=input()
print(A[0]=='0' or A[1]=='0' or A[2]=='0')


'''to check whether the sum of any of two number is greater than 10'''
A=int(input())
B=int(input())
C=int(input())
print(100>(A+B)>10 or 100>(B+C)>10 or 100>(C+A)>10)


'''to check whether the all the digits are greater than 4 or first digit is 6 in a three-digit number'''
A=input()
print((A[0]>'4' or A[1]>'4' or A[2]>'4') or (A[0]=='6'))



'''to check whether the first two digit is 19 and next two digit is between 30 and 60 of a given 4 digit number'''
A=input()
B=A[:2]
C=A[2:]
print((int(B)==19) and (int(C)>30 and int(C)<60))


'''to check in a given three digit number it has 1 and it's sum is less than 12 and last digit is 5'''
A=input()
B=A[2]
C=int(A[0])+int(A[1])+int(A[2])
print("1" in A and int(C)<12 and int(B)==5 )


'''to check whether given 3 digit number has all the digit greater than 7 or sum of two digit less or equal to 30 '''
A=input()
a=int(A[0])
b=int(A[1])
c=int(A[2])
print((a>7 and b>7 and c>7) or (a*b<=30 and b*c<=30 and c*a<=30))



'''to check whether the given two conditions are satisfied'''
M=int(input())
P=int(input())
C=int(input())
print((M+P>=100 or P+C>=100 or M+C>=100) and (M+P+C>=180))

