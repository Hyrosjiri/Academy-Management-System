class Payment:
    def __init__(self, student, course, amount, date, status="pending"):
        self.student = student
        self.course = course
        self.amount = amount
        self.date = date
        self.status = status

    # Označit jako zaplaceno
    def mark_as_paid(self):
        if self.status == "pending":
            self.status = "paid"
            return True
        return False

    # Označit jako nezaplaceno
    def mark_as_pending(self):
        if self.status == "paid":
            self.status = "pending"
            return True
        return False

    # Převod na slovník
    def to_dict(self):
        return {
            "student": self.student.student_id,
            "course": self.course.name,
            "amount": self.amount,
            "date": self.date,
            "status": self.status
        }
