#pierwszy program
print("CDV2019")
print(2)

#potega
potega = 2 ** 10
print(potega)

tekst = "CDV"
print(tekst * 2)

#pobieranie danych z klawiatury
imie = input()
print("Twoje imie podane z klawiatury: " + imie)

nazwisko = 'Nowak'
print("Twoje dane: " + imie + " " + nazwisko)

dlugosc = len(nazwisko)
print(dlugosc)

print(type(imie))
print(type(nazwisko))

wiek = input()
print("Wiek: " + wiek)

#wiekAla = 30
#wiekAla = str(wiekAla) #int converted to str
#print(type(wiekAla))
#print("Wiek Ali: " + wiekAla)

pierwszyZnak = nazwisko[0]
print(pierwszyZnak)

ostatniZnak = nazwisko[len(nazwisko) -1]
print(ostatniZnak)

ostatniZnak = nazwisko[-1]
print(ostatniZnak)

#konwersja
x = "5" * 1
print(type(x))
x = int(x)
print(type(x))

y = 4
print(type(y))
y = 4 / 2
print(type(y))
print(y)

nazwisko = "Kowalski"
print(nazwisko[0:2])
print(nazwisko[-2])
print(nazwisko[-5:])