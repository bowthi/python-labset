class student:
    id=" "
    name=" "
    branch=" "
    department=" "
    def get_details(self):
        self.id=input("Student id :")
        self.name=input("Name of the student :")
        self.branch=input("Enter the branch :")
        self.department=input("Enter department :")
    def print_student_details(self):
        print("\n Student ID :",self.id)
        print("\n Name :",self.name)
        print("\n Branch :",self.branch)
        print("\n Department :",self.department)
student1=student()
student1.get_details()
print("\n Student Details :")
student1.print_student_details()