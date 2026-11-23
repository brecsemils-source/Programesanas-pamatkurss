import random

# ==========================================
# 1. UZDEVUMS: Samaini divus elementus vietām
# ==========================================
print("=== 1. UZDEVUMS: Elementu apmaiņa ===")

# Saraksta elementu apmaiņa vienā rindā
rezultati_1 = [90, 45]
print("Pirms maiņas (saraksts):", rezultati_1)

rezultati_1[0], rezultati_1[1] = rezultati_1[1], rezultati_1[0]
print("Pēc maiņas (saraksts):  ", rezultati_1)

# Parasto mainīgo apmaiņa
a, b = 90, 45
print(f"Pirms maiņas: a = {a}, b = {b}")

a, b = b, a
print(f"Pēc maiņas:  a = {a}, b = {b}")

print("\n" + "="*40 + "\n")


# ==========================================
# 2. UZDEVUMS: Burbuļa pirmais gājiens
# ==========================================
print("=== 2. UZDEVUMS: Pirmais gājiens ===")

# Saraksts ar 6 nesakārtotiem skaitļiem
rezultati_2 = [64, 34, 25, 12, 22, 11]
print("Sākotnējais saraksts:", rezultati_2)

# Viens gājiens cauri sarakstam
for i in range(len(rezultati_2) - 1):
    if rezultati_2[i] > rezultati_2[i + 1]:
        rezultati_2[i], rezultati_2[i + 1] = rezultati_2[i + 1], rezultati_2[i]

print("Pēc 1. gājiena:       ", rezultati_2)
print(f"Lielākais skaitlis nonāca beigās: {rezultati_2[-1]}")

print("\n" + "="*40 + "\n")


# ==========================================
# 3. UZDEVUMS: Pabeidz pilnu Bubble Sort
# ==========================================
print("=== 3. UZDEVUMS: Pilna Bubble Sort kārtošana ===")

# Funkcija pilnai kārtošanai ar salīdzinājumu skaitītāju
def bubble_sort(saraksts, radit_gajienus=False):
    salidzinajumi = 0
    n = len(saraksts)
    
    # Ārējais cikls
    for j in range(n):
        # Iekšējais cikls vienam gājienam
        for i in range(n - 1 - j):
            salidzinajumi += 1
            if saraksts[i] > saraksts[i + 1]:
                saraksts[i], saraksts[i + 1] = saraksts[i + 1], saraksts[i]
        
        if radit_gajienus:
            print(f"Gājiens {j + 1}: {saraksts}")
            
    return saraksts, salidzinajumi


# Tests A: 6 elementi
print("--- Tests ar 6 elementiem ---")
saraksts_6 = [64, 34, 25, 12, 22, 11]
print("Sākotnējais saraksts:", saraksts_6)
sakartots_6, salidzinajumi_6 = bubble_sort(saraksts_6.copy(), radit_gajienus=True)
print(f"Kopējais salīdzinājumu skaits (6 elem.): {salidzinajumi_6}\n")


# Tests B: 10 elementi
print("--- Tests ar 10 elementiem ---")
saraksts_10 = [random.randint(1, 100) for _ in range(10)]
print("Sākotnējais saraksts:", saraksts_10)
sakartots_10, salidzinajumi_10 = bubble_sort(saraksts_10.copy(), radit_gajienus=False)
print("Sakārtotais saraksts: ", sakartots_10)
print(f"Kopējais salīdzinājumu skaits (10 elem.): {salidzinajumi_10}")