# Python script to demonstrate strings and string functions

# Declare a string variable
string_var = "hello MHD from MHD"

# Display the string variable with the first letter in uppercase
print(f"'string_var' with the first letter capitalised: %s" % string_var.capitalize())
print(f"'string_var' with the first letter capitalised: {string_var.capitalize()}")

# Display the type of 'string_var'
print(f"The type of 'string_var' is: {type(string_var)}")

# Display the contents of 'string_var' in uppercase
print(f"The content of 'string_var' in uppercase is: {string_var.upper()}")

# Display the contents of 'string_var' in lowercase
print(f"The content of 'string_var' in lowercase is: {string_var.lower()}")

string_2_center = "Programming With Python"
# Center 'string_2_center' with a specified width and given fill character
print(string_2_center.center(50, "-"))

# Count & display the number of times a character appears in a string ('o' in 'string_var')
print(f"The letter 'o' appears {string_var.count('o')} times in {string_var}")

# Display the highest and lowest alphabetical character
print(f"The highest alphabetical character in 'string_var' is '{max(string_var)}'\nAnd the lowest is: '{min(string_var)}'")

# Replace the 'he' with 'HE' and 'MHD' with 'IDK'
new_str = string_var.replace("he", 'HE').replace('MHD', 'IDK')
# Display the replaced / modified string
print(f"The modified contents of 'string-var' are: {new_str}")

# Declare another string variable for more string operations
my_string = "  Hello, World 123   "

# Get and display the number of characters using len()
print(f"The number of characters in 'my_strin' is: {len(my_string)}")

# isalnum() - checks if all characters are alphanumeric (no spaces, symbols)
print(f"Is the string 'my_string' alphanumeric? : {my_string.isalnum()}")

# islower(0 - checks if all alphabets are in lowercase
print(f"Are all alphabets in 'my_string' in lowercase? : {my_string.islower()}")

# isupper(0 - checks if all alphabets are in uppercase
print(f"Are all alphabets in 'my_string' in uppercase? : {my_string.isupper()}")

# lstrip() - removes any leading whitespaces (from the left)
print(f"Remove the leading spaces from 'my_string': '{my_string.lstrip()}'")

# rstrip() - removes any trailing whitespaces (from the right)
print(f"Remove the trailing spaces from 'my_string': '{my_string.rstrip()}'")

# strip() - removes any leading and trailing whitespaces (from the right)
print(f"Remove the leading and trailing spaces from 'my_string': '{my_string.strip()}'")

# endsWith() - checks if the specified string ends with the specified substring
print(f"Does {my_string} end with '123'?: {my_string.strip().endswith('123')}")

# find() - locates the first occurance of the specified substring
print(f"The first occurence of the substring 'World' in {my_string}: {my_string.find('World')}")

# index() - fins the first occurence of the substring, raises error when not found
print(f"Index of World: {my_string.index('World')}")

# count() - counts the number of occarences of the specified substirng
print(f"Number of times 'or' appears in 'my_string': {my_string.count('or')}")

# rfind() - find the last occurence of the specified substring
print(f"The last occurence of 'or' in 'my_strin' is {my_string.rfind('or')}")

# rindex() - find the last occurence of the specified substring, raises an error when not found
print(f"The last occurence of 'l' in 'my_strin' is at index: {my_string.rindex('l')}")

# startsWith() - checks if the string starts with a specified substring
print(f"Does {my_string} starts with '  Hello'?: {my_string.startswith('  Hello')}")