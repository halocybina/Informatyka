# Temat: Algorytmy na tekstach
print(type("slowo"))
print(str(12))

# Słowa to sekwencyjne typy danych, ale są niemodyfikowalne

#      0 1 2.........
slowo="informatyka"
#      .......-2 -1

print(slowo[0])
print(slowo[-1])

# wycinek - nazwa[start:stop:step]

tekst = "ABCDEFGH"
print(tekst)
print(tekst[2])
print(tekst[1::2])
print(tekst[::-1])
print(tekst[::2])
print(tekst[:-4:-2])
print(tekst[:3:2])
print(tekst[2::2])

for i in tekst:
  print(i, end=" ")
for i in range(len(tekst)):
   print(tekst[i], end=" ")
print()

# jeżeli chcemy dokonać zmiany w słowie to tworzymy nową zmienną pustą tekstową i dokładamy do niej elementy
s=""
for i in slowo:
  if i== "a":
    s+="*"
  else:
    s+=i
print(s)

# drugi sposób dokonywania zmian w tekście to zamiana słowa na listę znaków 
l=list(slowo)
for i in range(len(l)):
  if l[i] == "a":
    l[i] = "*"
  print("".join(l))

# Zdefiniuj funkcję ile(s), której parametrem jest ciąg znaków, a wynikiem – lista czterech liczb całkowitych oznaczających, ile razy symbole A, C, G i T występują w tym ciągu znaków. Sprawdź działanie funkcji dla podanych poniżej parametrów.
def ile(s):
  a=0
  c=0
  t=0
  g=0
  for i in s:
    if i =="A":
      a+=1
    elif i =="C":
      c+=1
    elif i =="T":
      t+=1
    elif  i =="G":
      g+=1
  return[a,c,t,g]
print(ile("CAATAAAAA"))

# Zdefiniuj funkcję pary(s), której parametrem jest łańcuch DNA, a wynikiem – liczba wystąpień par jednakowych symboli. Sprawdź działanie funkcji dla podanych poniżej parametrów.
def pary(s):
  pary=0
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      pary+=1
  return pary
print(pary("TGATTCTGAACAAGTGTT"))

# Odwrotne uzupełnienie łańcucha DNA to ciąg utworzony przez odwrócenie dane­go ciągu i dopełnienie każdego symbolu, tj. zamiany A na T i odwrotnie oraz C na G i odwrotnie (np. CTGA → AGTC → TCAG). Zdefiniuj funkcję oduz(s), której parametrem jest łańcuch DNA, a wynikiem jego odwrotne uzupełnienie. Sprawdź działanie funkcji dla podanych poniżej parametrów.
def oduz(s):
  s = s[::-1]
  text=""
  for i in s:
    if i == "A":
       text+="T"
    if i == "T":
      text+="A"
    if i == "C":
      text+="G"
    if i == "G":
      text+="C"
  return text
print(oduz("TGACCCA"))

# Zdefiniuj funkcję ta(s), której parametrem jest łańcuch DNA, a wynikiem – łańcuch DNA z gwiazdką (*) w miejscu symboli C, G i T. Sprawdź działanie funkcji dla podanych poniżej parametrów.
def ta(s):
  wynik=""
  for i in s:
    if i == "A":
      wynik+="A"
    else:
      wynik+="*"
  return wynik
print(ta("TGACCCA"))
# Zdefiniuj funkcję codruga(napis), której wynikiem jest napis z pominiętym co drugim znakiem. Sprawdź działanie funkcji dla podanych poniżej parametrów.
def codruga(napis):
  wynik=""
  for i in range(0, len(s), 2):
      wynik+=napis[i]
  return wynik
print(codruga("aksamitka"))

# Zdefiniuj funkcję wspak(napis), której wynikiem jest napis ze znakami przestawionymi od końca dopoczątku. Rozwiązanie zapisz za pomocą pętli. Sprawdź działanie funkcji dla podanych poniżej parametrów.
def wspak(napis):
  wynik=""
  for i in range(len(napis)-1, -1, -1):
    wynik+=napis[i]
  return wynik
print(wspak("aloes"))
# Zdefiniuj funkcję lustro(napis), której wynikiem jest napis z połączonym napisem wspak. Sprawdź działanie funkcji dla podanych poniżej parametrów.
def lustro(napis):
  return napis + wspak(napis)
print(lustro("aster"))

# Zdefiniuj funkcję czy_palindrom(napis), której wynikiem jest True, jeśli napis jest palindromem, a False w przeciwnym przypadku.
def czy_palindrom(napis):
  napis=napis.replace(" ", "")
  return napis == wspak(napis)
print(czy_palindrom("kajak"))
print(czy_palindrom("kamil ślimak"))

# Zdefiniuj funkcję czy_anagram(napis1, napis2), której wynikiem jest True, jeśli napisy są anagramami, a False w przeciwnym przypadku.
def czy_anagram(napis1, napis2):
  napis1 = sorted(napis1)
  napis2 = sorted(napis2)
  return napis1 == napis2
print(czy_anagram("arbuz", "burza"))