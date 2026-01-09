# Python script that handles an exception raised when the user tries to open a non-existent file
from sess05_files.create_write_read_text_file import content

try: # Write the code that may raise an exception(s) here
    file = open("non-existent.bin", "r")
    content = file.read()
    print(f"File conents are :{content}")
except FileNotFoundError: # Handle the file error here
    print("Error: File was not found!")
finally: # Resource clean up
    if 'file' in locals():
        file.close()
    else:
        print("Finally block executed")