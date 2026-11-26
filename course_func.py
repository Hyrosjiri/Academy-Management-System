# Importy tříd
from course import Course
from academy import Academy

# Importy pomocných funkcí
from utils import(
    print_title,
    get_int,
    clear_screen,
    wait_enter
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

    # Kontrola duplicity
    for check in academy.courses:
        if check.name == name:
            print("\n[INFO] Tento kurz již exituje.")
            return
    
    price = get_int("\nCena:\n>> ")
    capacity = get_int("\nKapacita:\n>> ")

    course = Course(name, price, capacity)

    if academy.create_course(course):
        print(f"\n[HOTOVO] {course.name} vytvořen.")


def remove_course(academy: Academy):
    print_title("ODSTRANĚNÍ KURZU")

    name = input("Název:\n>> ")

    if name == "0":
        return
    
    course = academy.find_course(name)

    if not course:
        print("[INFO] Kurz nenalezen.")
        return
    
    if not course.instructors and not course.students:
        if academy.remove_course(course):
            print(f"\n[INFO] {course.name} - Odstraněn")
            return
    print("\nKurz pro odstranění musí být prázdný.")    


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
    print_title("UPRAVENÍ KURZU")

    if not academy.courses:
        print(EMPTY_DATABASE)
        return
    
    name = input("Název:\n>> ")

    if name == "0":
        return
    
    course = academy.find_course(name)

    if not course:
        print("\n[INFO] Kurz nenalezen")
        return
    
    while True:
        clear_screen()
        print(f"Název:    {course.name}")
        print(f"Cena:     {course.price} Kč")
        print(f"Kapacita: {course.capacity}")

        command = input(
            "\n[1] Změnit název\n"
            "[2] Změnit cenu\n"
            "[3] Změnit kapacitu\n"
            "\n[0] Zpět\n"
            "\nVyber možnost: "
        )

        match command:
            case "1":
                course.name = input("\nNová název: ")
            case "2":
                course.price = get_int("\nNová cena: ")
            case "3":
                new_capacity = get_int("\nNová kapacita: ")

                if new_capacity >= len(course.students):
                    course.capacity = new_capacity
                    continue

                print("\n[CHYBA] Kapacita musí být nad limit počet studentů!")
                wait_enter()
            case "0":
                break
            case _:
                print("\nNeplatná volba.")