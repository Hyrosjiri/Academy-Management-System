# Importy tříd
from person import Person
from student import Student
from instructor import Instructor
from payment import Payment
from course import Course
from academy import Academy

# Importy funkcí
from utils import clear_screen, get_int, load_json, save_json, wait_enter, print_title
 
 
#  Import text
from prompt import MAIN_MENU, EMPTY_DATABASE


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

def create_course(academy: Academy):
    print_title("VYTVOŘENÍ NOVÉHO KURZU")
    
    name = input("Kurz:\n>> ")
    if name == "0":
        return
    
    price = get_int("Cena:\n>> ")
    capacity = get_int("Kapacita:\n>> ")

    course = Course(name, price, capacity)

    if academy.create_course(course):
        print(f"\n[HOTOVO] {course.name} vytvořen.")

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



def show_courses(academy: Academy):
    print_title("KURZY")
    
    if not academy.courses:
        print(EMPTY_DATABASE)
        return
    
    for course in academy.courses:
        print(f"Název: {course.name}")
        print(f"Cena: {course.price} Kč")
        print(f"Kapacita: {course.capacity}")
        print(f"Volná místa: {course.get_available_slots()}")
        list_instructors = "Žádný" if not course.instructors else ", ".join(
            instructor.name for instructor in course.instructors
        )

        list_students = "Žádný" if not course.students else ", ".join(
            student.name for student in course.students
        )
        print(f"Studenti: {list_students}")
        print(f"Instruktoři: {list_instructors}")
        print()


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

def show_payments(academy: Academy):
    pass


def create_payment(academy: Academy):
    pass


def pay_payment(academy: Academy):
    pass


def show_total_revenue(academy: Academy):
    pass


def load_file():
    pass


def save_file():
    pass


# Hlavní program
def main(name_course):
    academy = Academy(name_course)
    
    while True:
        clear_screen()
        print_title(academy.name)
        command = input(MAIN_MENU)
        clear_screen()
        
        match command:
            case "1":
                add_student(academy)
                
            case "2":
                show_students(academy)
                
            case "3":
                # upravit udaje studenta
                pass
                
            case "4":
                enroll_student(academy)
                
            case "5":
                unenroll_student(academy)
                
            case "6":
                # přidat instrutora
                pass
                                    
            case "7":
                show_instructors(academy)
                               
            case "8":
                # upravit udaje instruktora
                pass
                
            case "9":
                # priradit lektora je kurzu
                pass
                
            case "10":
                # odebrat lektora z kurz
                create_payment(academy)

            case "11":
                pay_payment(academy)

            case "12":
                show_total_revenue(academy)

            case "q" | "Q":
                
                break
            
            case _:
                print("Neplatná volba")

        wait_enter()
        
        
# Spuštění programu
if __name__ == "__main__":
    main("BLACKCAP DEV ACADEMY")