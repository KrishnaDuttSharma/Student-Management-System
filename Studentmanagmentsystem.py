# problem statement

# create a student managment system using python and oops
 
# the system should allow the user TimeoutError
# add a new student
# view alll the student
# search for a student using student id 
# update a student marks
# delete a student record using student id
# display the student with highest marks
#     exit the application
#     student detail

# each student should have

# student id
# student Name
# age
# marks

class Student:
    def __init__(self,name,id,age,marks):
        self.name=name
        self.id=id
        self.age=age
        self.marks=marks
    def display(self):
        print(f"ID of student  {self.id} ")
        print(f"Name of student  {self.name} ")
        print(f"Age of student  {self.age} ")
        print(f"Marks of student {self.marks}")
s1=Student("XYZ",9276,20,80)
s1.display()


class StudentManagment(Student):
    def __init__(self):
        self.student=[]
    def add_detail(self):
        Id=int(input("Enter the id  "))
        name=input("Enter the name ")
        age=int(input("Enter the age "))
        marks=int(input("Enter the marks "))
        students=Student(name,Id,age,marks)
        self.student.append(students)
        print("Student added successfully")
    def viewdetail(self):
        if len(self.student)==0:
            print("student not found")
        else:
            for stu in self.student:
                stu.display()
    def search(self):
        student_id=int(input("Enter student id "))
        for student in self.student:
            if student_id==student.id:
               print("Student Found")
               student.display()
               return
        print("Student Not Found")
    def delete(self):
        student_id=int(input("Enter student id "))
        for student in self.student:
            if student.id==student_id:
                self.student.remove(student)
                print("deleted successfully")
                return
            else:
                print("record not found") 

    def display_topper(self):
        if len(self.student) == 0:
            print("No Students Available!")
        else:
            topper = self.student[0]

            for student in self.student:
                if student.marks > topper.marks:
                    topper = student

            print("\nTopper Details")
            topper.display()
s=StudentManagment()
while True:
   
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Display Topper")
    print("7. Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        s.add_detail()

    elif choice == 2:
        s.viewdetail()

    elif choice == 3:
        s.search()

    elif choice == 4:
        s.update_marks()

    elif choice == 5:
        s.delete()

    elif choice == 6:
        s.display_topper()

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")



        
        

