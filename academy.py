class Academy():
    def __init__(self, name):
        self.name = name
        self.students = []
        self.instructors = []
        self.courses = []
        self.payments = []

    # Přidá studenta
    def add_student(self, student):
        if student:
            self.students.append(student)
            return True
        return False

    # Přidá instruktora
    def add_instructor(self, instructor):
        if instructor:
            self.instructors.append(instructor)
            return True
        return False

    # Vytvoří nový kurz
    def create_course(self, course):
        if course:
            self.courses.append(course)
            return True
        return False

    # Vyhledá studenta po emailu
    def find_student(self, email):
        if email:
            for student in self.students:
                if student.email == email:
                    return student
        return False

    # Vyhledá instruktora podle emailu
    def find_instructor(self, email):
        if email:
            for instructor in self.instructors:
                if instructor.email == email:
                    return instructor
        return False

    # Vyhledá kurz podle názvu
    def find_course(self, name):
        if name:
            for course in self.courses:
                if course.name == name:
                    return course
        return False

    # Přihlásí studenta do kurzu
    def enroll_student(self, student, course):
        if student and course:
            if course.add_student(student):
                if student.enroll_in_course(course):
                    return True
                course.remove_student(student)

        return False

    # Odhlásí studenta z kurzu
    def remove_student_from_course(self, student, course):
        if student and course:
            if course.remove_student(student):
                if student.remove_course(course):
                    return True
                course.add_student(student)
        return False
    
    # Přiřazení lektora ke kurzu
    def assign_instructor_to_course(self, instructor, course):
        if instructor and course:
            if course.add_instructor(instructor):
                if instructor.assign_course(course):
                    return True
                course.remove_instructor(instructor)
        return False
    
    # Odebrání lektro z kurzu
    def remove_instructor_from_course(self, instructor, course):
        if instructor and course:
            if course.remove_instructor(instructor):
                if instructor.remove_course(course):
                    return True
                course.add_instructor(instructor)
        return False
    
    # Převod do slovníku
    def to_dict(self):
        return {
            "name": self.name,
            "students": [student.to_dict() for student in self.students],
            "instructors": [instructor.to_dict() for instructor in self.instructors],
            "courses": [course.to_dict() for course in self.courses],
            "payments": [payment.to_dict() for payment in self.payments]
        }