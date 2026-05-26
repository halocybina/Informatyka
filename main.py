import os

print("Wybierz lekcję do uruchomienia:")
print("1. Etapy rozwiązywania problemów")
print("2. Podstawy Pythona")
print("3. Funkcja matematyczna i złożone operatory przypisania")
print("4. Instrukcje warunkowe")
print("5. Instrukcje iteracyjne")
print("6. Funkcje w Pythonie")
print("7. Algorytm Euklidesa")
print("7.1. Zadanie (NWW i NWD)")
print("8. Badanie czy liczba jest pierwsza")
print("9. Listy - sekwencyjne typy danych")
print("10. Liniowe porządkowanie ciągu liczbowego - sortowanie bąbelkowe")
print("11. Sortowanie przez wstawianie")
print("12. Algorytmy na tekstach")

wybor = input("Twój wybór (1-10): ")

if wybor == "1":
    os.system("python3 1_etapy_rozwiązywania_problemów_za_pomocą_komputera.py")
elif wybor == "2":
    os.system("python3 2_Podstawy_pythona.py")
elif wybor == "3":
    os.system("python3 3_Instrukcje_warunkowe_w_Pythonie.py")
elif wybor == "4":
    os.system("python3 4_Instrukcje_iteracyjne.py")
elif wybor == "5":
    os.system("python3 5_Instrukcje_warunkowe_w_Pythonie.py")
elif wybor == "6":
    os.system("python3 6_Funkcje_w_pythone.py")
elif wybor == "7":
    os.system("python3 7_Algorytm_Eukildesa.py")
elif wybor == "7.1":
    os.system("python3 7_zadanie.py")
elif wybor == "8":
    os.system("python3 8_Badanie_czy_liczba_jest_pierwsza.py")
elif wybor == "9":
    os.system("python3 9_Listy_-_sekwencyjne_typy_danych.py")
elif wybor == "10":
    os.system("python3 10_Liniowe_porzadkowanie_ciagu_liczbowego_-_sortowanie_babelkowe.py")
elif wybor == "11":
    os.system("python3 11_Sortownaie_przez_wstawianie.py")
elif wybor == "12":
    os.system("python3 12_Algorytmt_na_tekstach.py")
else:
    print("Nieprawidłowy wybór")
