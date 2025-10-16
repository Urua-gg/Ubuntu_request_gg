# File Read & Write 
try:
    with open("MYSTORY.txt", "r") as infile:
        content = infile.read()

    modified_content = content.upper()

    with open("NEWSTORY.txt", "w") as outfile:
        outfile.write(modified_content)

    print("MYSTORY.txt has been read and NEWSTORY.txt has been created successfully!")

except FileNotFoundError:
    print("Error: MYSTORY.txt file was not found.")
except PermissionError:
    print("Error: You do not have permission to read or write the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Error Handling 
filename = input("Enter the filename to open (e.g., blacklivesmatter.txt): ")

try:
    with open(filename, "r") as file:
        print("File opened successfully! Here is its content:")
        print(file.read())

except FileNotFoundError:
    print("Error: The file you entered does not exist.")
except PermissionError:
    print("Error: Permission denied while trying to read the file.")
except Exception as e:
    print(f"Unexpected error: {e}")
