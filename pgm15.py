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