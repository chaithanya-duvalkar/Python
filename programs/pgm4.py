'''basic programs'''

'''reads a word and prints length of a word'''
data=input()
print(len(data))


'''reads a word and prints stars(*) equals to the length of a word'''
data=input()
print("*"*len(data))

'''L-1'''
data=input()
print(len(data)-1)


'''reads a word and prints the index of the last character of the word'''
data=input()
last_index=len(data)-1
print(last_index)


'''to print the last character of a given word'''
data=input()
last_char=data[-1]
print(last_char)


'''print the length of the word excluding the first and last character'''
a=input()
b=len(a)-2
print(b)


'''to print the first letter of the given word and star(*) instead of the other letters'''
a=input()
print(a[0]+"*"*(len(a)-1))


'''to print half of the length of the word'''
a=input()
print(len(a)/2)