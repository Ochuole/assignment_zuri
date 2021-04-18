class Budget:
    def __init__ (self,**categories):
        self.categories = categories
        print(self.categories)



    def deposit(self, deposit_amount, category):
        self.categories[category] = self.categories [category] + deposit_amount
        print("$" + str(deposit_amount) + " has been deposited into the " + category)

    def withdraw(self, withdrawal_amount, category):
        if withdrawal_amount > self.categories[category]:
            print("Insufficient Balance")
        else:
            self.categories[category] - withdrawal_amount
            print("You withdrew the sum of $" + str(withdrawal_amount) + " from the " + category)

    def transfer(self, transfer_amount,debitCategory, creditCategory):
        self.categories[debitCategory] = self.categories[debitCategory] = self.categories[debitCategory] - transfer_amount
        self.categories[creditCategory] = self.categories[creditCategory] = self.categories[debitCategory] + transfer_amount
        print("You transferred the sum of $" + str(transfer_amount) + " from the " + debitCategory + " into the " + creditCategory)

    def check_balance(self, category):
        print("Your " + category + " balance is $" + str(self.categories[category]))


mybudget = Budget(food_budget = 10000, clothing_budget = 2000, rent_budget = 30000, entertainment_budget = 1500)
mybudget.deposit(1500,"food_budget")
mybudget.withdraw(3000, "rent_budget")
mybudget.transfer(70, "entertainment_budget", "clothing_budget")
mybudget.check_balance("clothing_budget")