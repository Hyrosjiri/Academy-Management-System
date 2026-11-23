class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def edit_email(self, new_email):
        if new_email:
            self.email = new_email
            return True
        return False
    
    def edit_name(self, new_name):
        if new_name:
            self.name = new_name
            return True
        return False

    def edit_phone(self, new_phone):
        if new_phone:
            self.phone = new_phone
            return True
        return False