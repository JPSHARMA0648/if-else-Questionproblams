'''Q11 Write a program that calculates the discount for a product based on its price:
If price is greater than 1000, discount is 10%
If price is between 500 and 1000, discount is 5%
Otherwise, no discount
Print the final price after applying the discount.'''
#ans

def calculate_discount(price):
    if price > 1000:
        discount = 0.10  # 10% discount
    elif 500 <= price <= 1000:
        discount = 0.05  # 5% discount
    else:
        discount = 0.00  # No discount
    return discount

def apply_discount(price, discount):
    final_price = price - (price * discount)
    return final_price

# Get user input for product price
price = float(input("Enter the price of the product: "))

# Calculate discount based on the price
discount = calculate_discount(price)

# Apply discount and calculate final price
final_price = apply_discount(price, discount)

# Output the result
print(f"The final price after applying the discount is: {final_price:.2f}")
