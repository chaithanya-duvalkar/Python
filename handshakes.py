'''
It was Raj's first day at school. His teacher Anu asked the students to meet every other student in the class and introduce themselves. 
The teacher asked them to do handshakes when they meet each other.
Write a program that reads an integer N and prints the number of handshakes made by the students.
'''
N=int(input())

handshakes=N*(N-1)//2

print(handshakes)