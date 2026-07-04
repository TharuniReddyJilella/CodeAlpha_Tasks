stock_prices = {
    "AAPL": 180, "TSLA": 250, "GOOG": 140, "MSFT": 320, "AMZN": 150
}

total_investment = 0

print("=" * 30)
print("     STOCK PORTFOLIO TRACKER")
print("=" * 30)

print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} -> ${price}")


while True:
    stock_name = input("\nEnter Stock Name(to stop enter done): ").strip().upper()

    if stock_name == 'DONE':
        break

    if stock_name in stock_prices:
        quantity = int(input(f"Enter Quantity for {stock_name}: "))
        investment_value = stock_prices[stock_name] * quantity
        total_investment += investment_value


        print(f"Investment Value of {stock_name} = ${investment_value}")
    else:
        print("Stock not found in database!")

print("\n" + "=" * 30)
print("PORTFOLIO SUMMARY")
print("=" * 30)

print(f"Total Investment Value = ${total_investment}")