import random

# ==========================================
# 1. FUNKCIJU DEFINĪCIJAS
# ==========================================

# 1. uzdevums & 3. uzdevums: Lineārā meklēšana ar soļu skaitīšanu
def linear_search(saraksts, mekletais):
    soli = 0  # 1. Pievieno skaitītāju soli = 0
    for i, elements in enumerate(saraksts):
        soli += 1  # 2. Palielini katrā cikla iterācijā
        if elements == mekletais:
            return i, soli  # 3. Atgriez gan indeksu, gan soļu skaitu
    return -1, soli


# 2. uzdevums & 3. uzdevums: Binārā meklēšana ar soļu skaitīšanu
def binary_search(saraksts, mekletais):
    soli = 0  # 1. Pievieno skaitītāju soli = 0
    apaksa = 0
    augsa = len(saraksts) - 1
    
    while apaksa <= augsa:
        soli += 1  # 2. Palielini katrā cikla iterācijā
        vidus = (apaksa + augsa) // 2
        
        if saraksts[vidus] == mekletais:
            return vidus, soli  # 3. Atgriez gan indeksu, gan soļu skaitu
        elif saraksts[vidus] < mekletais:
            apaksa = vidus + 1
        else:
            augsa = vidus - 1
            
    return -1, soli


# ==========================================
# 2. TESTĒŠANAS FUNKCIJA
# ==========================================

def testet_meklesanu(saraksta_lielums):
    # Izveido un sakārto sarakstu
    saraksts = sorted([random.randint(1, 10000) for _ in range(saraksta_lielums)])
    
    # Izvēlas pēdējo elementu (sliktākais gadījums lineārajai meklēšanai)
    mekletais = saraksts[-1]
    
    _, soli_lin = linear_search(saraksts, mekletais)
    _, soli_bin = binary_search(saraksts, mekletais)
    
    return soli_lin, soli_bin


# ==========================================
# 3. KODA IZPILDE UN REZULTĀTI
# ==========================================

# 4. Tests ar 20 elementiem
soli_20_lin, soli_20_bin = testet_meklesanu(20)

# 5. Tests ar 1000 elementiem
soli_1000_lin, soli_1000_bin = testet_meklesanu(1000)

# Rezultātu izvade terminālī
print("=== TESTA REZULTĀTI ===")
print(f"20 elementi   -> Lineārā: {soli_20_lin} soļi | Binārā: {soli_20_bin} soļi")
print(f"1000 elementi -> Lineārā: {soli_1000_lin} soļi | Binārā: {soli_1000_bin} soļi")