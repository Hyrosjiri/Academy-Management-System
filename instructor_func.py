# Importy tříd
from instructor import Instructor
from academy import Academy

# Importy pomocných funkcí
from utils import(
    print_title,
    get_int
)

# Importy textových konstant
from prompt import(
    EMPTY_DATABASE
)


def add_instructor(academy: Academy):

    print_title("PŘIDÁNÍ INSTRUKTORA")
    
    name = input("Jméno:\n>> ")
    
    if name == "0":
        return
    
    email = input("Email:\n>> ")
    phone = get_int("Telefoní číslo:\n>> ")
    specialization = input("Specializace:\n>> ")
    hourly_rate = get_int("Hodinová mzda:\n>> ")

    instructor = Instructor(name, email, phone, specialization, hourly_rate)

    if academy.add_instructor(instructor):
        print(f"\n[HOTOVO] {instructor.name} přidán.")


def remove_instructor(academy: Academy):
    pass


def show_instructors(academy: Academy):
    print_title("INSTRUKTOŘI")
    
    if not academy.instructors:
        print(EMPTY_DATABASE)
        return

    for instructor in academy.instructors:
        print(f"Jméno: {instructor.name}")
        print(f"Email: {instructor.email}")
        print(f"Telefoní číslo: {instructor.phone}")
        print(f"Specializace: {instructor.specialization}")
        print(f"Hodinová mzda: {instructor.hourly_rate} Kč")
        result = "Žádný" if not instructor.courses else ", ".join(instructor.name for course in instructor.courses)
        print(f"Kurzy: {result}")
        print()


def edit_instructor(academy: Academy):
    pass


def enroll_instructor(academy: Academy):
    pass


def unenroll_instructor(academy: Academy):
    pass