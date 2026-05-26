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