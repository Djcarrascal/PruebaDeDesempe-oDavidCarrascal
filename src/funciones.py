list_of_students = []
"""
En este apartado estaré trabajando en las funciones que llamaré en archivo sistema.py
"""
def register_student():
    while True:
        try:
            id = int(input("\nEnter the student identification number: "))
            if not id:
                print("\nYou cannot leave the field empty, please enter the student ID.")
                continue

        except ValueError:
            print("\nEnter a valid value.")
            continue
        break

    while True:
        try:
            name = str(input("\nEnter the student's name: "))
            if not name:
                print("\nYou cannot leave the field empty.")
                continue

            elif not name.isalpha():
                print("\nYou can only enter letters.")
                continue
        except ValueError:
            print("Enter a valid value.")
            continue
        break
    while True:
        try:
            age = int(input("\nEnter the student's age: "))
            if not age:
                print("\nYou cannot leave the field empty.")
                continue

        except ValueError:
            print("\nOnly numbers can be entered.")
            continue
        break
    while True:
        try:
            course_or_program = str(input("\nEnter the name of the course or program you belong to: "))
            if not course_or_program:
                print("\nYou cannot leave the field empty.")
            elif not course_or_program.isalpha():
                print("\nOnly letters can be entered")
                continue
            break
        except ValueError:
            print("\nEnter a valid value.")
            continue
    while True:
        try:
            state = str(input("\nIs the student's status active or inactive?: "))
            if not state:
                print("\nYou cannot leave the field empty..")
            elif not course_or_program.isalpha():
                print("\nYou can only enter letters.")
                continue
            break
        except ValueError:
            print("\nEnter a valid value.")

    student = {
        "id":id,
        "name":name,
        "age": age,
        "course":course_or_program,
        "state": state
    }

    list_of_students.append(student)

    print("\nRegistered student.")

def search_student(id):
    for student in list_of_students:
        if student["id"] == int(id):
            return student
    return None

def update_student(id, name, age, course, state):
    for student in list_of_students:
        if student["id"] == id:
            student["name"] = name
            student["age"] = age
            student["course"] = course
            student["state"] = state
            print("Update data")
            return
        else:
            print("\nStudent no found")

def delete_student(id):
    for student in list_of_students:
        if student["id"] == id:
            list_of_students.remove(student)
            print("Erased student")
        else:
            print("\nStudent no found")



