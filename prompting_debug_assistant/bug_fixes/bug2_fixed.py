def process_user_data(name, age, items):
    print(f"User processing: {name}")
    print(f"Next year you will be: {age + 1}")
    
    total_price = 0
    if not items:
        return 0
    
    for item in items:
        price = item.get("price")
        if price is not None:
            total_price += price
            
    average_item_price = total_price / len(items)
    print("Expensive choice!" if average_item_price > 50 else "Affordable price.")
    return average_item_price

if __name__ == "__main__":
    my_items = [{"price": 20}, {"price": 30}, {"price": None}]
    process_user_data("Murad", 20, my_items)
