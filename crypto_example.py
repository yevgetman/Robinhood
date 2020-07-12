from Robinhood import Robinhood
import schedule
import time

# Create instance of Robinhood class 
rh = Robinhood(True) # pass crypto flag as True (default False)

# Login 
rh.login(
    username="<your_robinhood_username>",
    password="<your_robinhood_password", 
    qr_code="MFA_QR_code" # optional (MFA handled via SMS if omitted)
)

# Cryptocurrency to be traded
# Options: (BTN, BCH, BSV, BTG, DASH, DOGE, ETC, ETH, LSK, LTC, NEO, OMG, QTUM, XLM, XMR, XRP, ZEC)
# See https://nummus.robinhood.com/currency_pairs/ for up-to-date list
symbol = 'BTC'

# View your cryptocurrency holdings
holdings = rh.holdings_crypto()
print(holdings['results'])

# Get current price quote
quote = rh.quote_crypto(symbol)
print(quote)

# Place a buy order
res = rh.place_order_crypto(
        symbol,            
        price=round(float(quote['mark_price']) * 1.005, 2),
        quantity="0.0005",
        side="buy",
        time_in_force="gtc",
        type="market"
    )

print(res)