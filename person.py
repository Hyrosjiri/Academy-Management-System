class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        
    def get_info(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }
        
    def change_email(self, new_email):
        if new_email:
            self.email = new_email
            return True
        return False
    