from models.buyer import Buyer
from models.seller import Seller
from models.market import Market

import random
import time

TRANSACTIONS = 100
BUYERS = random.randint(1, 10)
SELLERS = random.randint(1, 10)

buyers = [Buyer(b) for b in range(1, BUYERS + 1)]
sellers = [Seller(s) for s in range(1, SELLERS + 1)]
market = Market(1, buyers, sellers)

while TRANSACTIONS > 0:
    market.update()
    # for t in market.historical_transactions:
    #     if t is not None:
    #         print(t.new_market_price)
    #     else:
    #         print(-1)
    last_transaction = market.historical_transactions[len(market.historical_transactions) - 1]
    if last_transaction is not None:
        print(last_transaction.new_market_price)
    else:
        print(None)
    TRANSACTIONS -= 1
    input()
