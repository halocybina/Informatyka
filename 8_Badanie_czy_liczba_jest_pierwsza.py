'''
Temat: Badanie czy liczba jest pierwszą
Liczba pierwsza to liczba naturalna większa od 1, która ma dokładnie dwa dzielniki: jedynkę i siebie samą. Pozostałe liczby to liczby złożone. 1 i 0 nie są liczbami pierwszymi ani złożonymi.
'''
# Napisz program, który wypisuje wszystkie dzielniki badanej liczby naturalnej n.

n = int(input("Podaj liczbę: "))
for i in range(1,n+1):
  if n%i == 0:
    print(i, end=" ")
'''
Dane:
n - liczba naturalna
Wynik:
True - jeśli liczba jest pierwsza'''
def  pierwsza(n):
  if n < 2:
    return False
  if n == 2:
    return True
  if n%2 == 0:
    return False
  for i in range(3,int(n**0.5)+1,2):
    if n%i == 0:
      return False
  return True

print(pierwsza(13))
print(pierwsza(25))

def pierwsza1(n):
  if n<2:
    return False
  if n == 2
    return True
  if n%2 == 0:
    return False
  i = 3
  while i*i <= n:
    if n%i == 0:
      return False
    i+=2
  return True

# Napisz program który wypisze tylko dzielniki pierwsze badanej liczby naturalnej n
n = int(input("Podaj liczbę: "))

for i in range(1,n+1):
  if n%i == 0 and pierwsza1(i):
    print(i, end=" ")

# Napisz program który sprawdzi czy dwie wprowadzone przez użytkownika liczby naturalne są bliźniacze. Liczby bliźniacze to dwie liczby pierwsze, których różnica wynosi 2. np. (11,13)
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
if pierwsza1(a) and pierwsza1(b) and abs(a-b) == 2:
   print("Liczby są bliźniacze")
else:
    print("Liczby nie sa blizniacze")

n = int(input("Podaj liczbe: "))
# Sprawdzenie, czy liczba jest pierwsza
def czy_pierwsza(n):
    if n < 2:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

if czy_pierwsza(n):
    print(f"Liczba {n} jest pierwsza!")
else:
    print(f"Liczba {n} nie jest pierwsza.")

# 
    l1 = int(input("Podaj liczbę 1: "))
    l2 = int(input("Podaj liczbę 2: "))
    suma1 = 0
    suma2 = 0
    for i in range(1,l1):
        if l1%i==0:
            suma1+=i
    for i in range(1,l2):
        if l1%i==0:
            suma2+=i



def suma_cyfr(n):
    suma = 0
    while n > 0:
        suma+=n%10
        n = n // 10
    return suma