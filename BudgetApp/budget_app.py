# Complete the Category class in budget.py.
# It should be able to instantiate objects based on different budget categories like food, clothing, and entertainment.
# When objects are created, they are passed in the name of the category.
# The class should have an instance variable called ledger that is a list.

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()


# A deposit method that accepts an amount and description. If no description is given, it should be an empty string.
# The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.

    def deposit(self, amount, description=""):
        self.deposit_amount = amount
        self.deposit_description = description
        self.deposit_dict = dict()
        self.deposit_dict["amount"] = self.deposit_amount
        self.deposit_dict["description"] = self.deposit_description
        self.ledger.append(self.deposit_dict)


# A withdraw method that is similar to the deposit method, but the amount passed in ledger should be a negative number.
# If there are not enough funds, nothing should be added to the ledger.
# This method should return True if the withdrawal took place, and False otherwise.

    def withdraw(self, amount, description=""):
        self.withdraw_amount = amount * -1
        self.withdraw_description = description
        self.withdraw_dict = dict()
        if self.check_funds(self.withdraw_amount * -1) is True:
            self.withdraw_dict["amount"] = self.withdraw_amount
            self.withdraw_dict["description"] = self.withdraw_description
            self.ledger.append(self.withdraw_dict)
            return True
        else:
            return False


# A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals.

    def get_balance(self):
        total = 0
        for item in range(len(self.ledger)):
            total += self.ledger[item]["amount"]
        return total

# A transfer method that accepts an amount and another budget category as arguments.
# The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]".
# Then it should add a deposit to the other category with the description "Transfer from [Source Budget Category]".
# If there are not enough funds, nothing should be added to either ledgers.
# This method should return True if the transfer took place, and False otherwise.

    def transfer(self, amount, destination):
        self.transfer_amount = amount
        self.description = destination
        if self.check_funds(self.transfer_amount) is True:
            self.withdraw(amount, "Transfer to " + destination.name)
            destination.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False

# A check_funds method that accepts an amount as an argument.
# It returns False if the amount is greater than the balance of the budget category and returns True otherwise.
# This method should be used by both the withdraw method and transfer method.

    def check_funds(self, amount):
        balance = self.get_balance()
        check_balance = balance - amount
        if check_balance >= 0:
            return True
        else:
            return False

# When the budget object is printed it should display:
# A title line of 30 characters where the name of the category is centered in a line of * characters.
# A list of the items in the ledger. Each line should show the description and amount.
# The first 23 characters of the description should be displayed, then the amount.
# The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
# A line displaying the category total.

    def __str__(self):
        amount = []
        description = []
        for thing in range(len(self.ledger)):
            amount.append(str("{:.2f}".format(self.ledger[thing]["amount"])))
            description.append(str(self.ledger[thing]["description"]))
        final_string = "\n".join("{:<23s}{:>7s}".format(x[:23], y) for x, y in zip(description, amount))
        total_amount = self.get_balance()
        return "{:*^30s}\n{}\nTotal: {}".format(self.name, final_string, total_amount)


# Create a function (outside of the class) called create_spend_chart that takes a list of categories as an argument.
# It should return a string that is a bar chart.
# The chart should show the percentage spent in each category passed in to the function.
# The percentage spent should be calculated only with withdrawals and not with deposits.
# Down the left side of the chart should be labels 0 - 100.
# The "bars" in the bar chart should be made out of the "o" character.
# The height of each bar should be rounded down to the nearest 10.
# The horizontal line below the bars should go two spaces past the final bar.
# Each category name should be written vertically below the bar.
# There should be a title at the top that says "Percentage spent by category".

def create_spend_chart(categories):
    amounts = dict()
    rounded_total = list()

    for category in categories:
        category.total = 0
        for item in range(len(category.ledger)):
            if category.ledger[item]["amount"] < 0:
                category.total += category.ledger[item]["amount"] * -1
                amounts[category.__dict__["name"]] = category.total

    total_categories = 0
    category_names = list()
    for key, value in amounts.items():
        total_categories += value
        category_names.append(key)
    for key, value in amounts.items():
        amounts[key] = value/total_categories
    for key, value in amounts.items():
        if int(str(value).split(".")[1][1]) <= 9:
            rounded_total.append(int(str(value).split(".")[1][0])*10)
    title = "Percentage spent by category\n"
    count = 100

    while count >= 0:
        circles = ""
        for percent in rounded_total:
            if percent >= count:
                circles += "o" + "  "
            if percent < count:
                circles += "   "
        if count == 0:
            title += str(count).rjust(3) + "|" + " " + circles + "\n"
            break
        else:
            title += str(count).rjust(3) + "|" + " " + circles + "\n"
        count -= 10

    title += "    " + "---" * len(rounded_total) + "-" + "\n"
    sorted_names = sorted(category_names, key=len)
    longest_name = len(sorted_names[-1])
    name_count = 0
    while name_count <= longest_name:
        names = ""
        for name in category_names:
            if len(name) <= name_count:
                names += "   "
            elif len(name) > name_count:
                names += name[name_count] + "  "
        if name_count == longest_name - 1:
            title += "     " + names
            break
        else:
            title += "     " + names + "\n"
        name_count += 1
    return title

