# 🎓 Academy Management System

Konzolová aplikace v jazyce **Python** pro správu vzdělávací akademie zaměřené na programování, umělou inteligenci a kancelářské aplikace.

**Verze:** 1.0  
**Obtížnost:** 4/5  
**Technologie:** Python 3, OOP, JSON  
**Uživatelské rozhraní:** Konzole

---

## 1. Cíl projektu

Vytvořit funkční aplikaci umožňující:

- Evidovat studenty a lektory.
- Vytvářet kurzy a přiřazovat k nim lektory.
- Přihlašovat a odhlašovat studenty z kurzů.
- Kontrolovat kapacitu jednotlivých kurzů.
- Evidovat platby a měnit jejich stav.
- Vypočítávat celkové tržby akademie.
- Automaticky ukládat a načítat data pomocí JSON.

Program bude rozdělen do samostatných modulů. Všechny názvy tříd, metod, atributů a proměnných budou v angličtině. Konzolové rozhraní bude v češtině.

## 2. Struktura projektu

```text
academy-management/
│
├── main.py
├── academy.py
├── person.py
├── student.py
├── instructor.py
├── course.py
├── payment.py
├── utils.py
├── prompt.py
├── data.json
├── .gitignore
└── README.md
```

## 3. Návrh tříd

### 3.1 Person

Rodičovská třída pro studenty a lektory.

**Atributy:**
- `name`
- `email`
- `phone`

**Metody:**
- `get_info()` – vrátí slovník s informacemi o osobě.
- `change_email(new_email)` – změní e-mailovou adresu.

**Pravidla:**
- Při úspěšné změně e-mailu vrátí `True`.
- Při prázdném e-mailu vrátí `False`.

### 3.2 Student(Person)

Třída dědící ze třídy `Person`.

**Atributy:**
- `student_id` – jedinečné kladné celé číslo.
- `courses` – seznam objektů `Course`.

**Metody:**
- `get_info()` – rozšíří informace rodičovské třídy.
- `enroll_in_course(course)` – přidá kurz studentovi.
- `remove_course(course)` – odebere kurz studentovi.
- `get_courses()` – vrátí seznam studentových kurzů.

**Pravidla:**
- Student může být přihlášen do více kurzů.
- Stejný kurz nesmí mít v seznamu dvakrát.
- Metody přidání a odebrání vracejí `True` při úspěchu, jinak `False`.

### 3.3 Instructor(Person)

Třída dědící ze třídy `Person`.

**Atributy:**
- `specialization`
- `hourly_rate` – nezáporné číslo.
- `courses` – seznam objektů `Course`.

**Metody:**
- `get_info()` – rozšíří informace rodičovské třídy.
- `assign_course(course)` – přiřadí kurz lektorovi.
- `get_courses()` – vrátí seznam vyučovaných kurzů.

**Pravidla:**
- Jeden lektor může vyučovat více kurzů.
- Každý kurz má právě jednoho lektora.
- Kurz se nesmí v seznamu lektora opakovat.

### 3.4 Course

Třída reprezentující vzdělávací kurz.

**Atributy:**
- `course_id` – jedinečné kladné celé číslo.
- `name`
- `price` – nezáporné číslo.
- `capacity` – kladné celé číslo.
- `instructor` – objekt `Instructor`.
- `students` – seznam objektů `Student`.

**Metody:**
- `add_student(student)` – přidá studenta do kurzu.
- `remove_student(student)` – odebere studenta z kurzu.
- `get_students()` – vrátí seznam studentů.
- `available_slots()` – vrátí počet volných míst.

**Pravidla:**
- Počet studentů nesmí překročit kapacitu.
- Student nesmí být přihlášen dvakrát.
- Pokud je kurz plný, přihlášení se neprovede.
- Při úspěšném přidání nebo odebrání se vrací `True`, jinak `False`.
- Počet volných míst je `capacity - len(students)`.

### 3.5 Payment

Třída reprezentující platbu za kurz.

**Atributy:**
- `payment_id` – jedinečné kladné celé číslo.
- `student` – objekt `Student`.
- `course` – objekt `Course`.
- `amount` – kladné číslo.
- `date` – datum platby.
- `status` – stav platby.

