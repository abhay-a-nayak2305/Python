dict1={"Abhay":100, "Alice": 85, "Anuj": 60, "Amay": 87, "Jay": 78}
a=input("Enter the student's name: ")
if a in dict1:
    print(a+"'s marks: ",dict1[a])
else:
    print("Student not found.")