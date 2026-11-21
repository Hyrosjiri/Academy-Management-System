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
    except ValueError:
        return []

def save_json(name_json, file_data):
    with open(name_json, "w", encoding="utf-8") as file:
        json.dump(file, file_data, ensure_ascii=False, indent=4)  

def print_title(title: str, width):
    print("=" * width)
    print(title.center)
    print("=" * width)
    print()