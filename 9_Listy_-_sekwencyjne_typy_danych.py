from random import randint
# Temat: Listy - sekwencyjne typy danych

# a = 20

# idx  0   1      2      3
lista=[20,12.8,"tekst",True]
# idx  -4  -3    -2     -1
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[-4])
print(lista[-3])
print(lista[-2])
print(lista[-1])

# idx          0  1  2  3  4  5   6  7  8  9
lista_numerow=[10,20,30,40,50,60,70,80,90,100]
# idx         -10 -9 -8 -7 -6 -5  -4 -3 -2 -1

# wycinek [start:stop-1:step]

# ZAD. 1 Wypisz liczby od 30 do 60
print(lista_numerow[2:6])

# cała lista co 2
print(lista_numerow[::2])

# lista od końca do początku
print(lista_numerow[::-1])
lista_odwrotna=lista_numerow[::-1]
print(lista_odwrotna)

# modyfikacja elementu listy
lista_numerow[0]=200
print(lista_numerow)

# ZAD. 2 Utwóz program który utworzy 10-elementową listę liczb całkowitych wprowadzonych z klawiatury
lista_uzytkownika=[]
for i in range(10):
  lista_uzytkownika.append(int(input(f"Podaj liczbę {i+1}: ")))
print(lista_uzytkownika)

# losowa lista z wykorzystaniem modułu random
lista_randomowa=[]
for i in range(10):
  lista_randomowa.append(randint(1,100))
print(lista_randomowa)

# funkcja która zwraca długość listy
print(len(lista_randomowa))

# ZAD. 3 Napisz program który obliczy sumę elementów listy
# sposób 1 - for i in lista
suma=0
for i in lista_randomowa:
  suma+=i
print(suma)

# sposób 2 - for i in range(len(lista))
suma1=0
for i in range(len(lista_randomowa)):
  suma1+=lista_randomowa[i]
print(suma1)

# sposób 3 - while
suma2=0
i=0
while i > len(lista_randomowa):
  suma2 += lista_randomowa[i]
  i+=1
print(suma2)

# Napisz program wykonujący napstępujące operacje na liście zawierającej liczby całkowite:
# a) wypisanie wszytkich elementów listy
for el in lista_randomowa:
  print(el, end=" ")
# b) obliczenie liczby tych elementów listy, które są parzyste
ile=0
for i in lista_randomowa:
  if i%2==0:
    ile+=1
# c) zwiększenie o 2 wartości tych elmentów listy, którch wartość jest mniejsza od 5
for el in range(len(lista_randomowa)):
  if el < 5:
    el += 2
print(lista_randomowa)