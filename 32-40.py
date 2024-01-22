#32
#Utwórz program, który będzie losować liczby z zakresu 0 do 100 tak 
#długo, aż nie zostanie wylosowana liczba 50. Każda wylosowana 
#liczba musi być dodana do listy, natomiast po zakończeniu losowań 
#(po wylosowaniu liczby 50) cała lista musi być wydrukowana w 
#konsoli.      

import random
x=random.randint(0,100)

lista=[x,]
while x!=50:
    x=random.randint(0,100)
    lista.append(x)
print(lista)


#33
#Przy użyciu pętli wydrukuj w konsoli następującą listę:
#1*1=1
#1*2=2
#1*3=3
#2*1=2
#2*2=4
#2*3=6
#3*1=3
#3*2=6
#3*3=9

for x in range(1,4):
    for y in range (1,4):
        print(f'{x}*{y}={x*y}')



#34
#Napisz program, który wylosuje 1000 razy liczbę z zakresu 0 do 100. 
#Po zakończeniu losowań w konsoli powinny się wyświetlić dwie 
#informację: ile liczb zostało wylosowanych w zakresie od 0 do 50 
#oraz ile liczb zostało wylosowanych w zakresie 51 do 100.

import random
zakres1=0
zakres2=0

for x in range(1000):
    los=random.randint(0,100)
    if los in range(0,51):
        zakres1+=1
    else:
        zakres2+=1

print(f'W zakresie od 0 do 50: {zakres1} liczb.')
print(f'W zakresie od 51 do 100: {zakres2} liczb.')


#35
#Dana jest następująca lista plików graficznych:
#pliki=["plik1.jpg","plik2.bmp","plik3.jpg","plik4.png","plik5.jpg"]
#Na podstawie tej listy wyznacz zbiór wszystkich nazw plików (bez 
#rozszerzenia) oraz oddzielny zbiór wszystkich rozszerzeń plików (bez 
#kropki). Oba zbiory wydrukuj w konsoli.

pliki=["plik1.jpg","plik2.bmp","plik3.jpg","plik4.png","plik5.jpg"]
nazwy=set()
rozszerzenia=set()

for x in pliki:
    podzielony=x.split('.')
    nazwy.add(podzielony[0])
    rozszerzenia.add(podzielony[1])

print(nazwy)
print(rozszerzenia)


#36
#Dany jest słownik zawierający informacje o stolicach różnych krajów:
#slownik={
#"Warszawa":"Polska",
#"Berlin":"Niemcy",
#"Paryż":"Francja",
#"Rzym":"Włochy",
#"Madryt":"Hiszpania",
#"Oslo":"Norwegia"
#}
#Przenieś do listy wszystkie nazwy stolic, posortuj tę listę, następnie 
#wydrukuj w konsoli.
#Przenieś do drugiej listy wszystkie nazwy krajów, posortuję tę listę, 
#następnie wydrukuj w konsoli.

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


#37
#Dany jest słownik uczniowie, którego wartościami są słowniki 
#zawierające dane poszczególnych uczniów:
#uczniowie={
#"id1":{"imię":"Adam","wiek":15,"wzrost":150},
#"id2":{"imię":"Joanna","wiek":16,"wzrost":156},
#"id3":{"imię":"Monika","wiek":14,"wzrost":144}
#}
#Zaktualizuj wzrost uczennicy Joanna na 160 cm. Zaktualizuj wiek
#uczennicy Monika na 15. Dodaj do słownika nowego ucznia ("id4") o 
#imieniu Jacek, wieku 15 lat i wzroście 152 cm. Zmieniony słownik 
#uczniowie wydrukuj w konsoli.

uczniowie={
"id1":{"imię":"Adam","wiek":15,"wzrost":150},
"id2":{"imię":"Joanna","wiek":16,"wzrost":156},
"id3":{"imię":"Monika","wiek":14,"wzrost":144}
}

uczniowie['id2']['wzrost']=160
uczniowie['id3']['wiek']=15
uczniowie['id4']={'imię':'Jacek','wiek':15,'wzrost':152}

print(uczniowie)



#38
#Dana jest lista zawierające kody:
#kody=['AAB','CDA','ADB','BBC','AAA','CBB','BBA','CCC']
#Przekształć tę listę w słownik złożony z par: indeks-kod, przy czym 
#indeksowanie musi się rozpoczynać od 0.
#Otrzymany słownik wydrukuj w konsoli.

kody=['AAB','CDA','ADB','BBC','AAA','CBB','BBA','CCC']
slownik=dict(enumerate(kody))
print(slownik)


