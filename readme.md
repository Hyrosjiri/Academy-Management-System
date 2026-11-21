# 🎓 Academy Management System

Konzolová aplikace v jazyce **Python** pro správu vzdělávací akademie, která pořádá kurzy programování, umělé inteligence a kancelářských aplikací.

Projekt je zaměřený na procvičení **objektově orientovaného programování (OOP)**, dědičnosti, spolupráce objektů a ukládání dat do JSON.

## 📌 Cíl projektu

Vytvořit aplikaci, která umožní:

- Evidovat studenty a lektory.
- Vytvářet a spravovat kurzy.
- Přihlašovat a odhlašovat studenty.
- Kontrolovat kapacitu kurzů.
- Evidovat platby a jejich stav.
- Vypočítat celkové tržby akademie.
- Ukládat a načítat data pomocí JSON.

Aplikace bude ovládána prostřednictvím konzolového menu.

## 🏗️ Objektový návrh

### 1. Person (rodičovská třída)

**Atributy:**
- `name`
- `email`
- `phone`

**Metody:**
- `print_info()` – vypíše informace o osobě.
- `change_email(new_email)` – změní e-mailovou adresu.

### 2. Student (dědí z Person)

**Atributy:**
- `student_id`
- `courses`

**Metody:**
- `print_info()` – rozšíří rodičovskou metodu pomocí `super()`.
- `enroll_in_course(course)` – přihlásí studenta na kurz.
- `print_courses()` – zobrazí studentovy kurzy.

### 3. Instructor (dědí z Person)

**Atributy:**
- `specialization`
- `hourly_rate`
- `courses`

**Metody:**
- `print_info()` – rozšíří rodičovskou metodu.
- `assign_course(course)` – přiřadí kurz lektorovi.
- `print_courses()` – zobrazí vyučované kurzy.

### 4. Course

**Atributy:**
- `name`
- `price`
- `capacity`
- `instructor`
- `students`

**Metody:**
- `add_student(student)` – přihlásí studenta při dostupné kapacitě.
- `remove_student(student)` – odebere studenta z kurzu.
- `print_students()` – zobrazí přihlášené studenty.
- `available_slots()` – vrátí počet volných míst.

### 5. Payment

**Atributy:**
- `student`
- `course`
- `amount`
- `date`
- `status`

**Metody:**
- `process_payment()` – nastaví stav na zaplaceno.
- `refund_payment()` – nastaví stav na vráceno.
- `print_payment()` – zobrazí informace o platbě.

### 6. Academy (hlavní řídicí třída)

**Atributy:**
- `name`
- `students`
- `instructors`
- `courses`
- `payments`

**Metody:**
- `add_student(student)` – přidá studenta do akademie.
- `add_instructor(instructor)` – přidá lektora.
- `create_course(course)` – vytvoří kurz.
- `show_courses()` – zobrazí všechny kurzy.
- `find_student(email)` – vyhledá studenta podle e-mailu.
- `show_revenue()` – vypočítá celkové tržby ze zaplacených plateb.
- `save_data()` – uloží data do JSON.
- `load_data()` – načte data z JSON.

Třída `Academy` zajišťuje správu jednotlivých objektů a jejich vzájemnou spolupráci.

## 💻 Konzolové menu

```text
================================
       AKADEMICKÝ SYSTÉM
================================

1. Přidat studenta
2. Přidat lektora
3. Vytvořit kurz
4. Přihlásit studenta na kurz
5. Zobrazit všechny kurzy
6. Zobrazit studenty
7. Zobrazit platby
8. Zobrazit celkové tržby
9. Uložit data
10. Načíst data
0. Ukončit program

Vyber možnost:
```

## 🧪 Testovací scénář

**Testovací data:**

| Objekt | Hodnota |
|---|---|
| Student | Petr Novák |
| Student | Jana Svobodová |
| Instructor | Martin Dvořák |
| Course | Python OOP |
| Course | AI v praxi |

**Požadovaný postup:**

