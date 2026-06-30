students = []

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")

    student = {
        "Roll Number": roll,
        "Name": name,
        "Department": department
    }

    students.append(student)
    print("Student added successfully!")

def view_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        print("\nStudent Records")
        print("----------------------------")
        for student in students:
            print("Roll Number :", student["Roll Number"])
            print("Name        :", student["Name"])
            print("Department  :", student["Department"])
            print("----------------------------")

def update_student():
    roll = input("Enter Roll Number to Update: ")

    for student in students:
        if student["Roll Number"] == roll:
            student["Name"] = input("Enter New Name: ")
            student["Department"] = input("Enter New Department: ")
            print("Student updated successfully!")
            return

    print("Student not found.")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for student in students:
        if student["Roll Number"] == roll:
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")

while True:
    print("\n===== Student Database Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Thank You!")
        break
    else:
        print("Invalid choice. Please try again.")