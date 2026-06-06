'''List=[] ordered,changeable,allow duplicate
    Set={} unordered,unchangeable,no duplicate but add or remove items
    Tuple=() ordered,unchangeable,allow duplicate '''
    
#Shopping cart program
products =[]
prices =[]
total=0

while True:
    product=input("Enter the purchased product name(q to quit): ")
    if product.lower()=='q':
        break
    else:
        price=float(input(f"Enter the price of {product}: $"))
        products.append(product)
        prices.append(price)

print("\n----- YOUR CART -----")
for product in products:
    print(product, end=" ")
print()
for price in prices:
    total += price
print(f"Your total is: ${total:.2f}")