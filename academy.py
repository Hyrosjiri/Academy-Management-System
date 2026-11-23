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
                student.enroll_in_course(course)
                return True
        return False

    # Odhlásí studenta z kurzu
    def remove_student_from_course(self, student, course):
        if student and course:
            if course.remove_student(student):
                student.remove_course(course)
                return True
        return False

"""
Chyby
3. enroll_student() – neověřuješ úspěch obou operací.
4. remove_student_from_course() – neověřuješ úspěch obou operací.
Co chybí
1. assign_instructor_to_course() – přiřazení lektora ke kurzu.
2. remove_instructor_from_course() – odebrání lektora z kurzu.
3. Metody pro správu plateb.
4. Metoda pro výpočet celkových tržeb.
5. to_dict() – převod akademie na slovník pro JSON.
 """