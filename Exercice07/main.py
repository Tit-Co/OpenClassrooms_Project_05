## Écrivez votre code ici !
def square(x):
    if x.isdigit():
        print(f"Le carré de {x} est : {int(x) ** 2}")
        return int(x) ** 2
    else:
        try:
            print(f"Le carré de {x} est : {float(x) ** 2}")
            return float(x) ** 2
        except ValueError as e:
            print(f"Erreur : {e} - Le paramètre doit être un nombre !")
            return None


def main():
    nombre = input("Entrer un nombre :")
    square(nombre)

if __name__ == "__main__":
    main()

