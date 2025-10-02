## Écrivez votre code ici !
class BankAccount:
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance

    def __str__(self):
        return f"Titulaire du compte : {self.holder}, solde : {self.balance} euros.\n"

    def deposit(self, amount):
        print(f"\nVous souhaitez ajouter : {amount} euros.")
        if amount > 0:
            self.balance += amount
            print(f"Vous avez déposé {amount} euros avec succés.")
        else:
            print("Le montant est négatif !")

        self.display_balance()

    def withdraw(self, amount):
        print(f"\nVous souhaitez retirer : {amount} euros.")
        if self.balance >= amount:
            self.balance -= amount
            print(f"Vous avez retirer {amount} euros avec succés.")
        else:
            print("Votre solde est insuffisant !")

        self.display_balance()

    def display_balance(self):
        print(f"Il reste {self.balance} euros sur votre compte.")

def main():
    bank_account = BankAccount("Nicolas", 1000)
    print(bank_account)
    bank_account.deposit(100)
    bank_account.deposit(-300)
    bank_account.withdraw(700)
    bank_account.withdraw(500)

if __name__ == "__main__":
    main()