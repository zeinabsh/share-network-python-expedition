# ===============================
# Green-Spend Tracker Script
# ===============================

# 1. Data Entry: Initialize account
user_name = input("Enter your name: ").strip()  # String formatting (strip)
starting_deposit = float(input("Enter starting deposit: "))
balance = starting_deposit
account_active =  input("Enter your states: ")

# 2. Batch Initialization

# 3. Transaction Input

purchase_description = input("Enter purchase description: ").strip()
purchase_amount = float(input("Enter purchase amount: "))

# 4. Financial Calculation: Add sales tax and deduct from balance
tax_rate = 0.10  
total_purchase = purchase_amount * (purchase_amount + tax_rate)
balance -= total_purchase

# 5. Validation Logic
if account_active == "Active" and  balance >= total_purchase:
  print(f"Transaction successful! Total purchase: ${total_purchase:.2f}")
  print(f"Remaining balance: ${balance:.2f}")

   
elif balance < total_purchase:
    print("Insufficient funds for this transaction.")
else:
    print("Account is inactive. Cannot proceed with transaction.")

# Bonus points for "Green" purchase
if "green" in purchase_description.lower():
    print("Bonus")

# Display final account summary
print("\n--- Account Summary ---")
print(f"User: {user_name}")
print(f"Starting Deposit: ${starting_deposit:.2f}")
print(f"Current Balance: ${balance:.2f}")

