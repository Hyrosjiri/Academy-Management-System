# Importy tříd
from student import Student
from academy import Academy

# Importy pomocných funkcí
from utils import(
    print_title,
    get_int,
    wait_enter,
    clear_screen
)

# Importy textových konstant
from prompt import(
    EMPTY_DATABASE
)


def add_student(academy: Academy):
    print_title("PŘIDÁNÍ STUDENTA")
    
    name = input("Jméno:\n>> ")
    
    if name == "0":
        return
    
    email = input("Email:\n>> ")
    phone = get_int("Telefoní číslo:\n>> ")
    student_id = len(academy.students) + 1

    student = Student(name, email, phone, student_id)

    if academy.add_student(student):
        print(f"\n[HOTOVO] {student.name} přidán.")


def remove_student(academy: Academy):
    print_title("ODEBRÁNÍ STUDENTA")

    if not academy.students:
        print(EMPTY_DATABASE)
        return

    email = input("Email:\n>> ")

    if email == "0":
        return

    student = academy.find_student(email)

    if not student:
        print("\n[INFO] Student nenalezen.")
        return

    if academy.remove_student(student):
        print(f"\n[INFO] {student.name} - Odstraněn")


def show_students(academy: Academy):
    print_title("STUDENTI")

    if not academy.students:
        print(EMPTY_DATABASE)
        return

    for student in academy.students:
        print(f"Jméno: {student.name}")
        print(f"Email: {student.email}")
        print(f"Telefoní číslo: {student.phone}")
        print(f"ID: {student.student_id}")
        result = "Žádný" if not student.courses else ", ".join(
        course.name for course in student.courses
)
        print(f"Kurzy: {result}")
        print()


def edit_student(academy: Academy):
    print_title("UPRAVENÍ STUDENTA")

    if not academy.students:
        print(EMPTY_DATABASE)
        return

    email = input("Email:\n>> ")

    if email == "0":
        return

    student = academy.find_student(email)

    if not student:
        print("\n[INFO] Student nenalezen.")
        pass

    while True:
        print(f"Jméno:   {student.name}")
        print(f"Email:   {student.email}")
        print(f"Telefon: {student.phone}")

        command = input(
            "\n[1] Změnit jméno\n"
            "[2] Změnit email\n"
            "[3] Změnit telefon\n"
            "\n[0] Zpět\n"
            "\nVyber možnost: "
        )

        match command:
            case "1":
                student.name = input("Nové jméno: ")
            case "2":
                student.email = input("Nový email: ")
            case "3":
                student.phone = input("Nový telefon: ")
            case "0":
                break
            case _:
                print("Neplatná volba.")

        wait_enter()
        clear_screen()

        



# Přihlásit studenta na kurz
def enroll_student(academy: Academy):
    print_title("PŘIHLÁŠENÍ STUDENTA NA KURZ")
    
    if not academy.students or not academy.courses:
        print(EMPTY_DATABASE)
        return
    
    student_email = input("Zadej email:\n>> ")
    student = academy.find_student(student_email)
    
    if not student:
        print("\n[INFO] Student nenalezen")
        return
    
    course_name = input("Název kurzu:\n>> ")
    course = academy.find_course(course_name)

    if not course:
        print(f"\n[INFO] Kurz nenalezen")
        return
    
    if academy.enroll_student(student, course):
        print(f"\n[HOTOVO] {student.name} přihlášen -> {course.name}")
        return
        
    print(f"\n[INFO] Plná Kapacita kurzu.")

# Odhlásit studenta z kurzu
def unenroll_student(academy: Academy):
    print_title("ODHLÁŠENÍ STUDENTA Z KURZU")
    
    if not academy.students or not academy.courses:
        print(EMPTY_DATABASE)
        return
    
    student_email = input("Zadej email:\n>> ")
    student = academy.find_student(student_email)
    
    if not student:
        print("\n[INFO] Student nenalezen")
        return
    
    course_name = input("Název kurzu:\n>> ")
    course = academy.find_course(course_name)

    if not course:
        print(f"\n[INFO] Kurz nenalezen")
        return
    
    if academy.remove_student_from_course(student, course):
        print(f"\n[HOTOVO] {student.name} odhlášen -> {course.name}")

