products = [
    ("Laptop", 60000),
    ("Phone", 30000),
    ("Keyboard", 2000),
    ("Monitor", 15000),
    ("Mouse", 800)
]

sorted_products = sorted(products, key=lambda x: x[1])

filtered_products = list(filter(lambda p: p[1] > 10000, sorted_products))

print("Sorted products:")
print(sorted_products)
print("Filtered products (price > 10,000) after sorting:")
print(filtered_products)



