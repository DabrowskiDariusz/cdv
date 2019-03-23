tekst = "Anna, Paweł, tomEk"

tab = tekst.split(", ")
print(tekst)
print(tab)

print(tab[0])
print("Twoje imie: " + tab[1])

imieDuze = tab[0].upper()
print(imieDuze)

imieMale = tab[1].lower()
print(imieMale)

#sprawdzenie zawartosci
zawartosc = tab[0].isalpha()
print(zawartosc)
print(type(zawartosc))

imie = ""
zawartosc = imie.isalpha()
print(zawartosc)

print("Dane użytkownika: \n" + tab[0])

text1 = "Jan\n"
text2 = "Nowak"
print(text1 + text2)
text1 = text1.rstrip()
print(text1 + text2)

#wyswietlanie lancuchow znakow

#wszystkie wersje pythona

text = "%s, Java i %s" % ("PHP", "Python")
print(text)

#nowsze wersje pythona 2.6 i 3+
text = "{0}, Java i {1}".format("PHP", "Python")
print(text)

#help(text.replace)

new = text.replace("PHP", "C#")
print(new)

#wypisywanie danych
rok = "2015"
miesiac = "marzec"
dzien = "23"

print("Data: ", "end=""")