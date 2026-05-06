# Python script to demonstrate the map() function

# List of fibonacci numbers
numbers = sorted(set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]))

# Get and display the triple of each fibonacci numbers in the above set
tripled_num = sorted(set(map(lambda x: x * 3, numbers)))
print(f"Set of fibonacci numbers: {numbers}")
print(f"Set pf Fibonacci numbers raised to power 3: {tripled_num}")

# List of names and ages
names = ["Abigail", "Bernice", "Charlene" ,"Denise"]
age =[21, 24, 22, 19]

# Use the map funciton to combine the names and the mark
combined_data = map(lambda name, age: name + " is " + str(age), names, age)

# Convert the combined map object to a list then display the result

name_age_result = list(combined_data)
for i in name_age_result:
    print(i)