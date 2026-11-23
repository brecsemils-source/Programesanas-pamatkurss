import time

# ==========================================
# 1. UZDEVUMS: Izmēri O(1) darbību
# ==========================================
print("=== 1. UZDEVUMS: O(1) darbības mērījumi ===")

# Funkcija, kas atgriež pirmo elementu (O(1))
def iegut_pirmo(dati):
    return dati[0]

# Saraksti ar 10 un 1 000 000 elementiem
saraksts_mazs = list(range(10))
saraksts_liels = list(range(1000000))

# Laika mērīšana mazajam sarakstam
sakums_mazs = time.time()
iegut_pirmo(saraksts_mazs)
beigas_mazs = time.time()
laiks_mazs = beigas_mazs - sakums_mazs

# Laika mērīšana lielajam sarakstam
sakums_liels = time.time()
iegut_pirmo(saraksts_liels)
beigas_liels = time.time()
laiks_liels = beigas_liels - sakums_liels

print(f"Laiks ar 10 elementiem:        {laiks_mazs:.8f} s")
print(f"Laiks ar 1 000 000 elementiem: {laiks_liels:.8f} s")

print("\n" + "="*50 + "\n")


# ==========================================
# 2. UZDEVUMS: Salīdzini O(n) ar O(n²)
# ==========================================
print("=== 2. UZDEVUMS: O(n) un O(n²) salīdzinājums ===")

# Funkcija ar vienu ciklu - O(n)
def saskaitit_elementus(dati):
    kopa = 0
    for skaitlis in dati:
        kopa += skaitlis
    return kopa

# Funkcija ar diviem ligzdotiem cikliem - O(n²)
def ligzdotais_cikls(dati):
    kopa = 0
    for x in dati:
        for y in dati:
            kopa += x + y
    return kopa

# Mērīšanas palīgfunkcija
def merit_izpildi(funkcija, dati):
    sakums = time.time()
    funkcija(dati)
    beigas = time.time()
    return beigas - sakums

# Datu sagatavošana
dati_100 = list(range(100))
dati_1000 = list(range(1000))

# Mērījumi
laiks_on_100 = merit_izpildi(saskaitit_elementus, dati_100)
laiks_on2_100 = merit_izpildi(ligzdotais_cikls, dati_100)

laiks_on_1000 = merit_izpildi(saskaitit_elementus, dati_1000)
laiks_on2_1000 = merit_izpildi(ligzdotais_cikls, dati_1000)

# Pieauguma aprēķins
pieaugums_on = laiks_on_1000 / laiks_on_100 if laiks_on_100 > 0 else 0
pieaugums_on2 = laiks_on2_1000 / laiks_on2_100 if laiks_on2_100 > 0 else 0

print("100 elementi:")
print(f"  • O(n)  viena cikla laiks: {laiks_on_100:.6f} s")
print(f"  • O(n²) ligzdotā cikla laiks: {laiks_on2_100:.6f} s")

print("\n1000 elementi:")
print(f"  • O(n)  viena cikla laiks: {laiks_on_1000:.6f} s")
print(f"  • O(n²) ligzdotā cikla laiks: {laiks_on2_1000:.6f} s")

print("\nLaika pieaugums (palielinot datu apjomu 10 reizes):")
print(f"  • O(n)  laiks pieauga ~{pieaugums_on:.1f} reizes")
print(f"  • O(n²) laiks pieauga ~{pieaugums_on2:.1f} reizes")

print("\n" + "="*50 + "\n")


# ==========================================
# 3. UZDEVUMS: Nosaki sarežģītību svešam kodam
# ==========================================
print("=== 3. UZDEVUMS: Operāciju skaits un Big O ===")

# Funkcija A: Piekļuve saraksts[0] (Minējums: O(1))
def funkcija_a(saraksts):
    operacijas = 1
    rezultats = saraksts[0]
    return rezultats, operacijas

# Funkcija B: Viens cikls (Minējums: O(n))
def funkcija_b(saraksts):
    operacijas = 0
    kopa = 0
    for skaitlis in saraksts:
        operacijas += 1
        kopa += skaitlis
    return kopa, operacijas

# Funkcija C: Divi ligzdoti cikli (Minējums: O(n²))
def funkcija_c(saraksts):
    operacijas = 0
    kopa = 0
    for x in saraksts:
        for y in saraksts:
            operacijas += 1
            kopa += x + y
    return kopa, operacijas

# Testu dati
dati_10 = list(range(10))
dati_100_op = list(range(100))

# Mērījumi
_, op_a_10 = funkcija_a(dati_10)
_, op_b_10 = funkcija_b(dati_10)
_, op_c_10 = funkcija_c(dati_10)

_, op_a_100 = funkcija_a(dati_100_op)
_, op_b_100 = funkcija_b(dati_100_op)
_, op_c_100 = funkcija_c(dati_100_op)

print("Funkcija A (Minējums: O(1)):")
print(f"  • 10 elementi  -> {op_a_10} operācija")
print(f"  • 100 elementi -> {op_a_100} operācija")

print("\nFunkcija B (Minējums: O(n)):")
print(f"  • 10 elementi  -> {op_b_10} operācijas")
print(f"  • 100 elementi -> {op_b_100} operācijas")

print("\nFunkcija C (Minējums: O(n²)):")
print(f"  • 10 elementi  -> {op_c_10} operācijas")
print(f"  • 100 elementi -> {op_c_100} operācijas")