**Povolené stavy:**
- `pending` – čeká na úhradu.
- `paid` – zaplaceno.
- `refunded` – vráceno.

**Metody:**
- `process_payment()` – změní stav z `pending` na `paid`.
- `refund_payment()` – změní stav z `paid` na `refunded`.
- `get_payment()` – vrátí informace o platbě.

**Pravidla:**
- Nová platba má stav `pending`.
- Zaplatit lze pouze platbu ve stavu `pending`.
- Vrátit lze pouze zaplacenou platbu.
- Neplatná změna stavu vrátí `False`.
- Pro jednu dvojici student–kurz může existovat nejvýše jedna platba.
- Datum se eviduje ve formátu `YYYY-MM-DD`.

### 3.6 Academy

Hlavní řídicí třída aplikace.

**Atributy:**
- `name`
- `students`
- `instructors`
- `courses`
- `payments`

Všechny kolekce jsou při vytvoření akademie prázdné seznamy.

**Metody:**
- `add_students(student)` – přidá studenta.
- `add_instructor(instructor)` – přidá lektora.
- `create_courses(course)` – přidá kurz.
- `find_student(email)` – vyhledá studenta podle e-mailu.
- `find_instructor(email)` – vyhledá lektora podle e-mailu.
- `find_course(name)` – vyhledá kurz podle názvu.
- `enroll_student(student, course)` – přihlásí studenta.
- `remove_student_from_course(student, course)` – odhlásí studenta.
- `show_courses()` – vrátí seznam kurzů.
- `show_revenue()` – vrátí celkové tržby.

**Pravidla:**
- Vyhledávací metody vracejí nalezený objekt nebo `None`.
- Akademie spravuje vztahy mezi jednotlivými objekty.
- Přihlášení a odhlášení musí aktualizovat seznamy na obou stranách.
- Tržby zahrnují pouze platby se stavem `paid`.

## 4. Propojení objektů

### 4.1 Přiřazení lektora ke kurzu

Lektor se přiřazuje přímo při vytváření kurzu.

**Postup:**
1. Uživatel zadá název, cenu a kapacitu kurzu.
2. Zadá e-mail existujícího lektora.
3. Aplikace vyhledá objekt `Instructor`.
4. Pokud lektor neexistuje, vytvoření se zruší.
5. Pokud existuje, vytvoří se objekt `Course`.
6. Kurz se přidá do `academy.courses`.
7. Kurz se přidá do `instructor.courses`.

Kurz bez lektora nelze vytvořit. Změna lektora později není požadována.

### 4.2 Přihlášení studenta do kurzu

**Postup:**
1. Uživatel zadá e-mail studenta.
2. Zadá název kurzu.
3. Aplikace vyhledá oba objekty.
4. Zkontroluje, zda student již není přihlášen.
5. Zkontroluje volnou kapacitu.
6. Přidá studenta do `course.students`.
7. Přidá kurz do `student.courses`.

Pokud přihlášení selže, žádný ze seznamů se nesmí změnit.

### 4.3 Odhlášení studenta z kurzu

**Postup:**
1. Uživatel zadá e-mail studenta.
2. Zadá název kurzu.
3. Aplikace ověří existenci studenta a kurzu.
4. Ověří, zda je student přihlášen.
5. Odebere studenta z `course.students`.
6. Odebere kurz z `student.courses`.

Odhlášení nemění stav existující platby.

## 5. Konzolové menu

```text
========================================
           AKADEMICKÝ SYSTÉM
========================================

[1]  Přidat studenta
[2]  Přidat lektora
[3]  Vytvořit kurz
[4]  Přihlásit studenta na kurz
[5]  Odhlásit studenta z kurzu
[6]  Zobrazit všechny kurzy
[7]  Zobrazit studenty
[8]  Zobrazit lektory
[9]  Zobrazit platby
[10] Vytvořit platbu
[11] Uhradit platbu
[12] Vrátit platbu
[13] Zobrazit celkové tržby

[Q]  Ukončit program
```

### 5.1 Přidat studenta

Načte jméno, e-mail, telefon a ID. Vytvoří objekt `Student` a přidá jej do akademie.

### 5.2 Přidat lektora

Načte jméno, e-mail, telefon, specializaci a hodinovou sazbu. Vytvoří objekt `Instructor`.

