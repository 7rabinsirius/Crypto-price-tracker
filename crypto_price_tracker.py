import requests
import streamlit as st
import smtplib
import matplotlib.pyplot as plt

def get_price(coin_id='bitcoin', currency='usd'):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies={currency}'
    response = requests.get(url)
    data = response.json()
    if coin_id not in data:
        st.error(f"Failed to retrieve {coin_id} price. Response: {data}")
        return None
    return data[coin_id][currency]

st.title("Crypto Price Tracker")
coins = ["bitcoin", "ethereum", "dogecoin"]
prices = {coin: get_price(coin) for coin in coins}
st.table(prices)


thresholds = {coin: st.number_input(f"{coin.capitalize()} alert price", min_value=0.0) for coin in coins}



def send_alert_email(coin, price):
    msg = f"{coin.capitalize()} has reached ${price}"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('your_email@example.com', 'your_password')  # Use environment variables instead!
    server.sendmail('your_email@example.com', 'recipient@example.com', msg)
    server.quit()



# Example: collect historical data
historical_prices = {coin: [] for coin in coins}

for coin in coins:
    price = get_price(coin)
    prices[coin] = price
    if price is not None:
        historical_prices[coin].append(price)
        st.subheader(f"{coin.capitalize()} Price Trend")
        st.line_chart(historical_prices[coin])