from person import Person


class Instructor(Person):
    def __init__(self, name, email, phone, specialization, hourly_rate):
        super().__init__(name, email, phone)
        self.specialization = specialization
        self.hourly_rate = hourly_rate
        self.courses = []

    # přiřadí kurz instruktorovi
    def assign_course(self, course):
        if course:
            self.courses.append(course)
            return True
        return False

    # odebere kurz instruktorovi
    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            return True
        return False

    # převod na slovnik
    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "specialization": self.specialization,
            "hourly_rate": self.hourly_rate,
            "courses": [course.name for course in self.courses]
        }