x = float(input("Anna leiviskät: "))
y = float(input("Anna naulat: "))
z = float(input("Anna luodit: "))

Luoti = 13.3
Naula = 13.3 * 32
Leiviska = Naula * 20

Luodit = z * Luoti
Naulat = y * Naula
Leiviskat = x * Leiviska
Yht = Luodit + Naulat + Leiviskat

Kilogramma = Yht / 1000
Kilogramma = int(Kilogramma)
Grammat = Yht % 1000
Grammat = round(Grammat, 2)

print(f"Massa nyky mittojen mukaan: {Kilogramma} Kilogrammaa ja {Grammat} grammaa.")