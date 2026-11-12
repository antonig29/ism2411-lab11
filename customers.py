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