# Importy tříd
from course import Course
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


def remove_course(academy: Academy):
    pass


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


def edit_course(academy: Academy):
    pass