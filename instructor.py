from person import Person


class Instructor(Person):
    def __init__(self, name, email, phone, specialization, hourly_rate, courses = []):
        super().__init__(name, email, phone)
        self.specialization = specialization
        self.hourly_rate = hourly_rate
        self.courses = courses

    # přiřadí kurz instruktorovi
    def assign_course(self, course):
        pass

    # odebere kurz instruktorovi
    def remove_course(self, course):
        pass

    # převod na slovnik
    def to_dict(self):
        pass