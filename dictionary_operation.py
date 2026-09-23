"""Practice basic dictionary operations with a student record."""

student = {
    "name": "Alice Wong",
    "student_id": "ST1024",
    "age": 21,
    "program": "Software Engineering",
    "city": "Nanjing",
    "gpa": 3.6,
}


def average_and_status(courses):
    total = 0
    count = 0
    for score in courses.values():
        total += score
        count += 1
    average = total / count if count else 0
    if average >= 90:
        status = "Excellent"
    elif average >= 75:
        status = "Good"
    elif average >= 60:
        status = "Pass"
    else:
        status = "At Risk"
    return average, status


def find_course(courses, name):
    for course in courses:
        if course.casefold() == name.strip().casefold():
            return course
    return None


def main():
    print("Current student record")
    for key, value in student.items():
        print(f"{key}: {value}")

    if "email" not in student:
        student["email"] = input("Enter email: ").strip()

    new_city = input("Enter new city: ").strip()
    while not new_city:
        new_city = input("City cannot be empty. Enter new city: ").strip()
    student["city"] = new_city

    if student.get("phone") is None:
        print("Phone number not found.")
        student["phone"] = input("Enter phone number: ").strip()

    student["contact"] = {
        "phone": student["phone"],
        "email": student["email"],
    }
    student["courses"] = {
        "Python": 88,
        "Databases": 91,
        "Software Engineering": 84,
    }
    student["average_score"], student["academic_status"] = average_and_status(
        student["courses"]
    )

    query = input("Search for a course: ")
    course = find_course(student["courses"], query)
    if course is None:
        print("Course not found")
    else:
        print(f"{course}: {student['courses'][course]}")

    query = input("Enter the course to update: ")
    course = find_course(student["courses"], query)
    if course is None:
        print("Course not found")
    else:
        while True:
            raw_score = input("Enter the new score (0-100): ").strip()
            try:
                score = float(raw_score)
            except ValueError:
                print("Enter a number between 0 and 100.")
                continue
            if 0 <= score <= 100:
                break
            print("Enter a number between 0 and 100.")
        student["courses"][course] = int(score) if score.is_integer() else score
        print(f"{course} updated to {student['courses'][course]}.")

    student["average_score"], student["academic_status"] = average_and_status(
        student["courses"]
    )
    print("\n=====================================")
    print("        STUDENT RECORD")
    print("=====================================")
    print(f"Name: {student['name']}")
    print(f"Student ID: {student['student_id']}")
    print(f"Age: {student['age']}")
    print(f"Program: {student['program']}")
    print(f"City: {student['city']}")
    print(f"GPA: {student['gpa']}")
    print("\nCONTACT")
    print(f"Phone: {student['contact']['phone']}")
    print(f"Email: {student['contact']['email']}")
    print("\nCOURSE RESULTS")
    for course, score in student["courses"].items():
        print(f"{course}: {score}")
    print(f"\nAverage Score: {student['average_score']:.1f}")
    print(f"Academic Status: {student['academic_status']}")
    print("=====================================")


if __name__ == "__main__":
    main()
