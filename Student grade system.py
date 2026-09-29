# Student Grade System

students = []


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def add_student():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    grades = []

    try:
        math = float(input("Enter Math grade: "))
        science = float(input("Enter Science grade: "))
        english = float(input("Enter English grade: "))

        grades.extend([math, science, english])

        if any(grade < 0 or grade > 100 for grade in grades):
            print("Grades must be between 0 and 100.")
            return

        student = {
            "id": student_id,
            "name": name,
            "grades": grades
        }

        students.append(student)
        print("Student added successfully.")

    except ValueError:
        print("Please enter valid numeric grades.")


def view_students():
    if not students:
        print("No student records found.")
        return

    print("\nStudent Records")
    print("-" * 60)

    for student in students:
        grades = student["grades"]
        average = sum(grades) / len(grades)
        grade = calculate_grade(average)

        print(f"Student ID: {student['id']}")
        print(f"Name: {student['name']}")
        print(f"Grades: {grades}")
        print(f"Average: {average:.2f}")
        print(f"Final Grade: {grade}")
        print("-" * 60)


def search_student():
    student_id = input("Enter student ID to search: ")

    for student in students:
        if student["id"] == student_id:
            grades = student["grades"]
            average = sum(grades) / len(grades)
            grade = calculate_grade(average)

            print("\nStudent Found")
            print(f"Student ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Grades: {grades}")
            print(f"Average: {average:.2f}")
            print(f"Final Grade: {grade}")
            return

    print("Student not found.")


def delete_student():
    student_id = input("Enter student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Student deleted successfully.")
            return

    print("Student not found.")


def main():
    while True:
        print("\n===== Student Grade System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


main()
