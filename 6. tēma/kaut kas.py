import json

# ==========================================
# 1. uzdevums: Ieraksti un nolasi teksta failu
# ==========================================
with open("61_dati.txt", "w", encoding="utf-8") as f:
    f.write("Pirmā rinda\n")

with open("61_dati.txt", "r", encoding="utf-8") as f:
    print("1. uzdevums — faila 61_dati.txt saturs:")
    print(f.read())


# ==========================================
# 2. uzdevums: Salīdzini režīmus "w" un "a"
# ==========================================
# Režīms "w" pārraksta failu no sākuma — iepriekšējais saturs tiek dzēsts (rindas nekrājas).
with open("61_dati.txt", "w", encoding="utf-8") as f:
    f.write("Pirmā rinda\n")

# Režīms "a" (append) pievieno jaunus datus faila beigās — rindas krājas un to skaits aug.
with open("61_dati.txt", "a", encoding="utf-8") as f:
    f.write("Pirmā rinda\n")

with open("61_dati.txt", "r", encoding="utf-8") as f:
    print("2. uzdevums — pēc 'w' (pārraksta) un 'a' (papildina):")
    print(f.read())

# Mēģinājums atvērt neesošu failu režīmā "r" izraisa FileNotFoundError.
try:
    with open("neeksiste_fails.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("2. uzdevums — kļūda: FileNotFoundError (neesošu failu nevar atvērt režīmā 'r').\n")


# ==========================================
# 3. uzdevums: Saglabā spēles datus JSON formātā
# ==========================================
dati = {
    "vards": "Emīls",
    "punkti": 150,
    "materiali": ["koks", "akmens", "dzelzs"]
}

# Saglabā vārdnīcu failā 61_save.json ar atkāpēm (indent=4)
with open("61_save.json", "w", encoding="utf-8") as f:
    json.dump(dati, f, indent=4, ensure_ascii=False)

# Nolasa JSON failu atpakaļ un izdrukā punktus
with open("61_save.json", "r", encoding="utf-8") as f:
    ielade = json.load(f)

print("3. uzdevums — ielādētie punkti:", ielade["punkti"])

# Secinājums par indent=4:
# indent=4 formatē JSON failu ar 4 atstarpju atkāpēm katrā līmenī, padarot to cilvēkam viegli salasāmu (nevis saspiestu vienā rindā).