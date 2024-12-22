import random

while True:
    print("Lance les dés")
    liste = ['1', '2', '3', '4', '5', '6']
    chiffre_aleatoire = random.choice(liste)
    print(f"Le dé est tombé sur : {chiffre_aleatoire}")
    
    print("Voulez-vous relancer le dé ? 'yes' or 'no'")
    user_input = input("> ").lower()
    
    if user_input == "no":
        break
