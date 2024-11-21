licznik = 0
while True:
   odpowiedz = input("Czy pada? (tak/nie/nie wiem): ").strip().lower()
   if odpowiedz == "tak":
       licznik += 1
   if odpowiedz == "nie" or odpowiedz == "nie wiem": break
      
print(f"Użytkownik odpowiedział 'tak' {licznik} razy.")
