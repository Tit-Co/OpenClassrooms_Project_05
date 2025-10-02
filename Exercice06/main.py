# Fonction calculate_average
def calculate_average(numbers_list):
    the_average = sum(numbers_list) / len(numbers_list)
    return the_average

# Exemple d'utilisation de la fonction
numbers = [10, 20, 30, 40, 50]
average = calculate_average(numbers)
print("La moyenne est :", average)
