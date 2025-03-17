


'''to print three lines with each line containing N pluses(+)'''
N=int(input())
print("+ "*N)
print("+ "*N)
print("+ "*N)


'''basic arithmetic'''
A=input()
B=input()
add=(int(A)+int(B))
sub=(int(A)-int(B))
mul=(int(A)*int(B))
print(add)
print(sub)
print(mul)


'''to print Y such that N as input which divides into two parts X and Y
X is 30 percent of N
Y is the remaining percentage of N'''
N=float(input())
X=(30/100)*N 
Y=(N)-(X)
print(Y)



'''area and perimeter of the square'''
a=int(input())
perimeter=4*a
area=a*a
print(f"Area of the square is: {area}")
print(f"Perimeter of the square is: {perimeter}")



'''W1 & W2. W1 contains two parts. the ffirst part contains W2 and the second part contains
the remaining letters in W1. print W1 with the first part as stars(*)'''
W1=input()
W2=input()
print("*"*len(W2)+W1[len(W2):])


'''to print string A by excluding the first two and last two characters of the string'''
A=input()
first_two=A[:2]
last_two=A[-2:]
print(A[2:-2])