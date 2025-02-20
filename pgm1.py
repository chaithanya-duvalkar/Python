'''python is easy to learn
as it is simple to learn,syntax is easy
and it has minimal code i.e.,the no. of code lines are less
'''

'''
print("hello world!")
print("2+5")
print(2+5)
print(5*5.0)
print(4-3)
print(21/20)
'''

'''string concatenation'''
username="chai"
age="20"
print(username + " is "+ age + " years "+"old" )


'''
this wrong as only string can be concatenated not mixture of string and int
a="*"+20
print(a)
'''

#string repetition
a="*"*10
print(a)

s="python"
s=("*"*3) + s + ("*"*3)
print(s)

#length of the string
username=input()
age=input()
length=len(username)
print(username+ " is " +age+ " years old")
print(username[0])
#print(username[4])-->error
'''or
first_letter=username[0]
print(first_letter)
'''