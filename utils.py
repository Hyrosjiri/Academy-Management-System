import os
import json


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def wait_enter(text="\n[ENTER] - Pokračovat"):
    input(text)


def load_json(name_json):
    try:
        with open(name_json, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def save_json(name_json, file_data):
    with open(name_json, "w", encoding="utf-8") as file:
        json.dump(file_data, file, ensure_ascii=False, indent=4)  


def print_title(title: str, width=40):
    print("=" * width)
    print(title.center(width))
    print("=" * width)
    print()
    
    
def get_int(text):
    while True:
        try:
            data = int(input(text))
            if data < 0:
                print(f"[CHYBA] Číslo nesmí být záporné!\n")
                continue
            return data
        except ValueError:
            print(f"[CHYBA] Neplaný vstup!\n") 