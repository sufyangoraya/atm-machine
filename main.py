import streamlit as st
from datetime import datetime

# Initial account setup
if 'balance' not in st.session_state:
    st.session_state.balance = 10000  # Starting balance
    st.session_state.transactions = []

# Function to add a transaction
def add_transaction(type, amount):
    st.session_state.transactions.append({
        'type': type,
        'amount': amount,
        'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# Streamlit app
st.title("🏦 ATM Machine Simulator by Sufyan❤️")

menu = st.sidebar.selectbox("Select Option", ["Check Balance", "Withdraw", "Deposit", "Mini Statement"])

if menu == "Check Balance":
    st.subheader("💰 Your Current Balance")
    st.success(f"Rs: {st.session_state.balance}")

elif menu == "Withdraw":
    st.subheader("💸 Withdraw Money")
    amount = st.number_input("Enter amount to withdraw", min_value=100, step=100)
    if st.button("Withdraw"):
        if amount <= st.session_state.balance:
            st.session_state.balance -= amount
            add_transaction('Withdraw', amount)
            st.success(f"✅ Withdrawal Successful! New Balance: Rs: {st.session_state.balance}")
        else:
            st.error("❌ Insufficient Balance!")

elif menu == "Deposit":
    st.subheader("💵 Deposit Money")
    amount = st.number_input("Enter amount to deposit", min_value=100, step=100)
    if st.button("Deposit"):
        st.session_state.balance += amount
        add_transaction('Deposit', amount)
        st.success(f"✅ Deposit Successful! New Balance: Rs: {st.session_state.balance}")

elif menu == "Mini Statement":
    st.subheader("📜 Mini Statement")
    if st.session_state.transactions:
        for txn in reversed(st.session_state.transactions[-5:]):  # Last 5 transactions
            st.info(f"{txn['time']} | {txn['type']} | Rs: {txn['amount']}")
    else:
        st.warning("No transactions yet.")

st.sidebar.markdown("---")
st.sidebar.caption("Made with ❤️ by sufyan")
