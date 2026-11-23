from person import Person


class Student(Person):
    def __init__(self, name, email, phone, student_id):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.courses = []

    #  přidá kurz studentovi
    def enroll_in_course(self, course):
        if course:
            self.courses.append(course)
            return True
        return False

    # odebere kurz studentovi
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            return True
        return False

    # převod na slovník
    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "student_id": self.student_id,
            "courses": [course.name for course in self.courses]
        }