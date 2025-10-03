with open("output.txt","w") as file1:
    a=input("Enter text to write to the file: ")
    writing=file1.write(a)
    print("Data successfully written to output.txt.\n")

with open("output.txt","a") as file2:
    a=input("Enter additional text to append: ")
    appending=file2.write("\n"+a)
    print("Data successfully appended.\n")

with open("output.txt","r") as file3:
    print("Final content of output.txt: ")
    reading=file3.read()
    print(reading)
