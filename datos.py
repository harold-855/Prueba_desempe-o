
def record_student(student_id):

    counter=0

    while counter==0:
    
        name=input("write the name of the students ")

        if not name.replace(" ", "").isalpha():

            print("only letters\n")
    
        else:

            print("successful entry\n")

            counter=1

    counter_1=0

    while counter_1==0:

        try:
            age=abs(int(input("Write the age ")))

        except ValueError:

            print("only numbers\n")

        if age==0:

            print("must be greater than zero\n")
        
        else:

            print("successful entry\n")

            counter_1=1

    counter_2=0

    while counter_2==0:

        course=input("write the course ")

        if not course.replace(" ", "").isalpha():

            print("only letters\n")

        else:

            print("successful entry\n")

            counter_2=1

    counter_3=0

    while counter_3==0:

        state=input("write the state  ¿is it active or inactive? ")

        if not state.replace(" ", "").isalpha():

            print("only letters\n")
        
        else:

            print("successful entry\n")

            counter_3=1

    return {"student_id":student_id,"name":name,"age":age,"course":course,"state":state}



def consult(students):

    for student in students:

        return student
    
def search (students,student_id_search):

    for student in students:

        if student["student_id"]==student_id_search:

            return student
        
def update(students,student_update_id):
    
    counter=0

    while counter==0:
    
        new_name=input("write the new name ")

        if not new_name.replace(" ", "").isalpha():

            print("only letters\n")

        else:

            print("successful entry\n")
            counter=1

    counter_1=0

    while counter_1==0:

        try:
            new_age=abs(int(input("Write the  new age ")))

        except ValueError:

            print("only numbers\n")

        if new_age==0:

            print("must be greater than zero\n")
        
        else:

            print("successful entry\n")

            counter_1=1
    
    counter_2=0

    while counter_2==0:

        new_course=input("write the  new course ")

        if not new_course.replace(" ", "").isalpha():

            print("only letters\n")

        else:

            print("successful entry\n")

            counter_2=1

    counter_3=0

    while counter_3==0:

        new_state=input("write the state  ¿is it active or inactive? ")

        if not new_state.replace(" ", "").isalpha():

            print("only letters\n")
        
        else:

            print("successful entry\n")

            counter_3=1


    for student in students:

        if student["student_id"]==student_update_id:
            student["name"]=new_name
            student["age"]=new_age
            student["course"]=new_course
            student["state"]=new_state
            return student
        
def elimination(students,student_eliminate_id):
    
    for student in students:

        if student["student_id"]==student_eliminate_id:
            students.remove(student)
            return students
