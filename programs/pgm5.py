'''basic programs'''

'''sum of two numbers'''
A=input()
B=input()
print(int(A)+int(B))


'''division of two numbers'''
A=input()
B=input()
print(int(A)/int(B))


'''area of a triangle'''
length=input()
breadth=input()
area=int(length)*int(breadth)
print(int(area))


'''perimeter of rectangle'''
length=input()
breadth=input()
perimeter=2*(int(length)+int(breadth))
print(perimeter)


'''to print division of 2 numbers as an integer'''
A=input()
B=input()
div=int(A)/int(B)
print(int(div))


'''subtraction of two numbers'''
A=input()
B=input()
diff=float(A)-float(B)
print(diff)


'''percentage of boys'''
percent_girls=input()
percent_boys=100-int(percent_girls)
print(int(percent_boys))


'''to print the result in given format'''
A=input()
B=input()
add=float(A)+float(B)
print("Sum: "+str(add))


'''kilometers to meters'''
no_of_kilo=input()
in_meters=float(no_of_kilo)*1000
print(int(in_meters))


'''percentage'''
P=input()
value=(int(P)/100)*200
print(float(value))


'''to print remainder'''
dividend=input()
divisor=input()
quotient=int(dividend)/int(divisor)
remainder=int(dividend)-(int(divisor)*int(quotient))
print(remainder)