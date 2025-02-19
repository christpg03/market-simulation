from models.buyer import Buyer
from models.seller import Seller


class Transaction:
    def __init__(self, buyer: Buyer, seller: Seller, old_market_price: float, new_market_price: float,
                 transaction_price: float):
        self.buyer: Buyer = buyer
        self.seller: Seller = seller
        self.old_market_price: float = old_market_price
        self.new_market_price: float = new_market_price
        self.transaction_price: float = transaction_price
