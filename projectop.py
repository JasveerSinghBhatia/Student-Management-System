class Student: 
    def __init__(self, name: str, age: int, address: str, marks: int) -> None:
        self.name = name
        self.age = age
        self.address = address
        self.marks = marks

class StudentManagementSystem: 
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter name: ").strip()
        
        # Input validation for age and marks
        while True:
            try:
                age = int(input("Enter age: "))
                if age < 0:
                    raise ValueError("Age cannot be negative")
                break
            except ValueError as e:
                print(f"Invalid input for age. Please enter a valid number. ({e})")

        address = input("Enter address: ").strip()

        while True:
            try:
                marks = int(input("Enter marks: "))
                if marks < 0 or marks > 100:
                    raise ValueError("Marks should be between 0 and 100")
                break
            except ValueError as e:
                print(f"Invalid input for marks. Please enter a valid number. ({e})")

        student = Student(name, age, address, marks)
        self.students.append(student)
        print("Student successfully added.")

    def view_students(self):
        if not self.students:
            print("No students found.")
            return
        
        view_type = input("View all students or one student? (all/one): ").strip().lower()
        if view_type == "all":
            for student in self.students:
                self.print_student_details(student)
        elif view_type == "one":
            name = input("Enter the name of the student you want to view: ").strip()
            for student in self.students:
                if student.name.lower() == name.lower():
                    self.print_student_details(student)
                    return
            print(f"Student with name '{name}' not found.")
        else:
            print("Invalid option. Please choose either 'all' or 'one'.")

    def delete_student(self):
        name = input("Enter the name of the student you want to delete: ").strip()
        for student in self.students:
            if student.name.lower() == name.lower():
                self.students.remove(student)
                print(f"Student '{student.name}' successfully deleted.")
                return
        print(f"Student with name '{name}' not found.")

    def update_student(self):
        name = input("Enter the name of the student you want to update: ").strip()
        for student in self.students:
            if student.name.lower() == name.lower():
                print("Enter new details (leave blank to keep the current value):")

                new_name = input(f"New name (current: {student.name}): ").strip()
                if new_name:
                    student.name = new_name
                
                while True:
                    new_age = input(f"New age (current: {student.age}): ").strip()
                    if not new_age:
                        break
                    try:
                        new_age = int(new_age)
                        if new_age < 0:
                            raise ValueError("Age cannot be negative")
                        student.age = new_age
                        break
                    except ValueError as e:
                        print(f"Invalid input for age. ({e})")
                
                new_address = input(f"New address (current: {student.address}): ").strip()
                if new_address:
                    student.address = new_address

                while True:
                    new_marks = input(f"New marks (current: {student.marks}): ").strip()
                    if not new_marks:
                        break
                    try:
                        new_marks = int(new_marks)
                        if new_marks < 0 or new_marks > 100:
                            raise ValueError("Marks should be between 0 and 100")
                        student.marks = new_marks
                        break
                    except ValueError as e:
                        print(f"Invalid input for marks. ({e})")

                print(f"Student '{student.name}' successfully updated.")
                return
        print(f"Student with name '{name}' not found.")

    @staticmethod
    def print_student_details(student):
        print(f"\nName: {student.name}\nAge: {student.age}\nAddress: {student.address}\nMarks: {student.marks}\n")

# Main program
print("Welcome to Student Management System\n")
system = StudentManagementSystem()

while True:
    print("\n1. Add Student")
    print("2. View Student(s)")
    print("3. Delete Student")
    print("4. Update Student")
    print("5. Exit the system")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        system.add_student()
    elif choice == 2:
        system.view_students()
    elif choice == 3:
        system.delete_student()
    elif choice == 4:
        system.update_student()
    elif choice == 5:
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
