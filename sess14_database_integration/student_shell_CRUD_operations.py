# Python script to demonstrate MySQL database CRUD operations on the command line / shell
# NB: Ensure you've installed the mysql python connector => pip install mysql-connector-python

# Import the required modules
import mysql.connector
from db_conn import db_config
from student import Student

# Function to connect to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connected to python232401 MySQL database") # Remove in production code
            return connection
    except mysql.connector.Error as err:
        print(f"Error: Unable to connect to MySQl: {err}")
        return None

# Function to close the db connection
def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")

# Function to get / fetch student details from the python232401 database
def read_students(connection):
    try:
        cursor = connection.cursor()
        select_query = "SELECT * FROM student"
        cursor.execute(select_query)
        students = cursor.fetchall()
        for student in students:
            student = Student(*student)
            print(student)
    except mysql.connector.Error as err:
        print(f"Error: Unable to get student details from MySQL: {err}")

# Function to insert / add a student record into the student database
def insert_student(connection, student):
    try:
        cursor = connection.cursor()
        insert_qury = """INSERT INTO student(StudentNO,Name,BirthDate,Gender,City) VALUES (%s,%s,%s,%s,%s)"""
        student_data = (student.student_no, student.name, student.birth_date, student.gender, student.city)
        cursor.execute(insert_qury, student_data)
        connection.commit() # Save / store / persists commit changes to the python232401 database
        print(f"Student {student.name} inserted successfully")
    except mysql.connector.Error as err:
        print(f"Error: Unable to insert {student.name}'s details into MySQL: {err}")
    finally:
        cursor.close() # Close the cursor
        # close_connection(connection) # Close the database connection

# Function to update / modify the student details
def update_student(connection, student):
    try:
        cursor = connection.cursor()
        update_query= """
            UPDATE student
            SET Name=%s,BirthDate=%s,Gender=%s,City=%s
            WHERE StudentNo=%s
        """

        student_data = (student.name, student.birth_date, student.gender, student.city, student.student_no)
        cursor.execute(update_query, student_data)
        connection.commit()
        if cursor.rowcount > 1:
            print(f"Student {student.name} updated successfully")
        else:
            print(f"Student {student.name} not updated successfully")
    finally:
        cursor.close() # Close the cursor
        # close_connection(connection) # Close the database connection

# Function to delete a student's record from the database from the record
def delete_student(connection, student):
    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM student WHERE StudentNo=%s"
        cursor.execute(delete_query, (student.student_no,))
        connection.commit()
        if cursor.rowcount > 0:
            print(f"Student {student.name} deleted successfully")
        else:
            print(f"No record with the given student number was found!")
    except mysql.connector.Error as err:
        print(f"Error: Unable to delete student {student.name} from MySQL: {err}")
    finally:
        cursor.close()

# Run the script to perform the CRUD operations
if __name__ == '__main__':
    connection = connect_to_database()
    if connection.is_connected():
        # Create some studen objects
        new_student1 = Student("EICN_ADSE232401_S009", "Peter Njuguna", "2006-04-09", "m", "Mombasa")

        dummy_student = Student("EICN_ADSE232401_S010", "Some Dummy Student", "2010-04-09", "m", "Nyali")

        # Get all the students from the database
        read_students(connection)

        # Add / Insert the above student's details to the python232401 database
        # insert_student(connection, new_student1)
        # insert_student(connection, new_student1)
        delete_student(connection, new_student1)

        # read_students(connection)

    close_connection(connection)