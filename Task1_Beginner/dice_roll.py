import random

count_1 = 0
count_6 = 0
two_6s_row = 0

previous_roll = 0

for i in range(20):
    number = random.randint(1, 6)

    print(number)

    if number == 1:
        count_1 += 1

    if number == 6:
        count_6 += 1

    if previous_roll == 6 and number == 6:
        two_6s_row += 1

    previous_roll = number

print("Number of 1s:", count_1)
print("Number of 6s:", count_6)
print("Two 6s in a row:", two_6s_row)