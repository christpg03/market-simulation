import random
from models.buyer import Buyer, Offer
from models.seller import Seller, Sale
from models.transaction import Transaction


class Market:
    def __init__(self, product_id: int, buyers_list: list[Buyer], sellers_list: list[Seller]):
        self.product_id: int = product_id
        self.buyers_list: list[Buyer] = buyers_list
        self.sellers_list: list[Seller] = sellers_list
        self.historical_transactions: list[Transaction] = []
        self.current_price: float = random.uniform(20, 100)

    def update(self):
        transaction = None

        offers: list[Offer] = [b.offer(self.current_price) for b in self.buyers_list]
        sales: list[Sale] = [s.sell(self.current_price) for s in self.sellers_list]

        max_offer: Offer = max(offers, key=lambda x: x.offer)
        max_sale: Sale = max(sales, key=lambda x: x.sale)

        print(f"Current price: {self.current_price}")
        print(f"Max offer: {max_offer.offer} Max sale: {max_sale.sale}")

        if max_offer.offer >= max_sale.sale > 0 and max_sale.sale > 0:
            new_current_price: float = (max_offer.offer + self.current_price) / 2
            transaction = Transaction(max_offer.buyer, max_sale.seller, self.current_price, new_current_price,
                                      max_offer.offer)
            self.current_price = new_current_price
        else:
            self.current_price -= random.uniform(0, self.current_price * 0.05)

        self.historical_transactions.append(transaction)
