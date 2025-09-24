'''hollow pyramid'''
N=int(input())

for i in range(1,N):
    print(" "*(N-i), end="")
    if i==1 or i==N:
        print("*"*(2*i-1))
    else:
        print("*", end="")
        print(" "*(2*i-3),end="")
        print("*")
print("* "*N)   

'''hollow pyramid 2'''
N=int(input())

for i in range(1,N+1):
    if i==1:
        print(f"{i}")
    else:
        num_spaces=(2*i)-3
        print(f"{i}{' '* num_spaces}{i} ")
for i in range(N-1,0,-1):
        if i==1:
            print(f"{i}")
        else:
            num_spaces=(2*i)-3
            print(f"{i}{' '* num_spaces}{i} ")


'''hollow right-angled triangle'''
N=int(input())

print("# "*N)

for i in range(1,N):
    print(""*i,end="")
    num_spaces=(N-i)*2-3
    
    if num_spaces>0:
        print("+"+" "*num_spaces+"+")
    else:
        print("+")

'''hollow diamond'''
N=int(input())

for i in range(1,N+1):
    print(" "*(N-i),end="")
    
    if i==1:
        print("*")
    else:
        print("*",end="")
        print(" "*(2*i-3),end="")
        print("*")

for i in range(N-1,0,-1):
    print(" "*(N-i),end="")
    
    if i==1:
        print("*")
    else:
        print("*",end="")
        print(" "*(2*i-3),end="")
        print("*")   

