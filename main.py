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
