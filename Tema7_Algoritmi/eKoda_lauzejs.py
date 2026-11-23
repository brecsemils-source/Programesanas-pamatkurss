def aprekinat_minejumu(apaksa: int, augsa: int) -> int:
    """Aprēķina diapazona viduspunktu binārajai meklēšanai."""
    return (apaksa + augsa) // 2


def nolasit_atbildi(minejums: int) -> str:
    """Nolasa un validē lietotāja atbildi ('lielaks', 'mazaks' vai 'pareizi')."""
    atlautas_atbildes = {"lielaks", "mazaks", "pareizi"}
    while True:
        atbilde = input(
            f"Vai tavs skaitlis ir {minejums}? (lielaks/mazaks/pareizi): "
        ).strip().lower()
        if atbilde in atlatutas_atbildes:
            return atbilde
        print("Nederīga ievade! Lūdzu, raksti: lielaks, mazaks vai pareizi.")


def spelet_koda_lauzeju(apaksa: int = 1, augsa: int = 100) -> None:
    """Spēle, kur dators ar bināro meklēšanu uzmin spēlētāja skaitli."""
    if apaksa > augsa:
        print("Kļūda: sākuma apakšējā robeža nedrīkst pārsniegt augšējo.")
        return

    minejumi = 0
    print(f"Iedomājies skaitli diapazonā no {apaksa} līdz {augsa}!")

    while apaksa <= augsa:
        minejums = aprekinat_minejumu(apaksa, augsa)
        minejumi += 1

        atbilde = nolasit_atbildi(minejums)

        if atbilde == "pareizi":
            print(f"Uzvara! Dators uzminēja skaitli {minejums} {minejumi} minējumos.")
            print(
                f"Salīdzinājumam: lineārā meklēšana diapazonā {apaksa}..{augsa} "
                f"sliktākajā gadījumā prasītu {augsa - apaksa + 1} minējumus."
            )
            return
        elif atbilde == "lielaks":
            apaksa = minejums + 1
        elif atbilde == "mazaks":
            augsa = minejums - 1

    # Ja cikls beidzas, neuzminot skaitli, tas nozīmē, ka apaksa > augsa
    print("Atrasta pretruna! Iepriekšējās atbildes nav saderīgas — neviens skaitlis vairs neatbilst.")


if __name__ == "__main__":
    # Pārbaudei ar 1-1000 var nomainīt augsa = 1000
    spelet_koda_lauzeju(apaksa=1, augsa=100)