### 5.3 Vytvořit kurz

Načte název, cenu, kapacitu a e-mail lektora. Vytvoří kurz a propojí ho s lektorem.

### 5.4 Přihlásit studenta na kurz

Vyhledá studenta a kurz. Provede přihlášení při splnění podmínek.

### 5.5 Odhlásit studenta z kurzu

Vyhledá studenta a kurz. Odebere jejich vzájemné propojení.

### 5.6 Zobrazit všechny kurzy

Zobrazí název, cenu, kapacitu, počet přihlášených, počet volných míst, jméno lektora a studenty.

### 5.7 Zobrazit studenty

Zobrazí jméno, e-mail, telefon, ID a názvy přihlášených kurzů.

Pokud student nemá žádný kurz, zobrazí `Žádný`.

### 5.8 Zobrazit lektory

Zobrazí jméno, e-mail, telefon, specializaci, hodinovou sazbu a názvy vyučovaných kurzů.

### 5.9 Zobrazit platby

Zobrazí studenta, kurz, částku, datum a stav každé platby.

### 5.10 Vytvořit platbu

Vyhledá studenta a kurz. Student musí být přihlášen do daného kurzu.

Částka odpovídá ceně kurzu. Nová platba má stav `pending` a aktuální datum.

### 5.11 Uhradit platbu

Vyhledá platbu podle ID a změní její stav z `pending` na `paid`.

### 5.12 Vrátit platbu

Vyhledá platbu podle ID a změní její stav z `paid` na `refunded`.

### 5.13 Zobrazit celkové tržby

Sečte částky všech plateb se stavem `paid`.

Platby `pending` a `refunded` se nezapočítávají.

Pokud nejsou žádné zaplacené platby, tržby jsou `0`.

## 6. Automatické ukládání a načítání JSON

Veškerá data aplikace budou uložena v jediném souboru `data.json`.

**Ukládání a načítání nebude součástí konzolového menu.**

### 6.1 Automatické načítání

Při spuštění programu:

1. Aplikace ověří existenci `data.json`.
2. Pokud soubor existuje, načte jeho obsah.
3. Vytvoří instance tříd `Student`, `Instructor`, `Course` a `Payment`.
4. Obnoví vzájemné vazby mezi objekty.
5. Pokud soubor neexistuje, vytvoří prázdnou akademii.

Pokud soubor obsahuje neplatný JSON nebo neplatná data, aplikace oznámí chybu a nesmí automaticky přepsat poškozený soubor prázdnými daty.

### 6.2 Automatické ukládání

Při běžném ukončení programu:

1. Aplikace převede objekty na slovníky.
2. Připraví data pro JSON.
3. Uloží všechna data do `data.json`.
4. Ukončí program.

Pro verzi 1.0 postačuje ukládání při běžném ukončení. Automatické ukládání po každé změně je možné budoucí rozšíření.

### 6.3 Struktura JSON

JSON bude obsahovat:
- Název akademie.
- Studenty.
- Lektory.
- Kurzy.
- Platby.

Vzájemné vazby se ukládají pomocí identifikátorů, nikoliv přímým ukládáním objektů.

**Pravidla:**
- Kurz odkazuje na lektora pomocí jeho e-mailu.
- Kurz obsahuje ID přihlášených studentů.
- Platba obsahuje ID studenta a ID kurzu.
- Při načítání se všechny vazby znovu vytvoří.

## 7. Validace a chybové stavy

Pro dokončení verze 1.0 platí:

- Student nesmí mít duplicitní ID ani e-mail.
- Lektor nesmí mít duplicitní e-mail.
- Kurz nesmí mít duplicitní ID ani název.
- Platba nesmí mít duplicitní ID.
- ID musí být kladné celé číslo.
- Kapacita kurzu musí být alespoň `1`.
- Cena a hodinová sazba nesmí být záporné.
- Prázdné povinné textové údaje nejsou povoleny.
- Neplatný číselný vstup nesmí způsobit pád programu.
- Pokud student, lektor, kurz nebo platba neexistují, aplikace zobrazí oznámení.
- Neúspěšná operace nesmí poškodit existující data.

Validaci a kontroly duplicit lze doplnit až po zprovoznění základní funkcionality.

## 8. Testovací scénář

