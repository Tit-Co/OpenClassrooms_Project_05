def main():
    students = {
    'Alice': {
         'Mathematiques': 90,
         'Francais': 80,
         'Histoire': 95
    },
    'Bob': {
         'Mathematiques': 75,
         'Francais': 85,
         'Histoire': 70
    },
     'Charlie': {
         'Mathematiques': 88,
         'Francais': 92,
         'Histoire': 78
     }
    }

    user = input("Entrez le nom de l’étudiant : ")

    if user in students:
        moyenne = 0
        for matiere, note in students[user].items():
                print(f"{matiere} : \nNotes de {user} : {note}\n")
                moyenne += note
        print(f"Moyenne de {user} : {moyenne/3}")
    else:
        print(f"L'étudiant {user} n'existe pas dans la liste.")



if __name__ == '__main__':
    main()