1. Vytvořit dva studenty a jednoho lektora.
2. Vytvořit dva kurzy.
3. Přiřadit lektora ke kurzům.
4. Přihlásit studenty.
5. Zkontrolovat volnou kapacitu.
6. Vytvořit platby za kurzy.
7. Provést platby a zobrazit jejich stav.
8. Vypočítat celkové tržby.
9. Uložit data do JSON.
10. Načíst data při dalším spuštění a obnovit objekty.

## 🛠️ Použité technologie

- Python 3
- Objektově orientované programování (OOP)
- Dědičnost, `self`, `super()`
- Konstruktor `__init__()`
- Seznamy a slovníky
- Podmínky a cykly
- Ošetření výjimek `try/except`
- Práce se soubory
- Modul `json`

## 📂 Plánovaná struktura projektu

```text
academy-management/
│
├── main.py
├── person.py
├── student.py
├── instructor.py
├── course.py
├── payment.py
├── academy.py
├── utils.py
├── data.json
├── .gitignore
└── README.md
```

## 🗓️ Postup vývoje

### Etapa 1 – Návrh tříd
- [ ] Vytvořit rodičovskou třídu `Person`.
- [ ] Implementovat dědičnost `Student` a `Instructor`.
- [ ] Vytvořit třídy `Course`, `Payment` a `Academy`.
- [ ] Otestovat konstruktory a metody.

### Etapa 2 – Spolupráce objektů
- [ ] Přidávání studentů.
- [ ] Přidávání lektorů.
- [ ] Vytváření kurzů.
- [ ] Přiřazování lektorů.
- [ ] Přihlašování a odhlašování studentů.
- [ ] Kontrola kapacity kurzů.

### Etapa 3 – Platby
- [ ] Vytváření plateb.
- [ ] Změna stavu plateb.
- [ ] Vrácení plateb.
- [ ] Výpočet celkových tržeb.

### Etapa 4 – JSON
- [ ] Převod objektů na slovníky.
- [ ] Ukládání dat do JSON.
- [ ] Načítání dat ze souboru.
- [ ] Obnovení objektů a jejich vazeb.

### Etapa 5 – Konzolové rozhraní
- [ ] Vytvoření hlavního menu.
- [ ] Implementace jednotlivých voleb.
- [ ] Validace uživatelských vstupů.
- [ ] Ošetření chyb pomocí `try/except`.

### Etapa 6 – Rozšíření
- [ ] Vyhledávání kurzů podle názvu.
- [ ] Vyhledávání lektorů podle specializace.
- [ ] Zabránění duplicitním registracím.
- [ ] Studentské slevy a kupóny.
- [ ] Statistiky kurzů a lektorů.
- [ ] Historie přihlášení a odhlášení.

## ⚠️ Důležité technické poznámky

### Ukládání objektů do JSON

Python objekty nelze běžně ukládat přímo do JSON.

Je potřeba:

1. Převést objekty na slovníky.
2. Uložit slovníky do JSON.
3. Načíst JSON.
4. Vytvořit nové instance tříd.
5. Obnovit vzájemné vazby mezi objekty.

Při ukládání je nutné zabránit zacyklení referencí mezi studenty, kurzy a lektory. Vhodným řešením je ukládání jejich jednoznačných identifikátorů.

### Odpovědnost tříd

Každá třída by měla mít jasně definovanou odpovědnost.

- `Student` – informace o studentovi a jeho kurzech.
- `Instructor` – informace o lektorovi a jeho výuce.
- `Course` – správa účastníků a kapacity.
- `Payment` – evidence plateb.
- `Academy` – koordinace celé aplikace.

Vzájemné vztahy objektů musí zůstat konzistentní. Například přihlášení studenta do kurzu se musí projevit v evidenci kurzu i studenta.

## 🎯 Výsledek projektu

Cílem je vytvořit funkční konzolovou aplikaci, která propojuje více tříd do jednoho systému.

Projekt slouží jako praktické procvičení OOP, dědičnosti, práce s daty a návrhu větší aplikace v Pythonu.

**Stav projektu:** Ve vývoji.