#39
#Dany jest słownik:
#studenci={
#"id1":"Adam",
#"id2":"Monika",
#"id3":"Joanna",
#"id4":"Adam",
#"id5":"Grzegorz",
#"id6":"Anna",
#"id7":"Jacek"
#}
#Wyświetl w konsoli listę imion z tego słownika, która będzie
#posortowana i nie będzie zawierać powtórzeń

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



#40
#Dany jest słownik zawierający dane o produktach i cenach:
#produkty={
#"produkt1":100,
#"produkt2":150,
#"produkt3":120,
#"produkt4":200,
#"produkt5":300
#}
#Zamień cenę produktu 2 na 250. Usuń produkt 4 ze słownika. Dodaj 
#nowy produkt (produkt6) z ceną 400. Po modyfikacjach wydrukuj 
#zawartość słownika w konsoli.

produkty={
"produkt1":100,
"produkt2":150,
"produkt3":120,
"produkt4":200,
"produkt5":300
}
produkty['produkt2']=250
produkty.pop('produkt4')
produkty['produkt6']=400
print(produkty)


################################

#41
#Zdefiniuj funkcję, do której jako argument można przekazywać 
#dowolny obiekt iterowalny (tupla,zbiór,lista) zawierający łańcuchy
#tekstowe, i która zwraca listę łańcuchów o długości większej niż 7 
#znaków.
#Przykład użycia:
#lista=["komputer","monitor","laptop","klawiatur
#a","drukarka"]
#lista2=zliczaj_wieksze_niz_7(lista)

def zliczaj(wyrazy):
    wynik=[]
    for wyraz in wyrazy:
        if len(wyraz)>7:
            wynik.append(wyraz)
    return(wynik)

lista=["komputer","monitor","laptop","klawiatura","drukarka"] 
lista2=zliczaj(lista)
print(lista2)           


#42
#Zdefiniuj funkcję, która będzie sprawdzać, czy iterowalny obiekt 
#przekazany jako argument zawiera unikalne wartości:
#Przykłady użycia 1:
#lista=[1,2,3,4]
#print(unikalne(lista))

def unikalne(elementy):
    return len(elementy)==len(set(elementy))

lista=[1,2,3,4]
print(unikalne(lista))
lista=[1,2,4,4]
print(unikalne(lista))



#43
#Zdefiniuj funkcję, która będzie usuwać duplikaty z listy przekazanej 
#jako argument i będzie zwracać wynik w postaci posortowanej listy

def usun_duplikaty(dane):
    return sorted(list(set(dane)))

lista=["A","D","C","A","B","C","D","A","B","C","B","D"]
lista2=usun_duplikaty(lista)
print(lista2)


#44
#Utwórz funkcję, która będzie zwracać długość najdłuższego wyrazu w 
#obiekcie iterowalnym (lista, tupla, zbiór) przekazanym jako argument.
#Przykład użycia:
#sprzet=["komputer","monitor","laptop","klawiatu
#ra","drukarka"]
#print(najdluzszy_wyraz(sprzet))

def naj_wyraz(wyrazy):
    x=0
    for wyraz in wyrazy:
        if len(wyraz)>x:
            x=len(wyraz)
    return(x)

sprzet=["komputer","monitor","laptop","klawiatura","drukarka"]
print(naj_wyraz(sprzet))




#45
#Utwórz funkcję, która będzie zwracać najmniejszą z trzech liczb 
#przekazywanych jako argument. Konstrukcja tej funkcji powinna 
#opierać się na instrukcji warunkowej if.
#Przykład użycia:
#print(minimum(3,5,7))
#print(minimum(4,2,7))
#print(minimum(8,7,5))

def minimum(a,b,c):
    if a<b and a<c:
        return a
    elif b<c:
        return b
    else:
        return c

print(minimum(3,5,7))
print(minimum(1,2,3))                
print(minimum(8,7,2))



#46
#Napisz funkcję do której można przekazywać obiekt iterowalny 
#zawierający dowolne wartości i która będzie zwracała tylko łańcuchy 
#(wartości typu string) dłuższe niż 3 znaki.
#Przykład użycia:
#dane=["abcd",12,"True",False,12,"dwanaście"]
#print(lancuchy_dluzsze_niz_3(dane))

def longer_than_3(wykaz):
    wynik=[]
    for x in wykaz:
        if isinstance(x,str):
            if len(x)>3:
                wynik.append(x)
    return wynik

dane=["abcd",12,"True",False,12,"dwanaście"]
print(longer_than_3(dane))

























