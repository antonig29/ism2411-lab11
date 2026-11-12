#1 I use .get() when a key might be missing so the program doesn't crash and gives a default.
# i use brackets when the key has to be there so i get an error if something goes wrong

#2 It reminds me of a table in excel which adds amount for each square
# Python is better for more data because it handled more data better.

#Exercise 1
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1500.00
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

#Exercise 2
customer["phone"] = "123-456-7890"
print(customer["phone"])

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer) 

#Exercise 3
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: 'email' is not in the dictionary")

#Exercise 4
for key, value in customer.items():
    print(f"{key}: {value}")

for item in customer:
    print(item)

#without using .items() the loop only gives the keys but not the values 

#Exercise 5

tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)
final_price = 200 * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount * 100}%")
print(f"Final price: ${final_price:.2f}")


#Exercise 6

customer = [
    {"name": "Antoni", "tier": "gold"},
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "bronze"},
]

for c in customer:
    rate = tier_discounts.get(c["tier"], 0)
    discount_amount = 300 * rate
    print(f"{c['name']} | {c['tier']} | discount: ${discount_amount:.2f}")


#Exercise 7
catalog = {"Widget A": {"price": 9.99, "stock": 150}, "Gadget C": {"price": 49.99, "stock": 8}}

for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} (only {info['stock']} left)")


#Exercise 8
transactions = [
    {"region": "South", "amount": 300},                                            
    {"region": "North", "amount": 150}, 
    {"region": "South", "amount": 200}
    ]

summary = {}
for t in transactions:
    summary[t["region"]] = summary.get(t["region"], 0) + t["amount"]

for region in summary:
    print(f"{region}: ${summary[region]:.2f}")
