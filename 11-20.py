#11
#Dana jest zmienna napis:
#napis=" Python "
#Wydrukuj w konsoli ten łańcuch (z dopiskiem przed łańcuchem:
#„Napis zmieniony:”) z uwzględnieniem następujących modyfikacji:
#- tylko wielkie litery,
#- tylko małe litery,
#- bez spacji z dwóch stron
#- bez spacji z lewej strony
#- bez spacji z prawej strony
#- bez spacji z dwóch stron oraz zapisany małymi literami

napis = ' Python  '

print(f'Napis zmieniony: {napis.upper()}.')
print(f'Napis zmieniony: {napis.lower()}.')
print(f'Napis zmieniony: {napis.strip()}.')
print(f'Napis zmieniony: {napis.lstrip()}.')
print(f'Napis zmieniony: {napis.rstrip()}.')
print(f'Napis zmieniony: { (napis.strip()). lower()}.')


#12
#Dana jest zmienna zdanie, która przechowuje dowolny łańcuch
#tekstowy. Napisz program, który wyświetla w konsoli jeden z dwóch
#poniższych komunikatów w zależności od tego, czy zdanie
#rozpoczyna się od wyrazu: "Programowanie":
#Pierwszy wyraz to: 'Programowanie'
#Inny wyraz na początku zdania"

zdanie = 'Programowanie w języku Python'
if zdanie.startswith('Programowanie'):
    print('Pierwszy wyraz to: Programowanie')
else:
    print('Inny wyraz na początku zdania')

#13
#Dana jest zmienna zdanie, która przechowuje dowolny łańcuch
#tekstowy. Napisz program, który wyświetla w konsoli jeden z
#poniższych komunikatów w zależności od tego, czy zdanie kończy się
#od wyrazem: "Python":
#Ostatni wyraz to:'Python'
#Inny wyraz na końcu zdania

zdanie = 'Programowanie w języku Python'
if zdanie.endswith('Python'):
    print('Ostatni wyraz to: Python')
else:
    print('Inny wyraz na końcu zdania')


#14
#Dane są zmienne:
#napis="cena produktu: "
#cena=12.50
#Połącz te dane w jeden napis (wykonaj konkatenację) i wynik
#wyświetl w konsoli.    

napis="cena produktu: "
cena=12.50

print(napis+str(cena))


#15
#Dana jest zmienna kod:
#kod='237-192-45-45'
#Usuń dywizy z tego zapisu. Wynik zapisz w zmiennej o takiej samej
#nazwie (kod). Następnie otrzymany łańcuch wydrukuj w konsoli.
 
kod='237-192-45-45'

kod=kod.replace('-','')
print(kod)


#16
#Zlicz liczbę wystąpień litery P w zdaniu przechowywanym w
#zmiennej zdanie:
#zdanie="Programowanie w języku Python"
#Następnie korzystając z formatowania f-string wyświetl w konsoli
#komunikat (podstawiając otrzymany wynik):
#Liczba wystąpień litery P: 2

zdanie="Programowanie w języku Python"
print(f"Liczba wystąpień litery P: {zdanie.count('P')}")


#17
#Dana jest zmienna owoce przechowująca łańcuch tekstowy:
#owoce="Jabłko,Banan,Śliwka,Pomidor"
#Używając odpowiedniej metody podziel tekst na wyrazy i umieść je w
#liście. Zawartość tej listy wydrukuj w konsoli.

owoce="Jabłko,Banan,Śliwka,Pomidor"
lista=owoce.split(',')
print(lista)


#18
#Dany jest zbiór:
#owoce={'jabłko','gruszka'}
#Używając odpowiedniej metody dodaj do tego zbioru kolejny
#elementy: śliwka oraz czereśnia.
#Używając odpowiedniej metody usuń element: jabłko
#Wydrukuj w konsoli zwartość zbioru po tych operacjach oraz
#informację o liczbie owoców (poprzedzoną napisem: Liczba
#owoców).

owoce={'jabłko','gruszka'}
owoce.add('śliwka')
owoce.add('czereśnia')
owoce.remove('jabłko')
print(owoce)
print(f'LIczba owoców: {len(owoce)}')


#19
#Dany jest następujący łańcuch tekstowy przechowywany w zmiennej
#napis="Programowanie w języku Python"
#Usuń z tego łańcucha spacje, litery zamień na małe, następnie
#wyznacz zbiór wszystkich liter występujących w tym łańcuchu.
#Pomniejsz ten zbiór o litery samogłoskowe. Pomniejszony zbiór
#wydrukuj w konsoli.

napis="Programowanie w języku Python"
napis=napis.replace(' ','')
napis=napis.lower()
litery=set(napis)
samogloski={'a','e','o','u','ó','i','y','ą','ę'}
litery=litery.difference(samogloski)
print(litery)


#20
#Dane są zbiory:
#A={5,3,6,8,9}
#B={5,10,3,7,8}
#Wyznacz różnicę, sumę oraz część wspólną zbiorów A i B. Wydrukuj
#w konsoli wyniki z poprzedzającymi napisami opisującymi operacje

A={5,3,6,8,9}
B={5,10,3,7,8}

print(f'Różnica zbiorów: {A.difference(B)}')
print(f'Suma zbiorów: {A.union(B)}')
print(f'Część wspólna zbiorów: {A.intersection(B)}')












