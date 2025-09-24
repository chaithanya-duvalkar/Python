'''relational operators'''

'''to check whether given number is greater than 25 and the first digit is greater than second digit'''
A=input()
print(int(A) > 25)
print(A[0] > A[1])


'''read three digit number and to check whether the first digit of A is less than the last digit of B'''
A=input()
B=input()
print(A[0] < B[2])


'''to check second string is a first part of first string'''
A=input()
B=input()
print(A[:len(B)]==B)


'''checks if the percentage P of 500 is equal to the number N'''
P=float(input())
N=float(input())
percentage_value=(P/100)*500
print(percentage_value == N)



'''to check whether the area of the rectangle less than or equal to perimeter of the rectangle'''
A=int(input())
B=int(input())
area=A*B 
perimeter=2*(A+B)
print(area <= perimeter)


'''if first N characters of the string and the last N characters of the string are not same '''
A=input()
N=int(input())
print(A[:N] != A[-N:])