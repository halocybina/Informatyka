# Temat: Pozycyjne systemy liczbowe. Konwersja między systemami.
# Systemy liczbowe
# binarny: 0-1
# ósemkowy: 0-7
# szesnatkowy: 0-9, A-F (10-15)
'''
125(10) = 1111101(2)
125//2 = 62 reszta 1
62//2 = 31 reszta 0
31//2 = 15 reszta 1
15//2 = 7 reszta 1
7//2 = 3 reszta 1
3//2 = 1 reszta 1
1//2 = 0 reszta 1

327(10) = 517(8)
327//8 = 40 reszta 7
40//8 = 5 reszta 0
5//8 = 0 reszta 5

1231(10) = 4CF(16)
1231//16 = 76 reszta 15(F)
76//16 = 4 reszta 12(C)
4//16 = 0 reszta 4
'''
def hexa(liczba):
  s="0123456789ABCDEF"
  return s[liczba]

def konwersja(liczba, system):
  wynik = ""
  while liczba > 0:
    reszta = liczba % system
    wynik = hexa(reszta) + wynik
    liczba//=system
  return wynik

print(konwersja(125, 2))
print(konwersja(327, 8))
print(konwersja(1231, 16))
      
'''
1101(2) = 1*2^3 + 1*2^2 + 0*2^1 + 1*2^0 = 8 + 4 + 0 + 1 = 13(10)
'''
def kowersja1(liczba:str, system:int) -> int:
  potega = len(liczba)-1
  wynik = 0
  for i in range(len(liczba)):
    wynik += int(liczba[i])*system**potega
    potega -= 1
  return wynik

print(kowersja1("1101", 2))

# Napisz funkcję hexa1(liczba), która zamienia liczbę dziesiętną na szesnastkową
def hexa1(liczba):
   return hex(liczba)[2:]
   # return format(liczba, "x")
print(hexa1(1231))
    


  