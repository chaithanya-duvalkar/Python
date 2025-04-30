'''to read 3-digit number N and check if N is armstrong number'''
N=input()
a=int(N[0])
b=int(N[1])
c=int(N[2])
Armstrong_number = (a**3)+(b**3)+(c**3)

if Armstrong_number == int(N):
    print("True")
else:
    print("False")



'''
Write a program that reads a four-digit number N and checks if N is an Armstrong Number.
'''

n=int(input())

if n==sum(int(d)**4 for d in str(n)):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
