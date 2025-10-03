try:
    with open("sample.txt", "r") as file1:
        print("Reading file content: ")
        line=file1.read()
        print(line)

except FileNotFoundError:
    print("The file 'sample.txt' was not found.")