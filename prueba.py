import uuid     #import a library to create id 
import datos

uses = 0

students=[]

while uses == 0:

    print("student management system\n")

    print("------menu------\n")                 # create a menu
    print("1.Record\n")
    print("2.Consult the list\n")
    print("3.Search\n")
    print("4.Update\n")
    print("5.Eliminate\n")
    print("6.exit")
    print("---------------\n")

    try:                                         # Use a structure to handle potential errors
        option=int(input("Write an option "))

    except ValueError:

        print("only numbers")

    if option == 6:   

        print("Thanks for your use")

        uses = 1                                    # the program ends

    if option == 1:                                     # in this option    the program create the records

        student_id=uuid.uuid4().hex                    

        records=datos.record_student(student_id)

        students.append(records)

        print(records)

    if option == 2:                               # show you the list of students 

        list_of_students=datos.consult(students)

        print(students)

    if option == 3:                                 #With this you can find a student using their ID

        student_id_search=input("Enter the ID  that you are looking for ")

        student_search_engine=datos.search(students,student_id_search)

        print(student_search_engine)

    if option == 4:                     #With this you can update a student's information using their ID

        student_update_id=input("Enter the ID  that you are looking for ")

        updater=datos.update(students,student_update_id)

        print(updater)

    if option == 5:  #With this you can delete a student's information using the ID

        student_eliminate_id=input("Enter the ID  that you are looking for ") 

        eliminator= datos.elimination(students,student_eliminate_id)

        print(eliminator)

    else:
        print("error")

