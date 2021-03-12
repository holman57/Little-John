from Robinhood import Robinhood
from secrets import Secrets


robinhood_client = Robinhood()
robinhood_client.login(username=Secrets.robinhood_username,
                       password=Secrets.robinhood_password,
                       qr_code=Secrets.robinhood_qr_code)

stock_instrument = robinhood_client.instruments('MSFT')[0]
stock_quote = robinhood_client.quote_data('MSFT')
print(stock_quote['last_trade_price'])














