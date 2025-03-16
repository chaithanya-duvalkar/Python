'''basic programs'''

'''to print the half part of the string'''
a=input()
string=len(a)//2
print(a[:string])


'''to print the last three characters of the word N times in a single line'''
W=input()
N=int(input())
last_three=W[-3:]
print(last_three*N)


'''to repeat the same string N times separated by space'''
W=input()
N=int(input())
print((W+" ")*N)


'''to print the first two and the last two letters of the word and prints the star(*) instead of the remaining letters'''
W=input()
first_two=W[:2]
a=len(first_two)
last_two=W[-2:]
b=len(last_two)
word=len(W)-a-b
print(first_two+"*"*word+last_two)


'''to print the owrd excluding the fourth letter of the word'''
W=input()
print(W[:3]+W[4:])


'''to print the given word without the character at the given index'''
W=input()
I=int(input())
word=W[:I]+W[I+1:]
print(word)


'''to print a simple square using the hashes(#)'''
print("#"*3)
print("#"*3)
print("#"*3)


'''to print a simple triangle using the plus(+)'''
print("+")
print("+"*2)
print("+"*3)


'''to print three lines with each line containing N stars (*)'''
N=int(input())
print("* "*N)
print("* "*N)
print("* "*N)
