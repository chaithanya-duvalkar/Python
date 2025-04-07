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