from binance_client import BinanceClient
import os


api_key = os.getenv('API_KEY')
api_secret = os.getenv('API_SECRET')
print(f"API_KEY: {api_key}")
print(f"API_SECRET: {api_secret}")


bc = BinanceClient(api_key, api_secret)
print(f"BinanceClient: {bc}")

res = bc.system_status()
print(res)

try:
    res = bc.user_universal_transfer('MAIN_UMFUTURE', 'BTC', 0.0001)
    print(res)
except Exception as e:
    print(e.response.json())

try:
    res = bc.dust_transfer(['BTC', 'USDT'])
    print(res)
except Exception as e:
    print(e.response.json())

try:
    res = bc.withdraw('ETH', '')
    print(res)
except Exception as e:
    print(e.response.json())

try:
    res = bc.account_api_trading_status()
    print(res)
except Exception as e:
    print(e.response.json())

