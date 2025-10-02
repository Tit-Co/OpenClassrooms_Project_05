def main():
    words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

    comprehension_list = [(word, len([lettre for lettre in list(word) if lettre in "aeiouy"])) for word in words]
    print(comprehension_list)

if __name__ == "__main__":
    main()
