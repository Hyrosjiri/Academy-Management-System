from person import Person


class Instructor(Person):
    def __init__(self, name, email, phone, specialization, hourly_rate):
        super().__init__(name, email, phone)
        self.specialization = specialization
        self.hourly_rate = hourly_rate
        self.courses = []

    def get_info(self):
        info = super().get_info()
        info['specialization'] = self.specialization
        info['hourly_rate'] = self.hourly_rate
        return info

    # Přiřadí kurz lektorovi
    def assign_course(self, course):
        if course and course not in self.courses:
            self.courses.append(course)
            return True
        return False
    
    def get_courses(self):
        return self.courses