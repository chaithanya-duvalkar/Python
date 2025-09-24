

'''to check whether second number is greater than first number by one'''
A=int(input())
B=int(input())
print(A+1 == B)



'''to check whether the first letter and the last letter of the word are not same'''
A=input()
n=len(A)-1
print(A[0] != A[n])


'''to check whether N a two digit number..such that the two digit sum is greater than 7'''
N=input()
print(int(N[0])+int(N[1]) > 7)


'''to check password is valid or not. A string is considered as valid password if the number of characters is greater than 7'''
A=input()
n=len(A)
print(n>7)


'''to check if B starts at index I in A python code'''
A=input()
B=input()
index=int(input())
print(A[index:index+len(B)] == B)



'''to check the first three characters of the given string are same'''
A=input()
B=input()
print(A[:3] == B[:3])