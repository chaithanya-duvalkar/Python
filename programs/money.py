
# '''

# '''



# A=int(input())

# hundreds=int(A/100)
# a=A-(100*hundreds)
# fiftys=int(a/50)
# b=a-(50*fiftys)
# tens=int(b/10)
# c=b-(10*tens)
# ones=int(c/1)

# print(f"100:{hundreds}")
# print(f"50:{fiftys}")
# print(f"10:{tens}")
# print(f"1:{ones}")

# '''

# '''

# A=int(input())

# five_hundreds=int(A/500)
# a=A-(500*five_hundreds)
# fiftys=int(a/50)
# b=a-(50*fiftys)
# tens=int(b/10)
# c=b-(10*tens)
# ones=int(c/1)

# print("500:",five_hundreds,"50:",fiftys,"10:",tens,"1:",ones)


# ''' 
# '''
# A=int(input())

# hundreds=int(A/100)
# a=A-(100*hundreds)
# fifty=int(a/50)
# b=A-(100*hundreds)-(50*fifty)
# twenty=int(b/20)
# c=A-(100*hundreds)-(50*fifty)-(20*twenty)
# ten=int(c/10)

# print("100 Notes:",hundreds)
# print("50 Notes:",fifty)
# print("20 Notes:",twenty)
# print("10 Notes:",ten)


# '''


# '''
# A=int(input())

# two_thousands=int(A/2000)
# a=A-(2000*two_thousands)
# five_hundred=int(a/500)
# b=A-(2000*two_thousands)-(500*five_hundred)
# two_hundred=int(b/200)
# c=A-(2000*two_thousands)-(500*five_hundred)-(200*two_hundred)
# fifty=int(c/50)
# d=A-(2000*two_thousands)-(500*five_hundred)-(200*two_hundred)-(50*fifty)
# twenty=int(d/20)
# e=A-(2000*two_thousands)-(500*five_hundred)-(200*two_hundred)-(50*fifty)-(20*twenty)
# five=int(e/5)
# f=A-(2000*two_thousands)-(500*five_hundred)-(200*two_hundred)-(50*fifty)-(20*twenty)-(5*five)
# two=int(f/2)
# g=A-(2000*two_thousands)-(500*five_hundred)-(200*two_hundred)-(50*fifty)-(20*twenty)-(5*five)-(2*two)
# one=int(g/1)

# print(f"2000:{two_thousands} 500:{five_hundred} 200:{two_hundred} 50:{fifty} 20:{twenty} 5:{five} 2:{two} 1:{one}")


# '''

# '''
# N=int(input())

# thousands=int(N/1000)
# a=N-(1000*thousands)
# five_hundreds=int(a/500)
# b=N-(1000*thousands)-(500*five_hundreds)
# hundreds=int(b/100)
# c=N-(1000*thousands)-(500*five_hundreds)-(100*hundreds)
# fifty=int(c/50)
# d=N-(1000*thousands)-(500*five_hundreds)-(100*hundreds)-(50*fifty)
# twenty=int(d/20)
# e=N-(1000*thousands)-(500*five_hundreds)-(100*hundreds)-(50*fifty)-(20*twenty)
# five=int(e/5)
# f=N-(1000*thousands)-(500*five_hundreds)-(100*hundreds)-(50*fifty)-(20*twenty)-(5*five)
# one=int(f/1)

# print(f"1000:{thousands}")
# print(f"500:{five_hundreds}")
# print(f"100:{hundreds}")
# print(f"50:{fifty}")
# print(f"20:{twenty}")
# print(f"5:{five}")
# print(f"1:{one}")

int=9
for i in range(int):
    int=(int*1)
print(int)

num=15
total=90

for i in range(1,num):
    if (i%4)==2:
        total=(total+i)
print(total)

starting_num=10
ending_num=20
total=0

for i in range(starting_num,ending_num):
    if(i%5)==0:
        total=total+i
print(total)

country="America"
print(country[4:])

result=10
for i in range(1,5):
    result=result-1
print(result)

num=2
total=80
for i in range(1,num):
    if(i%2)==0:
        total=(total-i)
print(total)

fact=5
for i in range(4):
    fact=(fact*i)
print(fact)

word="Home Work"
length=len(word)
for i in range(length):
    if word[i]==" ":
        print(word[:i])

sport="Volleyball"
new_word=""

for each_char in sport[:5]:
    new_word=(new_word+each_char)
print(new_word)