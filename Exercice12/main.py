class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []
        self.borrow_books = []

    # Ajouter les méthodes ici

    def add_book(self, book):
        self.books.append(book)
        print(f"On ajoute {book.title} à la liste des livres disponibles.")

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return
        print("Livre non trouvé")

    def borrow_book(self, book_title):
        print(f"Vous souhaitez emprunter le livre : {book_title}")
        for book in self.books:
            if book.title == book_title:
                self.borrow_books.append(book)
                self.books.remove(book)
                print(f"{book.title} ajouté à la liste des livres empruntés.")
                return
        print("Livre non trouvé dans les livres disponibles")

    def return_book(self, book_title):
        print(f"Vous souhaitez rendre le livre : {book_title}")
        for book in self.borrow_books:
            if book.title == book_title:
                self.borrow_books.remove(book)
                self.add_book(book)
                print(f"{book.title} est retourné et ajouté à la liste des livres disponibles.")
                return
        print("Le livre n'est pas référencé comme emprunté.")

    def available_books(self):
        return [book.title for book in self.books]

    def borrowed_books(self):
        return [book.title for book in self.borrow_books]

def main():
    library = Library()
    library.add_book(Book("La Marquise", "Jean Dupont", 1999))
    library.add_book(Book("La Sphère Noire", "Peter Smith", 2010))
    print(f"Livres disponibles : {library.available_books()}")

    library.borrow_book("La Sphère Noire")
    print(f"Livres empruntés : {library.borrowed_books()}")
    print(f"Livres disponibles : {library.available_books()}")

    library.return_book("La Marquise")
    print(f"Livres empruntés : {library.borrowed_books()}")
    print(f"Livres disponibles : {library.available_books()}")

    library.borrow_book("La Sphère Noire")
    print(f"Livres empruntés : {library.borrowed_books()}")
    print(f"Livres disponibles : {library.available_books()}")

if __name__ == "__main__":
    main()
