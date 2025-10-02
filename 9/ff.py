#This is the scoring criteria: 
# Scores 91 - 100: Grade = "Outstanding" 
# Scores 81 - 90: Grade = "Exceeds Expectations" 
# Scores 71 - 80: Grade = "Acceptable" 
# Scores 70 or lower: Grade = "Fail" 

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for student, grade in student_scores.items():
    if grade >= 91:
        student_grades[student] = 'Outstanding'
    elif grade >= 81:
        student_grades[student] = 'Exceeds Expectations'
    elif grade >= 71:
        student_grades[student] = 'Acceptable'
    else:
        student_grades[student] = 'Fail'

print(student_grades)