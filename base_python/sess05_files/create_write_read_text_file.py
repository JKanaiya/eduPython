# Python script to demonstrate how to create, write, andread from a text file

# Import the required modules
import os


# create a file to create and write to a file
def create_file(path, content):
    """
    Creates a file with the given path and write the specified content to it.

    :param path: The path of the file to create.
    :param content: The content to write to the file.
    """
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"File created and contents writen successfully.")


# get and display the current working directory
current_dir = os.getcwd()
print(f"The current working directory is: {current_dir}")

# Get and display the path to the 'files' directory by going up one folder
files_dir = os.path.abspath(os.path.join(current_dir, "..", "files"))

print(f"The path to the 'files' directory is : {files_dir}")

# Specify and display the file path and name of the file to be created
file_path = os.path.join(files_dir, "hello.txt")
print(f"The full path to the file to be created is : {file_path}")

# Specify the text / content to be written to the file using a hard-coded / user input string
# content = input("Please enter the text you want to write to the file: ")
content = "Hello World 👋 from text files in python\n"

# Call / invoke the create_file() function to create and write to the text file
create_file(file_path, content)


# TODO: Write code to read the contents of the "hello.txt" file and display them