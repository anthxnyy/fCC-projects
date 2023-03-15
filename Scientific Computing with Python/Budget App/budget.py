class Category:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ledger = []

    def deposit(self, amount: int, description="") -> None:
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: int, description="") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self) -> float:
        return sum([item["amount"] for item in self.ledger])

    def transfer(self, amount: int, category: str) -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount: int) -> bool:
        return amount <= self.get_balance()

    def __str__(self) -> str:
        return (
            self.name.center(30, "*")
            + "\n"
            + "\n".join(
                [
                    f"{item['description'][:23].ljust(23)}{format(item['amount'], '.2f').rjust(7)}"
                    for item in self.ledger
                ]
            )
            + f"\nTotal: {self.get_balance():.2f}"
        )

    def amount_spent(self) -> float:
        total_amount = 0
        for i in self.ledger:
            amount = i["amount"]
            if amount < 0:
                total_amount += amount
        return -total_amount


def create_spend_chart(categories):
    category_spendings = [category.amount_spent() for category in categories]
    total_category_spending = sum(category_spendings)
    category_percentages = [
        spending * 100 / total_category_spending
        for spending in category_spendings
    ]
    chart = ["Percentage spent by category"]
    for i in range(0, 11):
        line = 10 * (10 - i)
        plot = "{:>3}| ".format(line)
        for percentage in category_percentages:
            if percentage >= line:
                plot += "o  "
            else:
                plot += "   "
        chart.append(plot)
    padding = " " * 4
    chart.append(padding + "-" * 3 * len(category_spendings) + "-")

    category_titles = [category.name for category in categories]
    longest_category_title = max(map(len, category_titles))
    for i in range(0, longest_category_title):
        space = padding
        for category in category_titles:
            space += " "
            space += category[i] if len(category) > i else " "
            space += " "
        chart.append(space + " ")

    return "\n".join(chart)
