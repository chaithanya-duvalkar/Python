'''Basic programs'''

'''to print the sum of the digits of a given 3-digit number'''
A=input()
print(int(A[0])+int(A[1])+int(A[2]))


'''to print the character present at the index N in the word W'''
W=input()
N=input()
N=int(N)
print(W[N])


'''to print the given word, N number of times in a single line'''
A=input()
N=input()
print(str(A)*int(N))


'''to print first 3 characters'''
A=input()
print(A[:3])


'''to print part of a word from the given index to the end of the word'''
A=input()
N=input()
print(A[int(N):])


'''to print a part of the word from the index X to the index Y'''
A=input()
n1=input()
n2=input()
print(A[int(n1):int(n2)+1])


'''to print the first N characters of the word'''
A=input()
N=input()
print(A[:int(N)])


'''to print last N characters of the word'''
word=input()
no_of_characters=input()
no_of_characters=int(no_of_characters)
word_length=len(word)
start_index=word_length-no_of_characters
part=word[start_index:]
print(part)


'''to print the second part of the string that has digits'''
A=input()
start_index=2
number=A[start_index:]
number=int(number)
print(number)


'''to print the first part of the string that has numbers'''
string=input()
no_of_characters=len(string)
end_index=no_of_characters-1
number=string[:end_index]
number=int(number)
print(number)
