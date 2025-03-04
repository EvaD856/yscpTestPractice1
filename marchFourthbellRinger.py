#did in python repository and copied and pasted into this repository so easy to find

# Sets empty dictionary
myDict = {}

#Asks for name and a grade 10 times
for names in range(5):
    name = input("Enter a student name: ")
    grade = int(input("Enter the student's grade: "))
    myDict [name] = grade

#prints out names and grades
for name, grade in myDict.items(): 
    print(f"{name}: {grade}")