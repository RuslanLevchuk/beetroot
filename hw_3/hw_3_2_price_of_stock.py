"""Input data:
Create a function which takes as input two dicts with structure mentioned above,
then computes and returns the total price of stock."""
#this function gets both dicts. and counts each price and saves result in another dict
#than it returns 2 values: dict with caclculated prices and it's amount
def price_calculator(stock, price):
    total_price = {}
    for item, item_price in price.items():
        total_price[item] = item_price*stock[item]
    return sum(total_price.values()), total_price
#input data
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
#get 2 values from func
total_pr, detalised_pr = price_calculator(stock, prices)
#output information
print("Stock price:")
for item, value in detalised_pr.items():
    print(f"{item.capitalize()}: {round(value, 2)} UAH")
print(f"Total price: {total_pr} UAH")