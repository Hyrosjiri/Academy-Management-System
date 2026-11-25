# Importy tříd
from instructor import Instructor
from academy import Academy

# Importy pomocných funkcí
from utils import(
    print_title,
    get_int,
    clear_screen
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
    print_title("ODEBRÁNÍ INSTRUKTURA")

    if not academy.instructors:
        print(EMPTY_DATABASE)
        return
    
    email = input("Email:\n>> ")

    if email == "0":
        return
    
    instructor = academy.find_instructor(email)

    if not instructor:
        print(f"\n[INFO] Instruktor nenalezen.")
        return
    
    if academy.remove_insturctor(instructor):
        print(f"\n[INFO] {instructor.name} - Odstaněn")

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
    print_title("UPRAVENÍ INSTRUKTORA")

    if not academy.instructors:
        print(EMPTY_DATABASE)
        return
    
    email = input("Email:\n>> ")

    if email == "0":
        return
    
    instructor = academy.find_instructor(email)

    if not instructor:
        print("\n[INFO] Instruktor nenalezen.")
        return
    
    while True:
        clear_screen()
        print(f"Jméno:   {instructor.name}")
        print(f"Email:   {instructor.phone}")
        print(f"Telefon: {instructor.phone}")

        command = input(
            "\n[1] Změnit jméno\n"
            "[2] Změnit email\n"
            "[3] Změnit telefon\n"
            "\n[0] Zpět\n"
            "\nVyber možnost: "
        )

        match command:
            case "1":
                instructor.name = input("\nNové jméno: ")
            case "2":
                instructor.email = input("\nNový email: ")
            case "3":
                instructor.phone = get_int("\nNový telefon: ")
            case "0":
                break
            case _:
                print("\nNeplatná volba.")


# Přihlásit instruktora na kuz
def enroll_instructor(academy: Academy):
    print_title("PŘIHLÁŠENÍ INSTRUKTORA NA KURZ")

    if not academy.instructors or not academy.courses:
        print(EMPTY_DATABASE)
        return
    
    instructor = academy.find_instructor(input("Zadej email:\n>> "))
    
    if not instructor:
        print("\n[INFO] Instruktor nenalezen")
        return
    
    course = academy.find_course(input("\nNázev kurzu:\n>> "))

    if not course:
        print("\n[INFO] Kurz nenalezen")
        return
    
    if academy.assign_instructor_to_course(instructor, course):
        print(f"\n[HOTOVO] {instructor.name} přihlášen -> {course.name}")
        return
    
    print("\n[CHYBA]")


def unenroll_instructor(academy: Academy):
    print_title("ODHLÁŠENÍ INSTRUKTORA Z KURZU")

    if not academy.instructors or not academy.courses:
        print(EMPTY_DATABASE)
        return

    instructor = academy.find_instructor(input("Zadej email:\n>> "))
    
    if not instructor:
        print("\n[INFO] Instruktor nenalezen")
        return
    
    course = academy.find_course(input("\nNázev kurzu:\n>> "))

    if not course:
        print("\n[INFO] Kurz nenalezen")
        return
    
    if academy.remove_instructor_from_course(instructor, course):
        print(f"\n[HOTOVO] {instructor.name} odhlášen -> {course.name}")
        return
    
    print("\n[CHYBA]")