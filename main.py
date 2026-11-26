# Standartní Importy
from email.policy import default
import time

# Importy tříd
from academy import Academy

# Importy funkcí
from student_func import(
    add_student,
    remove_student,
    show_students,
    edit_student,
    enroll_student,
    unenroll_student
)

from instructor_func import(
    add_instructor, 
    remove_instructor,
    show_instructors,
    edit_instructor,
    enroll_instructor,
    unenroll_instructor
)

from course_func import (
    create_course,
    remove_course,
    show_courses,
    edit_course
)

# Importy pomocných funkcí
from utils import (
    clear_screen,
    load_json,
    save_json,
    wait_enter,
    print_title
)

# Importy textových konstant
from prompt import (
    MAIN_MENU,
    STUDENT_MENU,
    INSTRUCTOR_MENU,
    COURSE_MENU,
    PAYMENT_MENU
)


# Funkce
def load_file(name_academy):
    data = load_json("academy.json", default=None)

    if data is None:
        return Academy(name_academy)

    return Academy.from_dict(data)

def save_file(academy: Academy):
    save_json("academy.json", academy.to_dict())


# Hlavní program
def main(name_academy):
    academy = load_file(name_academy)
    
    while True:
        clear_screen()
        print_title(academy.name)
        command = input(MAIN_MENU)
         
        match command:
            case "1":
                while True:
                    clear_screen()
                    print_title("SPRÁVA STUDENTŮ")
                    command = input(STUDENT_MENU)
                    

                    match command:

                        case "1":
                            clear_screen()
                            add_student(academy)

                        case "2":
                            clear_screen()
                            remove_student(academy)

                        case "3":
                            clear_screen()
                            show_students(academy)

                        case "4":
                            clear_screen()
                            edit_student(academy)

                        case "5":
                            clear_screen()
                            enroll_student(academy)

                        case "6":
                            clear_screen()
                            unenroll_student(academy)

                        case "0":
                            break

                        case _:
                            print("Neplatná volba.")
                            time.sleep(0.4)
                            continue

                    wait_enter()


            case "2":
                while True:
                    clear_screen()
                    print_title("SPRÁVA INSTRUKTORŮ")
                    command = input(INSTRUCTOR_MENU)

                    match command:

                        case "1":
                            clear_screen()
                            add_instructor(academy)

                        case "2":
                            clear_screen()
                            remove_instructor(academy)

                        case "3":
                            clear_screen()
                            show_instructors(academy)

                        case "4":
                            clear_screen()
                            edit_instructor(academy)

                        case "5":
                            clear_screen()
                            enroll_instructor(academy)

                        case "6":
                            clear_screen()
                            unenroll_instructor(academy)

                        case "0":
                            break

                        case _:
                            print("Neplatná volba.")
                            time.sleep(0.4)
                            continue

                    wait_enter()

            case "3":
                while True:
                    clear_screen()
                    print_title("SPRÁVA KURZŮ")
                    command = input(COURSE_MENU)

                    match command:

                        case "1":
                            clear_screen()
                            create_course(academy)

                        case "2":
                            clear_screen()
                            remove_course(academy)

                        case "3":
                            clear_screen()
                            show_courses(academy)

                        case "4":
                            clear_screen()
                            edit_course(academy)

                        case "0":
                            break

                        case _:
                            print("Neplatná volba.")
                            time.sleep(0.4)
                            continue

                    wait_enter()

            case "4":
                while True:
                    clear_screen()
                    print_title("SPRÁVA PLATEB")
                    command = input(PAYMENT_MENU)

                    match command:
                        
                        case "1":
                            pass

                        case "2":
                            pass

                        case "3":
                            pass

                        case "0":
                            break

                        case _:
                            print("Neplatná volba.")
                            time.sleep(0.4)

            case "q" | "Q":
                save_file(academy)
                break
            
            case _:
                print("Neplatná volba.")
                time.sleep(0.4)
        
        
# Spuštění programu
if __name__ == "__main__":
    main("BLACKCAP DEV ACADEMY")