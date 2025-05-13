# Oblíbená jídla
jídla = ["měď", "guma", "hliník"]
print(jídla)


# Známky
známky = [4, 3, 4, 5, 4]
print(známky)


# Zvířata
zvířata = ["ferda", "mravenec", "pytlík", "brouk"]
print(zvířata[1])
print(zvířata[-1])


# Prázdný seznam + .append
kabely = []
kabely.append(230)
kabely.append(12)
kabely.append(7)
print(kabely)


# Oblíbené filmy s výpisem
filmy = ["Drát 1", "Šroubovák: Návrat", "Typy šroubů"]
for film in filmy:
    print(film)


# Změna čísla
cisla = [13, 21, 34]
cisla[1] = 999
print(cisla)


# Součet čísel
soucastky = [1, 2, 3, 4, 5]
print(sum(soucastky))


# Velikost pole
materialy = ["meloun", "rejže", "J.K. Rowlingová", "pšenice"]
print(len(materialy))


# Průměr známek
znamky = [4, 3, 4, 5, 4]
prumer = sum(znamky) / len(znamky)
print("Průměr známek:", prumer)


# Hledání banánu
ovoce = ["plech", "šroub", "banán", "matice"]
if "banán" in ovoce:
    print("Banán tam je!")
else:
    print("Banán tam není.")


# Seznam libovolných 6 čísel
cisla = [4, 15, 9, 22, 3, 11]

# Proměnná pro počet čísel větších než 10
pocet_vetsich_nez_10 = 0

# Procházení seznamu pomocí cyklu
for cislo in cisla:
    if cislo > 10:
        pocet_vetsich_nez_10 += 1

# Výpis výsledku
print("Počet čísel větších než 10:", pocet_vetsich_nez_10)


# Vytvoření prázdného pole pro známky
známky2 = []

# Načtení počtu známek od uživatele
pocet_znamek = int(input("Kolik známek chceš zadat? "))

# Použití for cyklu podle zadaného počtu
for i in range(pocet_znamek):
    #  Načtení známky od uživatele
    znamka = float(input(f"Zadej známku číslo {i + 1}: "))
    
    # Přidání známky do pole
    známky2.append(znamka)

# Výpočet a výpis průměru
prumer = sum(známky2) / len(známky2)
print("Průměr zadaných známek je:", prumer)
