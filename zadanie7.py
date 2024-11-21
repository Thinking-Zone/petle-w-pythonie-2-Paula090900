import random
poprawna_odpowiedz = False
while not poprawna_odpowiedz:
   pogoda = random.choice(["Pada", "Nie pada"])
   print("Czy pada? (tak/nie)")
   odpowiedz = input().strip().lower()
   if (pogoda == "Pada" and odpowiedz == "tak") or (pogoda == "Nie pada" and odpowiedz == "nie"):
       print("Poprawna odpowiedź!")
       poprawna_odpowiedz = True
   else:
       print("Niepoprawna odpowiedź. Spróbuj ponownie.")
