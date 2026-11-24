class Course:
    def __init__(self, name, price, capacity):
        self.name = name
        self.price = price
        self.capacity = capacity
        self.instructors = []
        self.students = []

    def add_student(self, student):
        if student and self.get_available_slots() > 0:
            self.students.append(student)
            return True
        return False

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            return True
        return False
    
    def add_instructor(self, instructor):
        if instructor:
            self.instructors.append(instructor)
            return True
        return False
    
    def remove_instructor(self, instructor):
        if instructor:
            self.instructors.remove(instructor)
            return True
        return False

    # Vrátí počet volných míst
    def get_available_slots(self):
        return self.capacity - len(self.students)

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "capacity": self.capacity,
            "instructors": [instructor.email for instructor in self.instructors],
            "students": [student.student_id for student in self.students]
        }
