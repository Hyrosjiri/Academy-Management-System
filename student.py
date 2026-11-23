from person import Person


class Student(Person):
    def __init__(self, name, email, phone, student_id):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.courses = []

    #  přidá kurz studentovi
    def enroll_student_in_course(self, course):
        pass

    # odebere kurz studentovi
    def remove_course(self, course):
        pass

    # převod na slovník
    def to_dict(self):
        pass



