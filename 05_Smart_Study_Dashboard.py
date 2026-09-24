def is_strong(score):
    if score >= 80:
        return True

def show_course(course):
    print((f"{course['name']} - {course['score']}"))

def average_score(courses):
    total_score = 0
    for course in courses:
        total_score += course['score']

    return total_score / len(courses)


courses = [
{"name": "Python", "score": 88},
{"name": "Git", "score": 92},
{"name": "Math", "score": 74},
{"name": "SQL", "score": 81}
]

for course in courses:
    score = course['score']

    if is_strong(score):
        show_course(course)

avg_score = average_score(courses)
print(f"Average score: {avg_score}")