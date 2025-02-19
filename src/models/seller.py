import random


class Seller:
    def __init__(self, seller_id: int, minimum_selling_price: float = 0):
        self.id: int = seller_id
        if minimum_selling_price == 0:
            self.minimum_selling_price: float = random.uniform(20, 100)
        else:
            self.minimum_selling_price: float = minimum_selling_price

    def sell(self, current_price: float):
        print(f"Seller: {self.id}, Budget: {self.minimum_selling_price:.2f}")
        price: float = 0
        if current_price >= self.minimum_selling_price:
            decrease: float = random.uniform(0, min(5, int(current_price - self.minimum_selling_price)))
            price = max(current_price - decrease, self.minimum_selling_price)
        return Sale(self, price)


class Sale:
    def __init__(self, seller: Seller, sale: float):
        self.seller = seller
        self.sale = sale
