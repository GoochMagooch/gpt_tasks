orders = [
    {"customer": "Alice", "items": ["Burger", "Fries"], "total": 15.50},
    {"customer": "Bob", "items": ["Pizza", "Soda"], "total": 18.00},
    {"customer": "Charlie", "items": ["Salad", "Soup"], "total": 12.00},
    {"customer": "Diana", "items": ["Steak", "Wine"], "total": 45.00},
    {"customer": "Eve", "items": ["Pasta", "Garlic Bread"], "total": 22.50},
    {"customer": "Frank", "items": ["Tacos", "Beer"], "total": 17.75},
    {"customer": "Grace", "items": ["Chicken Sandwich", "Iced Tea"], "total": 14.25},
    {"customer": "Hank", "items": ["Fish and Chips"], "total": 20.00},
    {"customer": "Ivy", "items": ["Veggie Burger", "Smoothie"], "total": 19.50},
    {"customer": "Jack", "items": ["Sushi", "Miso Soup"], "total": 30.00}
    ]

def summarize_orders(order_lst):
    total_orders = 0
    for order in order_lst:
        total_orders += 1
    
    revenue = 0
    for order in order_lst:
        revenue += order["total"]

    order_value = 0
    for order in order_lst:
        order_value += order["total"]
    average_value = order_value / total_orders
   
    print(f"Total orders: {total_orders}")
    print(f"Total revenue: {revenue}")
    print(f"Average order value: {average_value}")

# Call function on 'orders'
summarize_orders(orders)
