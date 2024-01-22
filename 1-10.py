#1
#Napisz program, który policzy deltę dla równania kwadratowego:
a=3
b=-4
c=1
delta = b**2-4*a*c
print("Delta wynosi: ",delta)


#2
#Do kolejnych zmiennych (x1,x2,x3 oraz x4) przypisz następujące
#wartości:
#- znak nowej linii,
#- znak tabulatora
#- znak \ (backslash)
#- cudzysłów
#Wszystkie zmienne wydrukuj w jednej linii (przy użyciu
#formatowania f-string) w konsoli z poprzedzającą informacją o znaku.

x1 = '\n'
x2 = "\t"
x3 = "\\"
x4 = "\""
print(f"koniec linii: {x1} tabulator: {x2} backslash: {x3} cudzysłów: {x4}")

#3
#Dana jest nazwa pliku przypisana do zmiennej nazwa:
#nazwa="plik1.jpg"
#Wytnij z tej nazwy rozszerzenie (z kropką) i wyświetl go w konsoli

nazwa = 'plik.jpg'
print(nazwa[-4])


#4
#Wyznacz środek odcinka o końcach w punktach:
#A = (2, 4),
#B = (-4, 6).

x1 = 2
y1 = 4
x2 = -4
y2 = 6
s1=(x1+x2)/2
s2=(y1+y2)/2
print(f'Środek odcinka AB wynosi: ({s1}, {s2})')


#5
#Napisz program, który wyznaczy wszystkie liczby dwucyfrowe
#podzielne przez 7. Wynik wydrukuj do konsoli w postaci jednego
#łańcucha zawierającego wartości rozdzielone przecinkami.

wynik = []
for i in range(10,100):
    if i%7==0:
        wynik.append(str(i))
print(','.join(wynik))        


#6
#Wygeneruj ciąg arytmetyczny skończony, w którym pierwszy wyraz
#jest równy 0, ostatni wyraz nie jest większy niż 100, natomiast różnica
#w tym ciągu wynosi 3. Zapisz ciąg w liście oraz wydrukuj tę listę w
#konsoli.

lista = []
for x in range (0,100,3):
    lista.append(x)
print(lista)


#7
#Napisz program, który utworzy histogram - rozkład częstości w
#postaci słownika liter przechowywanych w liście:
#lista=['x','y','z','y','x','y','y','z','x']
#W odpowiedzi utworzony słownik wydrukuj do konsoli.

lista = ['x','y','z','y','x','y','y','z','x']

slownik = {}
for litera in lista:
    if litera not in slownik.keys():
        slownik[litera] = 1
    else:
        slownik[litera] += 1
print(slownik)



#8
#Podana jest niepełna lista imion (jednego brak):
#lista=['Jacek','Tomek','Monika',None,'Barbara']
#Lista składa się tylko z obiektów typu str lub wartości None.
#Posługując się instrukcją for oraz poleceniem continue wydrukuj do
#konsoli tylko poprawnie przekazane imiona (obiekty typu str).

lista=['Jacek','Tomek','Monika',None,'Barbara']

for name in lista:
    if name is None:
        continue
    print(name)



#9
#Dane są następujące zmienne:
#x1=None
#x2=False
#x3='False'
#x4=0
#x5=100
#x6=""
#x7="ABC"
#Przy użyciu formatowania f-string wyświetl informacje o wartościach
#logicznych reprezentowanych przez te wartości.

x1=None
x2=False
x3='False'
x4=0
x5=100
x6=""
x7="ABC"

print( f'Wartości logiczne: \n x1 to {bool(x1)} \n x2 to {bool(x2)} \n x3 to {bool(x3)} \n x4 to {bool(x4)} \n x5 to {bool(x5)} \n x6 to {bool(x6)} \n x7 to {bool(x7)}')



#10
#Dane są poniższe kody:
#kod1='AKRTB-20'
#kod2='AKRTB20'
#Używając odpowiedniej metody sprawdź czy kody składają się tylko
#ze znaków alfanumerycznych (cyfry + litery). Wynik wydrukuj do
#konsoli tak jak pokazano poniżej.

kod1='AKRTB-20'
kod2='AKRTB20'

print(f'Kod 1: {kod1.isalnum()}')
print(f'Kod 2: {kod2.isalnum()}')






























