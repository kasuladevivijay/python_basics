students_list = []

def create_student_data():
    name = input('Please enter your name => ')
    student_data = {
        "name": name,
        "marks": []
    }
    return student_data

# student_data = create_student_data()

def add_mark(student, mark):
    student['marks'].append(mark)

# add_mark(student_data, 89) #passing by reference

def calculate_average_mark(student):
    number = len(student['marks'])
    if number == 0:
        return

    total = sum(student['marks'])
    return total/number

def print_student_details(student):
    print("{}, average mark: {}.".format(student['name'],
                                         calculate_average_mark(student)))

def print_students_list(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        print_student_details(student)

def menu():
    selection = input("Enter 'p' to print student list"
                      " 's' to add a new student,"
                      " 'a' to add a mark to a student,"
                      " or 'q' to quit :")
    while selection != 'q':
        if selection == 'p':
            print_students_list(students_list)
        elif selection == 's':
            students_list.append(create_student_data())
        elif selection == 'a':
            student_id = int(input("select the stdent id from the students list"))
            student = students_list[student_id]
            new_mark = int(input("Enter the mark to be added to the student"))
            add_mark(student, new_mark)

        selection = input("Enter 'p' to print student list"
                      " 's' to add a new student,"
                      " 'a' to add a mark to a student,"
                      " or 'q' to quit :")


menu()
