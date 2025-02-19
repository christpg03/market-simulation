import random


class Buyer:
    def __init__(self, buyer_id: int, budget: float = 0):
        self.id: int = buyer_id
        if budget == 0:
            self.budget = random.uniform(20, 100)
        else:
            self.budget = budget

    def offer(self, current_price: float):
        print(f"Buyer: {self.id}, Budget: {self.budget:.2f}")
        new_offer: float = 0
        if self.budget >= current_price:
            increment = random.uniform(0, min(5, int(self.budget - current_price)))
            new_offer = self.budget + increment
        return Offer(self, new_offer)


class Offer:
    def __init__(self, buyer: Buyer, offer: float):
        self.buyer = buyer
        self.offer = offer
