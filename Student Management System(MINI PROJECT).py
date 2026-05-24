# Student Management System 

students = {
    "101": {"Name": "Arun", "Age": "18", "Course": "CSE"},
    "102": {"Name": "Kavin", "Age": "19", "Course": "AI & DS"},
    "103": {"Name": "Rahul", "Age": "18", "Course": "Cyber Security"},
    "104": {"Name": "Vignesh", "Age": "20", "Course": "Mechanical"},
    "105": {"Name": "Surya", "Age": "19", "Course": "ECE"},
    "106": {"Name": "Praveen", "Age": "18", "Course": "EEE"},
    "107": {"Name": "Harish", "Age": "21", "Course": "Civil"},
    "108": {"Name": "Ajay", "Age": "20", "Course": "IT"},
    "109": {"Name": "Dinesh", "Age": "19", "Course": "BCA"},
    "110": {"Name": "Naveen", "Age": "18", "Course": "Data Science"}
}

def add_student():
    roll = int(input("Enter Roll Number: "))

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    age = int(input("Enter Age(IN NUMBER): "))
    course = input("Enter Course: ")

    students[roll] = {
        "Name": name,
        "Age": age,
        "Course": course
    }

    print("Student Added Successfully!\n")


def view_students():
    if not students:
        print("No student records found.\n")
        return

    print("\n--- Student Records ---")

    for roll, details in students.items():
        print(f"\nRoll No: {roll}")
        print(f"Name   : {details['Name']}")
        print(f"Age    : {details['Age']}")
        print(f"Course : {details['Course']}")


def search_student():
    roll = input("Enter Roll Number to Search: ")

    if roll in students:
        details = students[roll]

        print("\nStudent Found")
        print(f"Name   : {details['Name']}")
        print(f"Age    : {details['Age']}")
        print(f"Course : {details['Course']}")
    else:
        print("Student not found.\n")


def update_student():
    roll = input("Enter Roll Number to Update: ")

    if roll in students:
        name = input("Enter New Name: ")
        age = int(input("Enter New Age(IN NUMBER): "))
        course = input("Enter New Course: ")

        students[roll] = {
            "Name": name,
            "Age": age,
            "Course": course
        }

        print("Student Updated Successfully!\n")
    else:
        print("Student not found.\n")


def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    if roll in students:
        del students[roll]
        print("Student Deleted Successfully!\n")
    else:
        print("Student not found.\n")


while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid choice! Please try again.")
