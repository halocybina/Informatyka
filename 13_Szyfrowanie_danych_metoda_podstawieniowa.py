# Temat: Szyfrowanie danych metodą podstawieniową - szyfr Cezara
'''
kryptologia:
kryptografia - szyfrowanie
kryptoanaliza - deszyfrowanie
szyfrogram, kryptogram - tekst zaszyfrowany
tekst jawny - tekst do zaszyfrowania
'''
# Zaszyfruj tekst SOS za pomocą szyfru Cezara z przesunięciem o 10
# SZYFROGRAM: CYC

def szyfr_cezara(slowo, klucz):
  zaszyfrowane = ""
  klucz = klucz % 26
  for znak in slowo:
    if znak.isalpha():
      przesuniecie = ord(znak) + klucz
      if znak.islower():
        zaszyfrowane+=chr((przesuniecie - ord("a"))%26 + ord("a"))
      else:
         zaszyfrowane+=chr((przesuniecie - ord("A"))%26 + ord("A"))
    else:
       zaszyfrowane+=znak
  return zaszyfrowane
print(szyfr_cezara("SOS", 10)) 
print(szyfr_cezara("klasa 3i2T", 10))
print(szyfr_cezara("uvkck 3s2D", 10))