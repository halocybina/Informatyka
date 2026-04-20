# Temat: Liniowe porządkowanie ciągu liczbowego - sortowanie bąbelkowe
# Rodzaje ciągów liczbowych:

rosnacy = [1,2,3,4,5,6,7,8,9,10] # rosnący
niemalejacy = [1,2,2,3,4,4,5,6,7,8,9,10] # niemalejący
malejacy = [10,9,8,7,6,5,4,3,2,1] # malejący
nierosnacy = [10,9,8,8,7,6,5,5,4,3,2,1] # nierosnący
staly = [1,1,1,1,1,1,1,1,1,1] # stały

# Napisz funkcję logiczną sprawdzającą czy ciąg jest rosnący
def czy_rosnacy(lista):
    for i in range(len(lista)-1):
      if lista[i] >= lista[i+1]:
         return False
    return True

# Napisz funkcję logiczną sprawdzającą czy ciąg jest niemalejący
def czy_niemalejacy(lista):
    for i in range(len(lista)-1):
      if lista[i] > lista[i+1]:
         return False
    return True

#  Napisz funkcję logiczną sprawdzającą czy ciąg jest malejący
def czy_malejacy(lista):
    for i in range(len(lista)-1):
      if lista[i] <= lista[i+1]:
         return False
    return True

# Napisz funkcję logiczną sprawdzającą czy ciąg jest nierosnący
def czy_nierosnacy(lista):
    for i in range(len(lista)-1):
      if lista[i] < lista[i+1]:
         return False
    return True

# Napisz funkcję logiczną sprawdzającą czy ciąg jest stały
def czy_staly(lista):
    for i in range(len(lista)-1):
      if lista[i] != lista[i+1]:
         return False
    return True