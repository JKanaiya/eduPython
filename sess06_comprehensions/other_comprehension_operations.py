# Python script to demonstrate working with comprehensions

# List f fibonacci numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]

# Get and display the squares of the above Fibonacci numbers using a list comprehension
fib_squares = [num ** 2 for num in numbers]
print(f"Original numbers: {numbers}")
print(f"Squares: ")

even_fib_squares = [num ** 3 for num in numbers if num % 2 == 0]
print(f"Even Cubed fib numbers: {even_fib_squares}")

# Dictionary of students and their mean scores in an exam
student_scores = {
    "Sue": 56, "Jim": 72, "Mark": 61, "Micha": 72, "Wiliam": 78, "Jane": 51, "Xi": 56, "Abigail": 92
}

# Display the student's and their scores
print(f"Students and their exam scores: {student_scores}")

# Get and display a dictionary of the students that passed (passmark: 55)
passed_students = {name: score for name, score in student_scores.items() if score > 55}
print(f"Students that passed and their exam scores: {passed_students}")

# TODO: Get and display the dictionary of students that failed
failed_students = {name: score for name, score in student_scores.items() if score < 55}
print(f"Students that failed and their exam scores: {failed_students}")

# Extract and display the set of student names form the student_scores dictionary

names_with4_or_more = {name for name in student_scores.keys() if len(name) > 4}
print(f"Student names with 4 or more letters:\n{names_with4_or_more}")

# Comprehensions with string functions
paragraph = """
Click Insert and then choose the elements you want from the different galleries.
Themes and styles also help keep your document coordinated. When you click Design
and choose a new Theme, the pictures, charts, and SmartArt graphics change to match
your new theme. When you apply styles, your headings change to match the new theme.
Save time in Word with new buttons that show up where you need them. To change the
way a picture fits in your document, click it and a button for layout options appears
next to it. When you work on a table, click where you want to add a row or a column,
and then click the plus sign. Reading is easier, too, in the new Reading view. You
can collapse parts of the document and focus on the text you want. If you need to stop
sreading before you reach the end, Word remembers where you left off – even on another device.
"""

# Remove all the manual line breaks (\n or newline characters) and replace them with a space (" ")
cleaned_paragraph = paragraph.replace("\n", " ")

sentences = cleaned_paragraph.split(" ")

# Display each sentence on a new line
for sentence in sentences:
    # strip the lading whitespaces and ensure sentence is not empty
    cleaned_sentence = sentence.strip()
    if cleaned_sentence:
        print(cleaned_sentence)
