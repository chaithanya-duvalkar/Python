'''to print the remainder'''
A=int(input())
B=int(input())

result=A % B 

if result:
    print(result)
else:
    print(0)


'''divisibility by 7'''
A=int(input())

if (A%7 == 0):
    print("Divisible by Seven")
else:
    print("Not Divisible by Seven")   


'''greatest remainder when divided by 4 & 5'''
N=int(input())

is_R1 = (N % 4)
is_R2 = (N % 5)

if is_R1 > is_R2:
    print(is_R1)
elif is_R1 < is_R2:
    print(is_R2)
else:
    print(is_R1)

'''to check divisibility of 11'''
N=int(input())

if (N % 11 == 0 or N % 11 == 1):
    print("Special Eleven")
else:
    print("Normal Number")         


'''divisibility of 9'''
N=input()

is_divisible=(int(N) % 9 == 0)
is_equal=(N[0] == '9' or N[1] == '9')

if is_divisible or is_equal:
    print("Lucky Number")
else:
    print("Unlucky Number")


'''to check if all the given condituons are satisfied'''
S=input()
s=S[:3]
i=int(S[3:])

if (s == 'NXT' and (i % 2 == 0 or i % 7 ==0)):
    print("Special String")
else:
    print("Not a Special String")  


'''check all the conditions are satisfied'''
A=int(input())
B=int(input())

is_three = (A % 3 == 0 and B % 3 == 0)
is_twelve = (A % 12 == 0 or B % 12 == 0)

if is_three and is_twelve:
    print("Pair")
else:
    print("Not a Pair")


'''to print if the given number is divisible by any of the lucky numbers 6,3,2 in decreasing order'''
N=int(input())

is_six=(N%6 ==0)
is_three=(N%3==0)
is_two=(N%2==0)

if is_six:
    print("Number is divisible by 6")
elif is_three:
    print("Number is divisible by 3")
elif is_two:
    print("Number is divisible by 2")
else:
    print("Number is not divisible by 2, 3 or 6")


'''to read two digit number and check if any of the conditions are satisfied'''
N=input()

a=int(N[0])
b=int(N[1])
s=a+b
n=int(N)

if s==7 or a==7 or b==7 or n%7==0:
    print("Special Number")
else:
    print("Normal Number")


'''reads a distance D in km and calculate the score'''
D=int(input())

if D<=10:
    print(D)
else:
    D=10+(D-10)*3
    print(D)


'''to check the last digit of N is == to the last digit of square of N''' 
D=int(input())

if D<=10:
    print(D)
else:
    D=10+(D-10)*3
    print(D)    


'''to read a number N and check if triple of N is divisible by 6'''
N=int(input())

triple=N*3

if triple % 6 == 0:
    print(triple)
else:
    print(N)               
             