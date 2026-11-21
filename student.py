from person import Person

class Student(Person):
    def __init__(self, name, email, phone, student_id):
        super().__init__(name, email, phone)
        self.student_id = student_id
        self.courses = []
        
    def get_info(self):
        info = super().get_info()
        info["student_id"] = self.student_id
        info["courses"] = self.courses
        return info
    
    def enroll_in_course(self, course):
        self.courses.append(course)
        return True
    
    def get_courses(self):
        return self.courses
    