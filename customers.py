#Exercise 1
customer = {
    "name": "Antoni Gomez",
    "email": "antoni@example.com",
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