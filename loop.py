'''

'''
n=int(input())

counter=0
while counter<n:
    print("0")
    counter=counter+1


'''
first natural numbers
'''
n=int(input())
a=0
count=0

while count<n:
    a=a+1 
    print(a)
    count=count+1


'''reads a N and print the cube of N numbers from 1'''
N=int(input())
counter=1
while counter<=N:
    cube=(counter**3)
    print(cube)
    counter=counter+1 
    

'''
 Given two integers M and N, print a solid rectangle of M rows and N columns using *, with a space after each *. 
'''
M=int(input())
N=int(input())
for _ in range(M):
    print("* "*N)


'''
write a program that reads the N and prints the 10 numbers after N
'''    
N=int(input())

count=0 
next_numbers=N
while count<10:
    next_numbers=next_numbers+1
    print(next_numbers)
    count=count+1    
         