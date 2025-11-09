#wap to ask the user to enter names of their 3 fvt movies and store them in a list
#wap to check if a list contains a palindrome of elements(use copy() method)
#wap to count the number of students with the "A" grade in the following tuple
#store the above values in a list & sort them from "A" to "D"
#store following word meanings in a python dictionary:
        #table:"a piece of furniture","list of facts and figures"
        #cat:"a small animal"
dictionary={
    "table":["a piece of furniture","list of facts and figures"],
    "cat":"a small animal"
}
print(dictionary)

#You are given a list of subjects for students. Assume one classroom is reuired for 1 subject.
  #how many classrooms are needed by all students.
    #"python","java","c++","python","js","java","python","java","c++","c"
subjects={
    "python","java","c++","python","js","java","python","java","c++","c"
}
print(subjects)
print(len(subjects))

#wap to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dict and add one by one.
    #use sub name as key and marks as value
marks={}

x=int(input("enter phy: "))
marks.update({"phy":x})

x=int(input("enter chem: "))
marks.update({"chem":x})

x=int(input("enter maths: "))
marks.update({"maths":x})

print(marks)


#figure out a way to store 9 and 9.0 as separate values in the set.(take built-in data types)
values={"7.0",9,9.0,8,8.0,"9.0"}
print(values)

value={
    ("float",9.0),
    ("int",9)
}
print(value)