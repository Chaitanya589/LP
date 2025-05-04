import csv

# Define the fields and file
student_fields = ['roll', 'name', 'age', 'email', 'phone']
student_database = 'students.csv'

# Display menu
def display_menu():
    print("\n1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")

# Add a new student
def add_student():
    student_data = [input(f"Enter {field}: ") for field in student_fields]
    with open(student_database, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(student_data)
    print("Student added!\n")

# View all students
def view_students():
    try:
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                print(", ".join(row))
    except FileNotFoundError:
        print("No students found.\n")

# Search for a student by roll number
def search_student():
    roll = input("Enter roll number: ")
    found = False
    try:
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == roll:
                    print("Student found:", ", ".join(row))
                    found = True
                    break
    except FileNotFoundError:
        print("No students found.\n")
    
    if not found:
        print("Student not found.\n")

# Update student information
def update_student():
    roll = input("Enter roll number to update: ")
    updated_data = []
    updated = False
    try:
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == roll:
                    print("Updating student info:")
                    row = [input(f"Enter {field}: ") for field in student_fields]
                    updated = True
                updated_data.append(row)
        
        if updated:
            with open(student_database, "w", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("Student updated!\n")
        else:
            print("Student not found.\n")
    except FileNotFoundError:
        print("No students found.\n")

# Delete a student
def delete_student():
    roll = input("Enter roll number to delete: ")
    updated_data = []
    deleted = False
    try:
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] != roll:
                    updated_data.append(row)
                else:
                    deleted = True
        
        if deleted:
            with open(student_database, "w", newline='', encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("Student deleted!\n")
        else:
            print("Student not found.\n")
    except FileNotFoundError:
        print("No students found.\n")

# Main loop
while True:
    display_menu()
    choice = input("Enter choice (1-6): ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        update_student()
    elif choice == '5':
        delete_student()
    elif choice == '6':
        print("Thank you for using the system!")
        break
    else:
        print("Invalid choice. Try again.")
