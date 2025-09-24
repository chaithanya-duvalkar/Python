# # '''python is easy to learn
# # as it is simple to learn,syntax is easy
# # and it has minimal code i.e.,the no. of code lines are less
# # '''

# # '''
# # print("hello world!")
# # print("2+5")
# # print(2+5)
# # print(5*5.0)
# # print(4-3)
# # print(21/20)
# # '''

# # '''string concatenation'''
# # username="chai"
# # age="20"
# # print(username + " is "+ age + " years "+"old" )


# # '''
# # this wrong as only string can be concatenated not mixture of string and int
# # a="*"+20
# # print(a)
# # '''

# # #string repetition
# # a="*"*10
# # print(a)

# # s="python"
# # s=("*"*3) + s + ("*"*3)
# # print(s)

# # #length of the string
# # username=input()
# # age=input()
# # length=len(username)
# # print(username+ " is " +age+ " years old")
# # print(username[0])
# # #print(username[4])-->error
# # '''or
# # first_letter=username[0]
# # print(first_letter)
# # '''

# # bird="Pigeon"
# # result=""
# # length=len(bird)

# # for i in range(length):
# #     result=result+bird[length-i]
# # print(result)

# for i in "Hardwork":
#     print(i)

# word="Invest"
# result=""

# for i in range(len(word)):
#     result=result+(word[i]*i)
# print(result)

# sentence="Do Hardwork"
# total=""

# for i in sentence:
#     if i!=" ":
#         total=total+i 
# print(total)

# var1=1
# var2=4
# for i in range(var1,var2):
#     print(i)


# start_num=2
# end_num=5

# for i in range(start_num,end_num):
#     print(i*i)

# string="abcd"
# for i in range(len(string)-1):
#     print(i)

# number=input()
# sum_of_numbers=0

# for i in number:
#     sum_of_numbers=sum_of_numbers+int(i)
# print(sum_of_numbers)

# greeting="Hello"
# for i in range(len(greeting)):
#     if greeting[i]=="l":
#         print(greeting[:i])

# num1=10
# num2=30
# total=10

# for i in range(num1,num2):
#     print("i=" +str(i))
#     if(i%3)==0:
#         total=(total-1)
#     else:
#         total=(total+3)
#     print(total)

country="India"
result=""
for i in range(len(country)):
    if(i==len(country)-1):
        result=result+country[i]
    else:
        result=result+country[i]+" "
print(result)

book="Wings of Fire"
for i in range(len(book)):
    if book[i]=="e":
        print(book[:i])

furniture="Chair"
result=""
for i in range(len(furniture)):
    result=result+(furniture[i]*i)
print(result)

sport="Tennis"
length=len(sport)
count=0
for i in range(1,length+1):
    count=count*i
print(count)

word="Paper"
result=""
length=len(word)
for i in range(length):
    result=result+word[length-i]
print(result)