your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total expenses:", your_total)
print("Partner total expenses:", partner_total)
if your_total > partner_total:
    print("You spent more money")
elif partner_total > your_total:
    print("Your partner spent more money")
else:
    print("Both spent the same amount")

max_difference = 0
max_category = ""

for category in your_expenses:
    difference = abs(your_expenses[category] - partner_expenses[category])

    if difference > max_difference:
        max_difference = difference
        max_category = category

print("Category with highest difference:", max_category)
print("Difference:", max_difference)