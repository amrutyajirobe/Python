
class student:
    major='CSE'

    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name


s1=student(1,'John')
s2=student(2,'Harry')


print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)


print(student.major)
