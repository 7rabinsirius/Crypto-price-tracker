# Crypto-price-tracker


# Crypto Price Tracker

A simple yet powerful Streamlit app that tracks real-time prices of popular cryptocurrencies and alerts users via email when the price crosses a custom threshold.

---

## Features

-  Real-time price tracking using CoinGecko API  
-  Customizable alert prices for Bitcoin, Ethereum, and Dogecoin  
-  Email notifications when a coin reaches its set threshold  
-  Price trend visualization using Streamlit charts  

---

## 🔧 Technologies Used

| Tool         | Purpose                                  |
|--------------|-------------------------------------------|
| Python       | Core programming language                 |
| Streamlit    | Web app UI and interactivity              |
| Requests     | Fetch crypto prices from CoinGecko API    |
| smtplib      | Send email alerts                         |
| Matplotlib   | (Optional) For advanced plotting          |

---

## 🛠️ Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/crypto-price-tracker.git
   cd crypto-price-tracker
   ```

2. **Install dependencies**
   ```bash
   pip install streamlit requests matplotlib
   ```

3. **Set up environment variables**
   Create a `.env` file:
   ```ini
   EMAIL_USER=your_email@example.com
   EMAIL_PASS=your_secure_password
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 🔒 Important Notes

- ⚠️ **Never hardcode email credentials!** Use environment variables or a secure vault.  
- ✅ CoinGecko API doesn’t need authentication on the free tier.  
- 🛡️ For Gmail alerts, enable [App Passwords](https://support.google.com/accounts/answer/185833?hl=en) if using 2FA.  

---


