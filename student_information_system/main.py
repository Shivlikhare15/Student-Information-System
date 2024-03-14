# student_information_system/main.py
from student import Student
from course import Courses
from grade_calculator import calculate_gpa

# create student
student1 = Student("001","Nikhil")
student2 = Student("002","Vrusabh")

# create courses
ds_course = Courses("DS01","Data Science 101")
da_course = Courses("DA01","Data Analysis 102")

#enroll students in courses
student1.add_course(ds_course,90)
student1.add_course(da_course,85)
student2.add_course(ds_course,78)
student2.add_course(da_course,92)

#display student information
print(f"{student1.name}'s Grades:{student1.get_grades()}")
print(f"{student2.name}'s Grades:{student2.get_grades()}")

# calculate and display GPA
gpa_student1 = calculate_gpa(student1.get_grades())
gpa_student2 = calculate_gpa(student2.get_grades())
print(f"{student1.name}'s GPA:{gpa_student1:.2f}")
print(f"{student2.name}'s GPA:{gpa_student2:.2f}")