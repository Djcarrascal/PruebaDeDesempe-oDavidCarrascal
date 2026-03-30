from funciones import *
opcion = 1

#We will create the interface's entry menu
print("\nWelcome to the student management system.")

while opcion >= 0 or opcion <=5:
    print("\n¿What operation do you want to have done?")
    print("\nOptions Menu:")
    print("1. Register new student.")
    print("2. View student list.")
    print("3. Search student.")
    print("4. Update student information.")
    print("5. Remove student from list.")
    print("0. Log off")
    while True:
        try:
              opcion =int(input("\nEnter an option: "))
              if opcion < 0 or opcion > 5:
                   print("\nPlease enter a valid option.")
              break
        except ValueError:
              print("\nPlease enter a valid option.")
    if opcion == 1:
         register_student()
    if opcion == 2:
        if not list_of_students:
              print("\nThere are no registered students")
        else:
             print(list_of_students)

    if opcion == 3:
        id = input("\nEnter the ID of the student you want to search for: ")
        student = search_student(id)

        if student:
            print(f"\nStudent data: NAme: {student["name"]}, Age: {student["age"]}, Course {student["course"]}, State {student["state"]}.")
        else:
            print("\nThe student is not registered.")

    if opcion == 4:
         id = int(input("\nEnter the ID of the student to be updated: "))
         name = str(input("\nEnter the updated name: "))
         age = int(input("\nEnter updated age: "))
         course = str(input("\nEnter the updated course: "))
         state = str(input("\nEnter the updated student status: "))
         update_student(id, name, age, course, state)

    if opcion == 5:
         id = int(input("\nEnter the ID of the student to be deleted."))
         delete_student(id)

    if opcion == 0:
         print("\nThank you for using this system.")
         break