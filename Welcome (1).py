# Zadanie 1
# Napisz program, który policzy deltę dla równania kwadratowego:
# Wyświetl wynik w konsoli.

#Rozwiązanie:
a=3
b=-4
c=1
delta=b**2-4*a*c
print(f'Delta wynosi: {delta}')


# Zadanie 2
# Do kolejnych zmiennych (x1,x2,x3 oraz x4) przypisz następujące
# wartości:
# - znak nowej linii,
# - znak tabulatora
# - znak \ (backslash)
# - cudzysłów
# Wszystkie zmienne wydrukuj w jednej linii (przy użyciu
# formatowania f-string) w konsoli z poprzedzającą informacją o znaku.
# Oczekiwany wynik
# koniec linii:
# tabulator: backslash:\ cudzysłów:"

# Rozwiązanie:
x1='\n'
x2="\t"
x3="\\"
x4="\""
print(f"koniec linii:{x1} tabulator:{x2}
backslash:{x3} cudzysłów:{x4}")


# Zadanie 3
# Dana jest nazwa pliku przypisana do zmiennej nazwa:
# nazwa="plik1.jpg"
# Wytnij z tej nazwy rozszerzenie (z kropką) i wyświetl go w konsoli
# Oczekiwany rezultat:
# .jpg

# Rozwiązanie 1:
nazwa="plik1.jpg"
print(nazwa[-4:])

# Rozwiązanie 2:
nazwa="plik1.jpg"
print(nazwa[5:])


# Zadanie 4
# Wyznacz środek odcinka o końcach w punktach:
# A = (2, 4),
# B = (-4, 6).
# Oczekiwany wynik:
# Środek odcinka AB: (-1.0, 5.0)

# Rozwiązanie:
x1=2
y1=4
x2=-4
y2=6
s1=(x1+x2)/2
s2=(y1+y2)/2
print(f'Środek odcinka AB: ({s1}, {s2})')


# Zadanie 5
# Napisz program, który wyznaczy wszystkie liczby dwucyfrowe
# podzielne przez 7. Wynik wydrukuj do konsoli w postaci jednego
# łańcucha zawierającego wartości rozdzielone przecinkami.
# Oczekiwany rezultat:
# 14,21,28,35,42,49,56,63,70,77,84,91,98

# Rozwiązanie:
wynik=[]
for x in range(10,100):
if x%7==0:
wynik.append(str(x))
print(",".join(wynik))


# Zadanie 6
# Wygeneruj ciąg arytmetyczny skończony, w którym pierwszy wyraz
# jest równy 0, ostatni wyraz nie jest większy niż 100, natomiast różnica
# w tym ciągu wynosi 3. Zapisz ciąg w liście oraz wydrukuj tę listę w
# konsoli.
# Oczekiwany rezultat:
# [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33,
# 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69,
# 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]

# Rozwiązanie:
lista=[]
for x in range(0,100,3):
lista.append(x)
print(lista)


# Zadanie 7
# Napisz program, który utworzy histogram - rozkład częstości w
# postaci słownika liter przechowywanych w liście:
# lista=['x','y','z','y','x','y','y','z','x']
# W odpowiedzi utworzony słownik wydrukuj do konsoli.
# Oczekiwany wynik:
# {'x': 3, 'y': 4, 'z': 2}

# Rozwiązanie:
lista=['x','y','z','y','x','y','y','z','x']
slownik={}
for litera in lista:
if litera not in slownik.keys():
slownik[litera] = 1
else:
slownik[litera] += 1
print(slownik)


# Zadanie 8
# Podana jest niepełna lista imion (jednego brak):
# lista=['Jacek','Tomek','Monika',None,'Barbara']
# Lista składa się tylko z obiektów typu str lub wartości None.
# Posługując się instrukcją for oraz poleceniem continue wydrukuj do
# konsoli tylko poprawnie przekazane imiona (obiekty typu str).
# Oczekiwany rezultat:
# Jacek
# Tomek
# Monika
# Barbara

# Rozwiązanie:
lista=['Jacek','Tomek','Monika',None,'Barbara']
for name in names:
if name is None:
continue
print(name)


# Zadanie 9
# Dane są następujące zmienne:
# x1=None
# x2=False
# x3='False'
# x4=0
# x5=100
# x6=""
# x7="ABC"
# Przy użyciu formatowania f-string wyświetl informacje o wartościach
# logicznych reprezentowanych przez te wartości.
# Oczekiwany wynik:
# Wartość logiczna x1 to False.
# Wartość logiczna x2 to False.
# Wartość logiczna x3 to True.
# Wartość logiczna x4 to False.
# Wartość logiczna x5 to True.
# Wartość logiczna x6 to False.
# Wartość logiczna x7 to True.

# Rozwiązanie:
x1=None
x2=False
x3='False'
x4=0
x5=100
x6=""
x7="ABC"
print(f"Wartość logiczna x1 to {bool(x1)}.")
print(f"Wartość logiczna x2 to {bool(x2)}.")
print(f"Wartość logiczna x3 to {bool(x3)}.")
print(f"Wartość logiczna x4 to {bool(x4)}.")
print(f"Wartość logiczna x5 to {bool(x5)}.")
print(f"Wartość logiczna x6 to {bool(x6)}.")
print(f"Wartość logiczna x7 to {bool(x7)}.")


# Zadanie 10
# Dane są poniższe kody:
# kod1='AKRTB-20'
# kod2='AKRTB20'
# Używając odpowiedniej metody sprawdź czy kody składają się tylko
# ze znaków alfanumerycznych (cyfry + litery). Wynik wydrukuj do
# konsoli tak jak pokazano poniżej.
# Oczekiwany wynik:
# Kod 1: False
# Kod 2: True

# Rozwiązanie:
kod1='AKRTB-20'
kod2='AKRTB20'
print(f'Kod 1: {kod1.isalnum()}')
print(f'Kod 2: {kod2.isalnum()}')


# Zadanie 11
# Dana jest zmienna napis:
# napis=" Python "
# Wydrukuj w konsoli ten łańcuch (z dopiskiem przed łańcuchem:
# „Napis zmieniony:”) z uwzględnieniem następujących modyfikacji:
# - tylko wielkie litery,
# - tylko małe litery,
# - bez spacji z dwóch stron
# - bez spacji z lewej strony
# - bez spacji z prawej strony
# - bez spacji z dwóch stron oraz zapisany małymi literami
# Oczekiwany wynik:
# Napis zmieniony: PYTHON .
# Napis zmieniony: python .
# Napis zmieniony:Python.
# Napis zmieniony:Python .
# Napis zmieniony: Python.
# Napis zmieniony:python.

# Rozwiązanie:
napis=" Python "
print(f"Napis zmieniony:{napis.upper()}.")
print(f"Napis zmieniony:{napis.lower()}.")
print(f"Napis zmieniony:{napis.strip()}.")
print(f"Napis zmieniony:{napis.lstrip()}.")
print(f"Napis zmieniony:{napis.rstrip()}.")
print(f"Napis zmieniony:{(napis.strip()).
lower()}.")


# Zadanie 12
# Dana jest zmienna zdanie, która przechowuje dowolny łańcuch
# tekstowy. Napisz program, który wyświetla w konsoli jeden z dwóch
# poniższych komunikatów w zależności od tego, czy zdanie
# rozpoczyna się od wyrazu: "Programowanie":
# Pierwszy wyraz to: 'Programowanie'
# Inny wyraz na początku zdania"

# Rozwiązanie:
zdanie="Programowanie w języku Python"
if zdanie.startswith("Programowanie "):
print("Pierwszy wyraz to:'Programowanie'")
else:
print("Inny wyraz na początku zdania")


# Zadanie 13
# Dana jest zmienna zdanie, która przechowuje dowolny łańcuch
# tekstowy. Napisz program, który wyświetla w konsoli jeden z
# poniższych komunikatów w zależności od tego, czy zdanie kończy się
# od wyrazem: "Python":
# Ostatni wyraz to:'Python'
# Inny wyraz na początku zdania

# Rozwiązanie:
zdanie="Programowanie w języku Python."
if zdanie.endswith(" Python") or
zdanie.endswith(" Python.");
print("Ostatni wyraz to:'Python'")
else:
print("Inny wyraz na końcu zdania")


# Zadanie 14
# Dane są zmienne:
# napis="cena produktu: "
# cena=12.50
# Połącz te dane w jeden napis (wykonaj konkatenację) i wynik
# wyświetl w konsoli.
# Oczekiwany wynik:
# cena produktu: 12.5

# Rozwiązanie 1:
napis="cena produktu: "
cena=12.50
print(napis+str(cena))

# Rozwiązanie 2:
napis="cena produktu: "
cena=12.50
print(napis,cena)


# Zadanie 15
# Dana jest zmienna kod:
# kod='237-192-45-45'
# Usuń dywizy z tego zapisu. Wynik zapisz w zmiennej o takiej samej
# nazwie (kod). Następnie otrzymany łańcuch wydrukuj w konsoli.
# Oczekiwany wynik:
# 2371924545

# Rozwiązanie:
kod='237-192-45-45'
kod=kod.replace("-","")
print(kod)


# Zadanie 16
# Zlicz liczbę wystąpień litery P w zdaniu przechowywanym w
# zmiennej zdanie:
# zdanie="Programowanie w języku Python"
# Następnie korzystając z formatowania f-string wyświetl w konsoli
# komunikat (podstawiając otrzymany wynik):
# Liczba wystąpień litery P: 2

# Rozwiązanie:
zdanie="Programowanie w języku Python"
print(f"Liczba wystąpień litery P:
{zdanie.count('P')}")


# Zadanie 17
# Dana jest zmienna owoce przechowująca łańcuch tekstowy:
# owoce="Jabłko,Banan,Śliwka,Pomidor"
# Używając odpowiedniej metody podziel tekst na wyrazy i umieść je w
# liście. Zawartość tej listy wydrukuj w konsoli.
# Oczekiwany wynik:
# ['Jabłko', 'Banan', 'Śliwka', 'Pomidor']

# Rozwiązanie:
owoce="Jabłko,Banan,Śliwka,Pomidor"
lista=owoce.split(",")
print(lista)


# Zadanie 18
# Dany jest zbiór:
# owoce={'jabłko','gruszka'}
# Używając odpowiedniej metody dodaj do tego zbioru kolejny
# elementy: śliwka oraz czereśnia.
# Używając odpowiedniej metody usuń element: jabłko
# Wydrukuj w konsoli zwartość zbioru po tych operacjach oraz
# informację o liczbie owoców (poprzedzoną napisem: Liczba
# owoców).
# Oczekiwany wynik:
# {'czereśnia', 'śliwka', 'gruszka'}
# Liczba owoców: 3

# Rozwiązanie:
owoce={"jabłko","gruszka"}
owoce.add("śliwka")
owoce.add("czereśnia")
owoce.remove("jabłko")
print(owoce)
print(f"Liczba owoców: {len(owoce)}")


# Zadanie 19
# Dany jest następujący łańcuch tekstowy przechowywany w zmiennej
# napis:
# napis="Programowanie w języku Python"
# Usuń z tego łańcucha spacje, litery zamień na małe, następnie
# wyznacz zbiór wszystkich liter występujących w tym łańcuchu.
# Pomniejsz ten zbiór o litery samogłoskowe. Pomniejszony zbiór
# wydrukuj w konsoli.
# Oczekiwany rezultat:
# {'z','r','n','j','p','g','w','m','k','t','h'}

# Rozwiązanie:
napis="Programowanie w języku Python"
napis=napis.replace(" ","")
napis=napis.lower()
litery=set(napis)
samogloski={"a","e","o","u","ó","i","y","ą","ę"
}
litery=litery.difference(samogloski)
print(litery)


# Zadanie 20
# Dane są zbiory:
# A={5,3,6,8,9}
# B={5,10,3,7,8}
# Wyznacz różnicę, sumę oraz część wspólną zbiorów A i B. Wydrukuj
# w konsoli wyniki z poprzedzającymi napisami opisującymi operacje
# Oczekiwany wynik:
# Różnica zbiorów A i B: {9, 6}
# Suma zbiorów A i B: {3, 5, 6, 7, 8, 9, 10}
# Część wspólna zbiorów A i B: {8, 3, 5}

# Rozwiązanie:
A={5,3,6,8,9}
B={5,10,3,7,8}
print(f"Różnica zbiorów A i B:
{A.difference(B)}")
print(f"Suma zbiorów A i B: {A.union(B)}")
print(f"Część wspólna zbiorów A i B:
{A.intersection(B)}")


# Zadanie 21
# Dane są dwie listy miast:
# miasta1=['Warszawa','Łódź','Kraków']
# miasta2=["Poznań","Gdańsk","Szczecin"]
# Utwórz trzecią listę (miasta3) która będzie połączeniem tych list.
# Powstałą listę posortuj i wydrukuj.
# Oczekiwany rezultat:
# ['Gdańsk', 'Kraków', 'Poznań', 'Szczecin',
# 'Warszawa', 'Łódź']

# Rozwiązanie:
miasta1=['Warszawa','Łódź','Kraków']
miasta2=["Poznań","Gdańsk","Szczecin"]
miasta3=miasta1+miasta2
miasta3.sort()
print(miasta3)


# Zadanie 22
# Dane są dwie tuple zawierające nazwy miast:
# miasta1=('Warszawa','Łódź','Kraków')
# miasta2=("Poznań","Gdańsk","Szczecin")
# Utwórz trzecią tuplę (miasta3) która będzie połączeniem tych tupli.
# Oczekiwany rezultat:
# ('Warszawa', 'Łódź', 'Kraków', 'Poznań',
# 'Gdańsk', 'Szczecin')

# Rozwiązanie:
miasta1=('Warszawa','Łódź','Kraków')
miasta2=("Poznań","Gdańsk","Szczecin")
miasta3=miasta1+miasta2
print(miasta3)


# Zadanie 23
# Dane są lista i tupla zawierające nazwy miast:
# miasta1=['Warszawa','Łódź','Kraków']
# miasta2=("Poznań","Gdańsk","Szczecin")
# Dołącz elementy z tupli do listy a następnie listę tę posortuj oraz
# wyświetl w konsoli.
# Oczekiwany wynik:
# ['Gdańsk', 'Kraków', 'Poznań', 'Szczecin', 'Warszawa', 'Łódź']

# Rozwiązanie:
miasta1=['Warszawa','Łódź','Kraków']
miasta2=("Poznań","Gdańsk","Szczecin")
miasta1.extend(miasta2)
miasta1.sort()
print(miasta1)


# Zadanie 24
# Dana jest tupla, której elementami są dwie dwuelementowe tuple z
# danymi osób:
# osoby=(("Jan",20),("Monika",25))
# Utwórz nową tuplę (korzystając z tego samego identyfikatora: osoby),
# w której do indeksu 1 będzie przypisana kolejna osoba: Joanna, 22.
# Nową tuplę wydrukuj w konsoli.
# Oczekiwany rezultat:
# (('Jan', 20), ('Joanna', 22), ('Monika', 25))

# Rozwiązanie:
osoby=(("Jan",20),("Monika",25))
osoby=(osoby[0],("Joanna",22),osoby[1])
print(osoby)


# Zadanie 25
# Dana jest tupla:
# tupla1=('nie','tak','tak','nie','tak','tak')
# Przy użyciu formatowania f-string wyświetl w kolejnych wierszach
# informację o liczbie odpowiedzi tak oraz nie.
# Oczekiwany rezultat:
# Odpowiedzi tak: 4
# Odpowiedzi nie: 2

# Rozwiązanie:
tupla1=('nie','tak','tak','nie','tak','tak')
print(f"Odpowiedzi tak: {tupla1.count('tak')}")
print(f"Odpowiedzi nie: {tupla1.count('nie')}")


# Zadanie 26
# Dana jest następująca tupla:
# imiona=("Monika","Anna","Damian","Bożena","Krys
# tyna")
# Utwórz nową tuplę o tym samym identyfikatorze (tuple są
# niemutowalne) zawierającą takie same elementy ale ułożone w
# kolejności alfabetycznej.
# Oczekiwany wynik:
# ('Anna', 'Bożena', 'Damian', 'Krystyna',
# 'Krzysztof', 'Monika')

# Rozwiązanie:
imiona=("Monika","Anna","Damian","Bożena","Krystyna")
imiona=tuple(sorted(list(imiona)))
print(imiona)


# Zadanie 27
# Dana jest następująca zagnieżdżona struktura list zawierająca
# informacje o notowaniach spółek:
# notowania=[['firma1',['ABA',320]],['firma2',
# ['BBF',420]],['firma3',['CAA',120]]]
# Wyświetl w konsoli skrót firmy 1 oraz wartość firmy 2. Zmień
# notowanie firmy 3 na 200. Następnie wyświetl całą listę notowania.
# Oczekiwany rezultat:
# ABA
# 420
# [['firma1', ['ABA', 320]], ['firma2', ['BBF',
# 420]], ['firma3', ['CAA', 200]]]

# Rozwiązanie:
notowania=[['firma1',['ABA',320]],['firma2',
['BBF',420]],['firma3',['CAA',120]]]
print(notowania[0][1][0])
print(notowania[1][1][1])
notowania[2][1][1]=200
print(notowania)


# Zadanie 28
# Dana jest lista liczb:
# lista=[2,56,3,45,1,2,35,8,5,34,43,33,26,18,7]
# Zamień elementy o indeksach od 3 do 5 następującą listą:[5,6,7,8,9]
# Usuń ostatni element listy. Usuń pierwszy element listy. Wydrukuj w
# konsoli zmodyfikowaną listę
# Oczekiwany efekt:
# [56, 3, 5, 6, 7, 8, 9, 35, 8, 5, 34, 43, 33,
# 26, 18]

# Rozwiązanie:
lista=[2,56,3,45,1,2,35,8,5,34,43,33,26,18,7]
lista[3:6]=[5,6,7,8,9]
lista.pop()
lista.pop(0)
print(lista)


# Zadanie 29
# Dana jest lista liczb:
# lista=[2,56,3,45,1,2,35,8,5,34,43,33,26,18,7]
# Wydrukuj w konsoli: 4 początkowe elementy listy, 4 ostatnie
# elementy listy oraz elementy o indeksach od 5 do 10.
# Oczekiwany wynik:
# [56,3,5,6,7,8,9,35,8,5,34,43,33,26,18]
# [2,56,3,45]
# [33,26,18,7]
# [2,35,8,5,34,43]

# Rozwiązanie:
lista=[2,56,3,45,1,2,35,8,5,34,43,33,26,18,7]
print(lista[:4])
print(lista[-4:])
print(lista[5:11])


# Zadanie 30
# Dana jest lista miasta:
# miasta=['Warszawa','Łódź','Kraków']
# Dodaj do listy: Poznań, Gdańsk. Usuń z listy Warszawę. Listę
# posortuj oraz wydrukuj w konsoli.
# Oczekiwany rezultat:
# ['Gdańsk', 'Kraków', 'Poznań', 'Łódź']

# Rozwiązanie:
miasta=['Warszawa','Łódź','Kraków']
miasta.append("Poznań")
miasta.append("Gdańsk")
miasta.remove("Warszawa")
miasta.sort()
print(miasta)


# Zadanie 31
# Dana jest lista:
# lista1=["A","B","A","A","B","A","A","B"]
# Napisz program zliczający liczbę wystąpień elementu "A" na tej liście
# i wynik wyświetl w konsoli przy użyciu formatowania f-string.
# Oczekiwany wynik:
# Liczba elementów A: 5

# Rozwiązanie:
lista1=["A","B","A","A","B","A","A","B"]
print(f"Liczba elementów A:
{lista1.count('A')}")


# Zadanie 32
# Utwórz program, który będzie losować liczby z zakresu 0 do 100 tak
# długo, aż nie zostanie wylosowana liczba 50. Każda wylosowana
# liczba musi być dodana do listy, natomiast po zakończeniu losowań
# (po wylosowaniu liczby 50) cała lista musi być wydrukowana w
# konsoli.
# Przykładowy oczekiwany wynik:
# [31, 65, 70, 35, 101, 71, 70, 33, 53, 6, 65,
# 92, 31, 80, 69, 60, 83, 36, 42, 1, 69, 62, 86,
# 53, 79, 89, 100, 26, 35, 2, 42, 62, 82, 78, 65,
# 9, 51, 50]

# Rozwiązanie:
import random
x=random.randint(0,100)
lista=[x,]
while x!=50:
x=random.randint(0,100)
lista.append(x)
print(lista)


# Zadanie 33
# Przy użyciu pętli wydrukuj w konsoli następującą listę:
# 1*1=1
# 1*2=2
# 1*3=3
# 2*1=2
# 2*2=4
# 2*3=6
# 3*1=3
# 3*2=6
# 3*3=9

# Rozwiązanie:
for x in range(1,4):
for y in range(1,4):
print(f"{x}*{y}={x*y}")


# Zadanie 34
# Napisz program, który wylosuje 1000 razy liczbę z zakresu 0 do 100.
# Po zakończeniu losowań w konsoli powinny się wyświetlić dwie
# informację: ile liczb zostało wylosowanych w zakresie od 0 do 50
# oraz ile liczb zostało wylosowanych w zakresie 51 do 100.
# Przykładowy oczekiwany wynik:
# W zakresie od 0 do 50 wylosowano: 510 liczb.
# W zakresie od 51 do 100 wylosowano: 490 liczb.

# Rozwiązanie:
import random
zakres1=0
zakres2=0
for x in range(1000):
los=random.randint(0,100)
if los in range(0,51):
zakres1+=1
else:
zakres2+=1
print(f"W zakresie od 0 do 50 wylosowano:
{zakres1} liczb.")
print(f"W zakresie od 51 do 100 wylosowano:
{zakres2} liczb.")


# Zadanie 35
# Dana jest następująca lista plików graficznych:
# pliki=["plik1.jpg","plik2.bmp","plik3.jpg","pli
# k4.png","plik5.jpg"]
# Na podstawie tej listy wyznacz zbiór wszystkich nazw plików (bez
# rozszerzenia) oraz oddzielny zbiór wszystkich rozszerzeń plików (bez
# kropki). Oba zbiory wydrukuj w konsoli.
# Oczekiwany rezultat:
# {'plik5', 'plik2', 'plik4', 'plik1', 'plik3'}
# {'jpg', 'bmp', 'png'}

# Rozwiązanie:
pliki=["plik1.jpg","plik2.bmp","plik3.jpg","pli
k4.png","plik5.jpg"]
nazwy=set()
rozszerzenia=set()
for x in pliki:
podzielony=x.split(".")
nazwy.add(podzielony[0])
rozszerzenia.add(podzielony[1])
print(nazwy)
print(rozszerzenia)


# Zadanie 36
# Dany jest słownik zawierający informacje o stolicach różnych krajów:
# slownik={
# "Warszawa":"Polska",
# "Berlin":"Niemcy",
# "Paryż":"Francja",
# "Rzym":"Włochy",
# "Madryt":"Hiszpania",
# "Oslo":"Norwegia"
# }
# Przenieś do listy wszystkie nazwy stolic, posortuj tę listę, następnie
# wydrukuj w konsoli.
# Przenieś do drugiej listy wszystkie nazwy krajów, posortuję tę listę,
# następnie wydrukuj w konsoli.
# Oczekiwany rezultat:
# ['Berlin', 'Madryt', 'Oslo', 'Paryż', 'Rzym',
# 'Warszawa']
# ['Francja', 'Hiszpania', 'Niemcy', 'Norwegia',
# 'Polska', 'Włochy']

# Rozwiązanie:
slownik={
"Warszawa":"Polska",
"Berlin":"Niemcy",
"Paryż":"Francja",
"Rzym":"Włochy",
"Madryt":"Hiszpania",
"Oslo":"Norwegia"
}
stolice=sorted(list(slownik.keys()))
print(stolice)
kraje=sorted(list(slownik.values()))
print(kraje)


# Zadanie 37
# Dany jest słownik uczniowie, którego wartościami są słowniki
# zawierające dane poszczególnych uczniów:
# uczniowie={
# "id1":{"imię":"Adam","wiek":15,"wzrost":150},
# "id2":{"imię":"Joanna","wiek":16,"wzrost":156},
# "id3":{"imię":"Monika","wiek":14,"wzrost":144}
# }
# Zaktualizuj wzrost uczennicy Joanna na 160 cm. Zaktualizuj wiek
# uczennicy Monika na 15. Dodaj do słownika nowego ucznia ("id4") o
# imieniu Jacek, wieku 15 lat i wzroście 152 cm. Zmieniony słownik
# uczniowie wydrukuj w konsoli.
# Oczekiwany wynik:
# {'id1': {'imię': 'Adam', 'wiek': 15, 'wzrost': 150},
# 'id2': {'imię': 'Joanna', 'wiek': 16, 'wzrost': 160},
# 'id3': {'imię': 'Monika', 'wiek': 15, 'wzrost': 144},
# 'id4': {'imię': 'Jacek', 'wiek': 15, 'wzrost':
# 152}}

# Rozwiązanie:
uczniowie={
"id1":{"imię":"Adam","wiek":15,"wzrost":150},
"id2":{"imię":"Joanna","wiek":16,"wzrost":156},
"id3":{"imię":"Monika","wiek":14,"wzrost":144}
}
uczniowie["id2"]["wzrost"]=160
uczniowie["id3"]["wiek"]=15
uczniowie["id4"]={"imię":"Jacek","wiek":15,"wzrost":1
52}
print(uczniowie)


# Zadanie 38
# Dana jest lista zawierające kody:
# kody=['AAB','CDA','ADB','BBC','AAA','CBB','BBA'
# ,'CCC']
# Przekształć tę listę w słownik złożony z par: indeks-kod, przy czym
# indeksowanie musi się rozpoczynać od 0.
# Otrzymany słownik wydrukuj w konsoli.
# Oczekiwany rezultat:
# {0: 'AAB', 1: 'CDA', 2: 'ADB', 3: 'BBC', 4:
# 'AAA', 5: 'CBB', 6: 'BBA', 7: 'CCC'}

# Rozwiązanie:
kody=['AAB','CDA','ADB','BBC','AAA','CBB','BBA'
,'CCC']
slownik=dict(enumerate(kody))
print(slownik)


# Zadanie 39
# Dany jest słownik:
# studenci={
# "id1":"Adam",
# "id2":"Monika",
# "id3":"Joanna",
# "id4":"Adam",
# "id5":"Grzegorz",
# "id6":"Anna",
# "id7":"Jacek"
# }
# Wyświetl w konsoli listę imion z tego słownika, która będzie
# posortowana i nie będzie zawierać powtórzeń.
# Oczekiwany wynik:
# ['Adam', 'Anna', 'Grzegorz', 'Jacek', 'Joanna',
# 'Monika']

# Rozwiązanie:
studenci={
"id1":"Adam",
"id2":"Monika",
"id3":"Joanna",
"id4":"Adam",
"id5":"Grzegorz",
"id6":"Anna",
"id7":"Jacek"
}
print(sorted(list(set(studenci.values()))))


# Zadanie 40
# Dany jest słownik zawierający dane o produktach i cenach:
# produkty={
# "produkt1":100,
# "produkt2":150,
# "produkt3":120,
# "produkt4":200,
# "produkt5":300
# }
# Zamień cenę produktu 2 na 250. Usuń produkt 4 ze słownika. Dodaj
# nowy produkt (produkt6) z ceną 400. Po modyfikacjach wydrukuj
# zawartość słownika w konsoli.
# Oczekiwany rezultat:
# {'produkt1': 100, 'produkt2': 250, 'produkt3':
# 120, 'produkt5': 300, 'produkt6': 400}

# Rozwiązanie:
produkty={
"produkt1":100,
"produkt2":150,
"produkt3":120,
"produkt4":200,
"produkt5":300,
}
produkty["produkt2"]=250
produkty.pop("produkt4")
produkty["produkt6"]=400
print(produkty)


# Zadanie 41
# Zdefiniuj funkcję, do której jako argument można przekazywać
# dowolny obiekt iterowalny (tupla,zbiór,lista) zawierający łańcuchy
# tekstowe, i która zwraca listę łańcuchów o długości większej niż 7
# znaków.
# Przykład użycia:
# lista=["komputer","monitor","laptop","klawiatur
# a","drukarka"]
# lista2=zliczaj_wieksze_niz_7(lista)
# Oczekiwany wynik:
# ['komputer', 'klawiatura', 'drukarka']

# Rozwiązanie:
def zliczaj_wieksze_niz_7(wyrazy):
wynik=[]
for wyraz in wyrazy:
if len(wyraz)>7:
wynik.append(wyraz)
return wynik
lista=["komputer","monitor","laptop","klawiatur
a","drukarka"]
lista2=zliczaj_wieksze_niz_7(lista)
print(lista2)


# Zadanie 42
# Zdefiniuj funkcję, która będzie sprawdzać, czy iterowalny obiekt
# przekazany jako argument zawiera unikalne wartości:
# Przykłady użycia 1:
# lista=[1,2,3,4]
# print(unikalne(lista))
# Oczekiwany wynik:
# True
# Przykłady użycia 2:
# lista=[1,2,4,4]
# print(unikalne(lista))
# Oczekiwany wynik:
# False

# Rozwiązanie:
def unikalne(elementy):
return len(elementy)==len(set(elementy))
lista=[1,2,3,4]
print(unikalne(lista))
lista=[1,2,4,4]
print(unikalne(lista))


# Zadanie 43
# Zdefiniuj funkcję, która będzie usuwać duplikaty z listy przekazanej
# jako argument i będzie zwracać wynik w postaci posortowanej listy.
# Przykład użycia:
# lista=["A","D","C","A","B","C","D","A","B","C",
# "B","D"]
# lista2=usun_duplikaty(lista)
# print(lista2)
# Oczekiwany wynik:
# ['A', 'B', 'C', 'D']

# Rozwiązanie:
def usun_duplikaty(dane):
return sorted(list(set(dane)))
lista=["A","D","C","A","B","C","D","A","B","C",
"B","D"]
lista2=usun_duplikaty(lista)
print(lista2)


# Zadanie 44
# Utwórz funkcję, która będzie zwracać długość najdłuższego wyrazu w
# obiekcie iterowalnym (lista, tupla, zbiór) przekazanym jako argument.
# Przykład użycia:
# sprzet=["komputer","monitor","laptop","klawiatu
# ra","drukarka"]
# print(najdluzszy_wyraz(sprzet))
# Oczekiwany wynik:
# 10

# Rozwiązanie 1:
def najdluzszy_wyraz(wyrazy):
x=0
for wyraz in wyrazy:
if len(wyraz)>x:
x=len(wyraz)
return(x)
sprzet=["komputer","monitor","laptop","klawiatu
ra","drukarka"]
print(najdluzszy_wyraz(sprzet))

# Rozwiązanie 2:
def najdluzszy_wyraz2(wyrazy):
lista=[0]
for wyraz in wyrazy:
lista.append(len(wyraz))
return(max(lista))
sprzet=["komputer","monitor","laptop","klawiatu
ra","drukarka"]
print(najdluzszy_wyraz2(sprzet))


# Zadanie 45
# Utwórz funkcję, która będzie zwracać najmniejszą z trzech liczb
# przekazywanych jako argument. Konstrukcja tej funkcji powinna
# opierać się na instrukcji warunkowej if.
# Przykład użycia:
# print(minimum(3,5,7))
# print(minimum(4,2,7))
# print(minimum(8,7,5))
# Oczekiwany wynik:
# 3
# 2
# 5

# Rozwiązanie:
def minimum(a,b,c):
if a<b and a<c:
return a
elif b<c:
return b
else:
return c
print(minimum(3,5,7))
print(minimum(4,2,7))
print(minimum(8,7,5))


# Zadanie 46
# Napisz funkcję do której można przekazywać obiekt iterowalny
# zawierający dowolne wartości i która będzie zwracała tylko łańcuchy
# (wartości typu string) dłuższe niż 3 znaki.
# Przykład użycia:
# dane=["abcd",12,"True",False,12,"dwanaście"]
# print(lancuchy_dluzsze_niz_3(dane))
# Oczekiwany wynik:
# ['abcd', 'True', 'dwanaście']

# Rozwiązanie:
def lancuchy_dluzsze_niz_3(wykaz):
wynik=[]
for x in wykaz:
if isinstance(x,str):
if len(x)>3:
wynik.append(x)
return wynik
dane=["abcd",12,"True",False,12,"dwanaście"]
print(lancuchy_dluzsze_niz_3(dane))


# Zadanie 47
# Przy użyciu Notatnika utwórz plik tekstowy tekst1.txt (kodowanie
# UTF8) w katalogu "c:/pliki". W treści pliku umieść następującą
# zawartość:
# wyraz1 wyraz2 wyraz3
# wyraz4 wyraz5 wyraz6
# wyraz7 wyraz8 wyraz9
# wyraz10 wyraz11 wyraz12
# Napisz program, który odczyta zawartość tego pliku do zmiennej dane
# i zamieni fragmenty "wyraz" na "x". Następnie program powinien
# wyświetlić w konsoli oznaczone etykietami: zawartość zmiennej dane,
# typ zmiennej dane oraz liczbę znaków tekstowych w zmiennej dane.
# Oczekiwany wynik:
# Zawartość: x1 x2 x3
# x4 x5 x6
# x7 x8 x9
# x10 x11 x12
# Typ zmiennej dane: <class 'str'>
# Długość tekstu: 38

# Rozwiązanie:
f=open("C:/pliki/tekst1.txt", mode="r",
encoding="utf-8")
dane=f.read()
f.close()
dane=dane.replace("wyraz","x")
print(f"Zawartość: {dane}")
print(f"Typ zmiennej dane: {type(dane)}")
print(f"Długość tekstu: {len(dane)}")


# Zadanie 48
# Przy użyciu Notatnika utwórz plik tekstowy tekst1.txt (kodowanie
# UTF8) w katalogu "c:/pliki". W treści pliku umieść następującą
# zawartość:
# wyraz1 wyraz2 wyraz3
# wyraz4 wyraz5 wyraz6
# wyraz7 wyraz8 wyraz9
# wyraz10 wyraz11 wyraz12
# Napisz program, który odczyta zawartość tego pliku i przeniesie ją do
# listy dane. Następnie program powinien wydrukować w konsoli
# informacje o długościach poszczególnych łańcuchów w tej liście.
# Oczekiwany wynik:
# 21
# 21
# 21
# 23

# Rozwiązanie:
with open("C:/pliki/tekst1.txt", mode="r",
encoding="utf-8") as plik:
dane=plik.readlines()
for wiersz in dane:
print(len(wiersz))


# Zadanie 49
# Napisz program, który wygeneruje 100 liczb losowych w zakresie 0
# do 1000 i wynik zamieści w liście, a następnie przeniesie zawartość
# tej listy do pliku tekstowego teskt2.txt w katalogu pliki na dysku c.

# Rozwiązanie:
import random
losy=[]
for x in range(100):
losy.append(str(random.randint(0,1000))+"\n")
with open("C:/pliki/tekst2.txt", mode="w",
encoding="utf-8") as plik:
plik.writelines(losy)


# Zadanie 50
# Utwórz klasę Prostokat. Obiekty tej klasy muszą przechowywać
# informacje o długości boków prostokąta oraz o jego polu i obwodzie.
# W czasie tworzenia tworzenia instancji klasy Prostokat będą
# przekazywane dane o długości boków a i b. Pole i obwód powinny
# zostać obliczone automatycznie przy tworzeniu instancji.
# Przykład użycia:
# pr1=Prostokat(10,20)
# print(f"Obwód: {pr1.obwod}")
# print(f"Pole: {pr1.pole}")
# Oczekiwany wynik:
# Obwód: 60
# Pole: 200

# Rozwiązanie:
class Prostokat:
def __init__(self,a,b):
self.bok_a=a
self.bok_b=b
self.oblicz_obwod()
self.oblicz_pole()
def oblicz_obwod(self):
self.obwod=(2*self.bok_a)+(2*self.bok_b)
def oblicz_pole(self):
self.pole=self.bok_a*self.bok_b
pr1=Prostokat(10,20)
print(f"Obwód: {pr1.obwod}")
print(f"Pole: {pr1.pole}")