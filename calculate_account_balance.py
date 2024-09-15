customers_and_balances = [{1: 10000}, {2: 7500}, {3: 15000}]

transactions = [
    {"customer_id": 1, "type": "deposit", "amount": 500},
    {"customer_id": 2, "type": "deposit", "amount": 1000},
    {"customer_id": 3, "type": "withdrawal", "amount": 200},
    {"customer_id": 1, "type": "withdrawal", "amount": 100},
    {"customer_id": 2, "type": "withdrawal", "amount": 150},
    {"customer_id": 3, "type": "deposit", "amount": 300},
    {"customer_id": 1, "type": "deposit", "amount": 250},
    {"customer_id": 2, "type": "deposit", "amount": 400},
    {"customer_id": 3, "type": "withdrawal", "amount": 50},
    {"customer_id": 1, "type": "withdrawal", "amount": 200}
]

def calculate_balance():
    
    # Figure out how to return to the input selection if either of the following checks are not met
    try:
        customer_id = int(input("Please enter customer ID: "))
    except ValueError:
        print("Please enter a valid customer ID")
        return
    
    if customer_id not in customers_and_balances:
        print("Customer ID not found")
        return

    customer_balance = customers_and_balances[customer_id]
    
    # Calculate transactions for selected customer id
    for transaction in transactions:
        if "customer_id" == customer_id:
            if "type" == "deposit":
                customer_balance += "amount"
            else if "type" == "withdrawal":
                customer_balance -= "amount"
    print(f"Customer {customer_id} has a remaining balance of: {customer_balance}")

calculate_balance()
    
