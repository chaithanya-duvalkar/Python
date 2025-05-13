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


'''
to read two numbers M and N and print N numbers after M
'''
M=int(input())
N=int(input())
count=0
next_numbers=M
while count<N:
    next_numbers=next_numbers+1
    print(next_numbers)
    count=count+1   


'''
to read two numbers M and N and inputs the sum of N numbers from M
'''
M=int(input())
N=int(input())
count=1
sum_numbers=M
next_numbers=M
while count<N:
    next_numbers=next_numbers+1
    sum_numbers=sum_numbers+next_numbers
    count=count+1
print(sum_numbers)    



'''
to print the right-angled triangular pattern of N lines using an * character
'''
N=int(input())
count=1

while count<=N:
    print("* "*count)
    count=count+1


'''
to read N numbers as input and prints the product of the given N numbers
'''    
N=int(input())
count=0
num=1 

while count<N:
    num=int(input())*num
    count+=1 
print(num)    
    

'''same for sum
'''
N=int(input())
count=0
sum_numbers=0

while count<N:
    sum_numbers+=int(input())
    count+=1 
print(sum_numbers)    
         