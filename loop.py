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


'''
to read a word and print each character of the word in a new line
'''
a = input()
counter = 0
length_of_a = len(a)
while counter < (length_of_a):
    print(a[counter])
    counter = (counter + 1)


'''
write a program that reads a string and prints the first character of 
the given string on N lines, where N is the length of the given string
'''
S=input()
N=int(len(S))
count=0

while count<N:
    print(S[0])
    count=count+1


'''to read a string and print each character of the given string on a new line'''
S=input()
N=int(len(S))
count=0

while count<N:
    print(S[count])
    count=count+1


'''
'''
N=int(input())
count=1 

while count<=N:
    print((str(count))*count)
    count+=1
count=1 
while count<=N:
    print((str(count))*count)
    count+=1   

    
'''
to print

'''
N=int(input())
count=1 

while count<=N:
    row=(str(count)+" ")*count
    print(row)
    count+=1


'''
to print
'''
N=int(input())
count=1 

while count<N:
    print("* "*count)
    count+=1 
print("+ "*count) 


'''
to print cube of N inputs from 1
'''
N=int(input())
count=1 

while count<=N:
    print(count ** 3)
    count+=1


'''use for loop'''

'''
to print N inputs 
'''
N=int(input())
count=1 

for i in range(N):
    print(int(input()))
    count+=1 


'''
solid rectangle
'''
M=int(input())
N=int(input())
count=1 

for i in range(M):
    print("* "*N)
    count+=1       


'''
right angled triangle
'''
N=int(input())
count=1 

for i in range(N):
    print("* "*count)
    count+=1    


''' sum of numbers'''
N=int(input())
count=0
sum_numbers=0

for i in range(N):
    sum_numbers+=int(input())
    count+=1 
print(sum_numbers)    
        

'''to print numbers from M to N'''
M=int(input())
N=int(input())
numbers=M 

print(numbers)
for i in range(M,N):
    numbers+=1
    print(numbers)
            

'''sum of numbers from M to N'''
M=int(input())
N=int(input())
sum_numbers=0

for i in range(M,N+1):
    sum_numbers+=i
print(sum_numbers)                


'''write a program that reads a number N and prints a square of N rows and N columns using stars(*)'''
N=int(input())

for i in range(N):
        print("* "*N)


'''to read a number M and prints a Square of M rows and M columns using numbers'''
N=int(input())

for i in range(1,N+1):
    print(f"{i}"*N)
        

'''to read two numbers M and N, and print a rectangle of M rows and N columns using *'''
M=int(input())
N=int(input())

for i in range(M):
        print("*"*N)


'''to print right angled triangle'''
N=int(input())

for i in range(1,N+1):
    print("*"*i)  


'''to read a number and print all the digits of the given number separated by space'''
N=input()
n=int(len(N))
numbers=""

for i in range(n):
    numbers=numbers+N[i]+" "
print(numbers)  

'''print numbers in reverse'''
N=int(input())
 
for i in range(N):
    print(N-i)