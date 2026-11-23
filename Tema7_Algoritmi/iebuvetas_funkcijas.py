import time

# --- 1. UZDEVUMS: Atrodi min un max ar iebūvētajām funkcijām ---
print("--- 1. UZDEVUMS ---")
ienaidnieku_hp = [45, 12, 89, 33, 78, 9, 56, 92, 24, 67]

vajakais = min(ienaidnieku_hp)
stiprakais = max(ienaidnieku_hp)

print(f"Vajakais ienaidnieks (min): {vajakais}")
print(f"Stiprakais ienaidnieks (max): {stiprakais}")

# Pasa rakstits cikls mazakajai vertibai bez min()
maka_vertiba_cikls = ienaidnieku_hp[0]
for hp in ienaidnieku_hp:
  if hp < maka_vertiba_cikls:
    maka_vertiba_cikls = hp

print(f"Mazaka vertiba, izmantojot savu ciklu: {maka_vertiba_cikls}")
print(f"Vai rezultati sakrit? {maka_vertiba_cikls == vajakais}")


# --- 2. UZDEVUMS: Salīdzini iebūvēto sum() ar savu ciklu ---
print("\n--- 2. UZDEVUMS ---")
dati = list(range(1000000))


def saskaitit_ar_ciklu(saraksts):
  summa = 0
  for skaitlis in saraksts:
    summa += skaitlis
  return summa


def saskaitit_ar_iebuveto(saraksts):
  return sum(saraksts)


rezultats_cikls = saskaitit_ar_ciklu(dati)
rezultats_iebuvets = saskaitit_ar_iebuveto(dati)

print(f"Cikla summa: {rezultats_cikls}")
print(f"Iebuveta sum() summa: {rezultats_iebuvets}")
print(f"Vai rezultati ir vienadi? {rezultats_cikls == rezultats_iebuvets}")


# --- 3. UZDEVUMS: Izmēri abus ar time un izdari secinājumu ---
print("\n--- 3. UZDEVUMS ---")

# Meram cikla laiku
sakuma_laiks_cikls = time.time()
rezultats_cikls = saskaitit_ar_ciklu(dati)
beigu_laiks_cikls = time.time()
laiks_cikls = beigu_laiks_cikls - sakuma_laiks_cikls

# Meram sum() laiku
sakuma_laiks_sum = time.time()
rezultats_iebuvets = saskaitit_ar_iebuveto(dati)
beigu_laiks_sum = time.time()
laiks_sum = beigu_laiks_sum - sakuma_laiks_sum

# Izdrukojam ar :.4f formatejumu
print(f"Pasa cikla izpildes laiks: {laiks_cikls:.4f} sekundes")
print(f"Iebuvetas sum() laiks: {laiks_sum:.4f} sekundes")

# Aprekinam, cik reizes atraka bija iebuveta funkcija
if laiks_sum > 0:
  paatrinajums = laiks_cikls / laiks_sum
  print(f"Iebuveta funkcija bija apmeram {paatrinajums:.1f} reizes atraka.")

print(
    "\nSecinajums: Abiem algoritmiem ir O(n) sarezgiba, jo tie iziet cauri"
    " sarakstam vienu reizi[cite: 5]. Tomēr iebūvētā funkcija darbojas C"
    " valodas līmenī, tāpēc tā izpildās ievērojami ātrāk nekā Python for cikls"
    "[cite: 2, 5]."
)