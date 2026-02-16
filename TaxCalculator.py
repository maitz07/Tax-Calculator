import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Tax Calculator Web App")

income = st.number_input("Enter Annual Income (₹):", min_value=0.0, step=10000.0)

# -------------------------
# Old Regime Calculation
# -------------------------
def old_regime_tax(income):
    tax = 0
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = 12500 + (income - 500000) * 0.20
    else:
        tax = 112500 + (income - 1000000) * 0.30
    return tax

# -------------------------
# New Regime Calculation
# -------------------------
def new_regime_tax(income):
    tax = 0
    if income <= 300000:
        tax = 0
    elif income <= 600000:
        tax = (income - 300000) * 0.05
    elif income <= 900000:
        tax = 15000 + (income - 600000) * 0.10
    elif income <= 1200000:
        tax = 45000 + (income - 900000) * 0.15
    elif income <= 1500000:
        tax = 90000 + (income - 1200000) * 0.20
    else:
        tax = 150000 + (income - 1500000) * 0.30
    return tax

# -------------------------
# Flat Tax (20%)
# -------------------------
def flat_tax(income):
    return income * 0.20

# Calculate taxes
old_tax = old_regime_tax(income)
new_tax = new_regime_tax(income)
flat = flat_tax(income)

# Add 4% Cess
old_total = old_tax * 1.04
new_total = new_tax * 1.04
flat_total = flat * 1.04

if income > 0:
    st.subheader("Tax Summary (Including 4% Cess)")
    st.write(f"Old Regime Tax: ₹{old_total:,.2f}")
    st.write(f"New Regime Tax: ₹{new_total:,.2f}")
    st.write(f"Flat Tax (20%): ₹{flat_total:,.2f}")

    min_tax = min(old_total, new_total, flat_total)

    if min_tax == old_total:
        st.success("Old Regime is the most beneficial.")
    elif min_tax == new_total:
        st.success("New Regime is the most beneficial.")
    else:
        st.success("Flat Tax System is the most beneficial.")

# -------------------------
# Graphs
# -------------------------
income_range = np.linspace(0, 2000000, 100)

old_list = [old_regime_tax(i) * 1.04 for i in income_range]
new_list = [new_regime_tax(i) * 1.04 for i in income_range]
flat_list = [flat_tax(i) * 1.04 for i in income_range]

# Graph 1: Income vs Total Tax
plt.figure()
plt.plot(income_range, old_list, label="Old Regime")
plt.plot(income_range, new_list, label="New Regime")
plt.plot(income_range, flat_list, label="Flat Tax")
plt.xlabel("Income")
plt.ylabel("Total Tax")
plt.title("Income vs Total Tax")
plt.legend()
st.pyplot(plt)

# Graph 2: Effective Tax Rate
plt.figure()
plt.plot(income_range, np.array(old_list)/income_range, label="Old Regime")
plt.plot(income_range, np.array(new_list)/income_range, label="New Regime")
plt.plot(income_range, np.array(flat_list)/income_range, label="Flat Tax")
plt.xlabel("Income")
plt.ylabel("Effective Tax Rate")
plt.title("Income vs Effective Tax Rate")
plt.legend()
st.pyplot(plt)
