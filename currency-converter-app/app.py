import json
import streamlit as st

# Load exchange rates
with open("rates.json") as f:
    data = json.load(f)

rates = data["rates"]
currencies = list(rates.keys())

# Page title
st.title("Currency Converter")

# Input amount
amount = st.number_input("Amount", value=100.0, min_value=0.0)

# Select currencies
col1, col2 = st.columns(2)

with col1:
    source = st.selectbox("From", currencies, index=currencies.index("USD"))

with col2:
    target = st.selectbox("To", currencies, index=currencies.index("CNY"))

# Convert
if amount >= 0:
    result = amount * (rates[target] / rates[source])
    st.markdown(f"## {amount} {source} = **{result:.2f} {target}**")
