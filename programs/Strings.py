# # # # string="--c--a--r--"
# # # # print(string[2::3])

# # # # count=1
# # # # word="Hello"
# # # # result=""
# # # # while count<4:
# # # #     result=result+word[count]
# # # #     count=count+1
# # # # print(result)  

# # # # n=4
# # # # count=1
# # # # while count<=n:
# # # #     print("+ "*n)
# # # #     count=count+1

# # # # a=4
# # # # while a>=2:
# # # #     a=a-1
# # # #     print(a) 

# # # # a="Hello"
# # # # count=0
# # # # len_a=len(a)
# # # # while count<(len_a-1):
# # # #     print(a[count])
# # # #     count=count+2  

# # # # word="Python"
# # # # count=2
# # # # while count<len(word)-1:
# # # #     count=count+1
# # # #     print(word[count])   

# # # # a=10
# # # # counter=0
# # # # while counter==3:
# # # #     a=a+1
# # # #     print(a)
# # # #     counter=counter+1
# # # # print("End")   

# # # # # i=1
# # # # # cond=(i!=3)

# # # # # while cond:
# # # # #     print(i)
# # # # #     i=i+1

# # # # # n=int(input())
# # # # # count=0
# # # # # while count<n:
# # # # #     number=int(input())
# # # # #     print(number)
# # # # #     count=count+1
# # # # # print("End")    

# # # # a=4
# # # # while a>2:
# # # #     a=a-1
# # # #     print(a**a)

# # # # a=6
# # # # i=0
# # # # count=0
# # # # while i<=a:
# # # #     if i%2==0:
# # # #         count=count+i 
# # # #     i=i+1
# # # # print(count)    


# # # # a=5
# # # # while a<=6:
# # # #     if a<6:
# # # #         print("Hai")
# # # #         a=a+1
# # # # print(a)

# # # # a=True
# # # # i=1
# # # # while a:
# # # #     if i>3:
# # # #         a=False 
# # # #     i=i+1
# # # # print(i)

# # # # a=10
# # # # count=0
# # # # while count<3:
# # # #     if a%2==0:
# # # #         a=a+2
# # # #     if a%3==0:
# # # #         a=a+3
# # # #     else:
# # # #         a=a+1
# # # #     count=count+1
# # # # print(a)    

# # # # a=1
# # # # count=1
# # # # while count<4:
# # # #     a=a+1
# # # #     print(a)
# # # # print("End")

# # # # a=4
# # # # counter=0

# # # # while counter<3:
# # # #     a=a+1
# # # #     print(a)
# # # #     counter=counter+1

# # # count=0
# # # while count<3:
# # #     if(count<2) and (count<6):
# # #         print('Work')
# # #     count=count+1
# # # print("Done!")

# # # a=0
# # # count=1
# # # while count<4:
# # #     a=a+1
# # #     print(a)
# # #     count=count+1
# # # print("End")

# # total=2
# # for i in range(1,8):
# #     total=total*1
# # print(total)

# # plant="Aloe Vera"
# # for digit in str(plant):
# #     print(digit)

# # fact =100
# # for i in range(4):
# #     fact=(fact*i)
# # print(fact)

# # fruit="Papaya"
# # for i in range(len(fruit)):
# #     print(i)

# start=3
# end=10
# total=0

# for i in range(start,end):
#     if (i%2)==0:
#         total=total+i 
# print(total)

# number=10
# total=100
# for i in range(1,number):
#     if (i%2) ==0:
#         total=(total-i)
# print(total)

# slogan="Save Earth, Save Lives"
# length_of_slogan=len(slogan)

# for i in range(length_of_slogan):
#     if slogan[i]==" ":
#         print(slogan[:i])

number=5
count=100

for i in range(1,number):
    count=(count-2)
print(count)

fact=5
for i in range(1,5):
    fact=(fact*i)
print(fact)

number=20
for i in range(number):
    number=(number-1)
print(number)

greeting="Hello World"
new_word=""

for each_char in greeting[:5]:
    new_word=(new_word+each_char)
print(new_word)

number=10
total=80
for i in range(1,number):
    if(i%3)==0:
        total=(total+i)
print(total)