### Testovací studenti

| ID | Jméno |
|---|---|
| 1 | Petr Novák |
| 2 | Jana Svobodová |
| 3 | Tomáš Malý |

### Testovací lektoři

| Jméno | Specializace |
|---|---|
| Martin Dvořák | Python |
| Eva Černá | Umělá inteligence |

### Testovací kurzy

| Kurz | Cena | Kapacita | Lektor |
|---|---:|---:|---|
| Python OOP | 5 000 Kč | 2 | Martin Dvořák |
| AI v praxi | 3 000 Kč | 3 | Eva Černá |

### Povinné testy

1. Přidat tři studenty.
2. Přidat dva lektory.
3. Vytvořit oba kurzy a přiřadit lektory.
4. Přihlásit Petra a Janu na Python OOP.
5. Pokusit se přihlásit Tomáše na plný kurz. Operace musí být odmítnuta.
6. Přihlásit Tomáše na AI v praxi.
7. Ověřit propojení studentů, kurzů a lektorů.
8. Odhlásit Janu z Python OOP.
9. Přihlásit Tomáše na uvolněné místo.
10. Vytvořit platbu Petra za Python OOP.
11. Vytvořit platbu Tomáše za AI v praxi.
12. Označit obě platby jako zaplacené.
13. Ověřit celkové tržby 8 000 Kč.
14. Vrátit Tomášovu platbu.
15. Ověřit nové tržby 5 000 Kč.
16. Ukončit program a automaticky uložit data.
17. Znovu spustit program.
18. Ověřit automatické načtení všech dat a obnovení vztahů mezi objekty.

## 9. Etapy vývoje

### Etapa 1 – Základní OOP

- [ ] Dokončit `Person`.
- [ ] Dokončit `Student`.
- [ ] Dokončit `Instructor`.
- [ ] Dokončit `Course`.
- [ ] Dokončit `Academy`.

### Etapa 2 – Spolupráce objektů

- [ ] Přidávání studentů a lektorů.
- [ ] Vytváření kurzů.
- [ ] Přiřazování lektorů.
- [ ] Přihlašování studentů.
- [ ] Odhlašování studentů.
- [ ] Zobrazování informací.

### Etapa 3 – Platby

- [ ] Vytváření plateb.
- [ ] Změna stavu na zaplaceno.
- [ ] Vrácení platby.
- [ ] Výpočet tržeb.

### Etapa 4 – JSON

- [ ] Převod objektů na slovníky.
- [ ] Automatické načítání při spuštění.
- [ ] Automatické ukládání při ukončení.
- [ ] Obnovení vztahů mezi objekty.

### Etapa 5 – Dokončení

- [ ] Kontrola duplicit.
- [ ] Validace uživatelských vstupů.
- [ ] Ošetření chyb.
- [ ] Otestování všech funkcí.
- [ ] Aktualizace dokumentace.

## 10. Programátorská pravidla

- Používat objektově orientované programování.
- Každá hlavní třída bude v samostatném souboru.
- Využívat dědičnost a `super()`.
- Jednotlivé třídy budou spolupracovat prostřednictvím objektů.
- V metodách tříd nepoužívat `input()` ani `print()`.
- Konzolové rozhraní bude oddělené od aplikační logiky.
- Pro práci se soubory používat modul `json`.
- Data budou uložená v jednom souboru.
- Program bude verzovaný pomocí Git a GitHub.

## 11. Podmínky dokončení

Projekt bude považován za dokončený, pokud:

- [ ] Všech 13 položek menu funguje.
- [ ] Studenti, lektoři a kurzy jsou správně propojeni.
- [ ] Kapacita kurzů je dodržována.
- [ ] Platby správně mění svůj stav.
- [ ] Celkové tržby se počítají správně.
- [ ] Data se automaticky ukládají při ukončení.
- [ ] Data se automaticky načítají při spuštění.
- [ ] Po načtení jsou obnoveny všechny vztahy mezi objekty.
- [ ] Program zvládá běžné chybné vstupy.
- [ ] Všechny povinné testy proběhnou úspěšně.

---

**Výsledek projektu:** Plně funkční konzolový systém pro správu vzdělávací akademie s využitím OOP, dědičnosti, spolupráce objektů a automatického ukládání dat do JSON.