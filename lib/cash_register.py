class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount          # uses the setter
        self.total = 0
        self.items = []
        self.previous_transactions = []

    # --- Property ---

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if not isinstance(value, int) or not (0 <= value <= 100):
            print("Not valid discount")
            self._discount = 0
        else:
            self._discount = value

    # --- Methods ---

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if not self.discount:
            print("There is no discount to apply.")
            return
        self.total = self.total * (1 - self.discount / 100)
        print(f"After the discount, the total comes to ${int(self.total)}.")

    def void_last_transaction(self):
        if not self.previous_transactions:
            print("No transactions to void.")
            return
        last = self.previous_transactions.pop()
        self.total -= last["price"] * last["quantity"]
        self.items.remove(last["item"])
        print(f"Voided: {last['item']} — removed ${last['price'] * last['quantity']:.2f} from total.")
