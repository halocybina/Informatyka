# Temat: Liniowe porządkowanie ciągu liczbowego - sortowanie bąbelkowe
# Rodzaje ciągów liczbowych:
from subprocess import BELOW_NORMAL_PRIORITY_CLASS

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

# Sortowanie bąbelkowe
# i = 0  1  2  3  4
#     9, 7, 4, 2, 5
# 1 pętla zewnętrzna
#                     1 por 9>7  7,9,4,2,5
# pętla wewnętrzna    2 por 9>4  7,4,9,2,5
#                     3 por 9>2  7,4,2,9,5
#                     4 por 9>5  7,4,2,5,9
# 2 pętla zewnętrzna
#                     1 por 7>4  4,7,2,5,9
# pętla wewnętrzna    2 por 7>2  4,2,7,5,9
#                     3 por 7>5  4,2,5,7,9
# 3 pętla zewnętrzna
#                     1 por 4>2  2,4,5,7,9
# pętla wewnętrzna    2 por 4>5  2,4,5,7,9
# 4 pętla zewnętrzna
# pętla wewnętrzna    1 por 2>4  2,4,5,7,9

def sortowanie_babelkowe(lista):
    for i in range(len(lista)-1):
        zmiana = False
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                zmiana = True
        if not zmiana:
             break
    return lista

print(sortowanie_babelkowe([9,7,4,2,5]))

