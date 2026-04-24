n = int(input("Enter No of records- "))
students = []

for i in range(n):
    print(f"Enter Details of student-{i+1}")
    name = input("Enter Student name- ")
    edu = input("Enter Higher Education- ")
    skill = input("Enter Primary Skill- ")
    year = input("Enter Year of Graduation- ")
    
    students.append((name, edu, skill, year))

print("\nEnter Job Role Requirement")
req_skill = input("Enter Skill- ")
req_edu = input("Enter Higher Education- ")
req_year = input("Enter Year of Graduation- ")

found = False

for student in students:
    if (student[1].lower() == req_edu.lower() and
        student[2].lower() == req_skill.lower() and
        student[3] == req_year):
        
        print(student)
        found = True

if not found:
    print("No such candidate")