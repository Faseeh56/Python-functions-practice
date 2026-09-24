students = [
{"name": "Ali", "score": 82},
{"name": "Sara", "score": 91},
{"name": "Hamza", "score": 67},
{"name": "Ayesha", "score": 88}
]

def is_high_score(score):
    if score >= 80:
        return True
    else:
        return False        

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    else:
        return "Need improvement"

def show_student(student):
    print(f"{student['name']} - {student['score']} - {get_grade(student['score'])}")

for student in students:
    score = student["score"]

    if is_high_score(score):
        show_student(student)
        
    
