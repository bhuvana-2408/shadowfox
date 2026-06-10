completed = 0

for i in range(10):
    completed += 10

    print("You completed", completed, "jumping jacks")

    tired = input("Are you tired? (yes/no): ")

    if tired == "yes" or tired == "y":
        skip = input("Do you want to skip the remaining sets? (yes/no): ")

        if skip == "yes" or skip == "y":
            print("You completed a total of", completed, "jumping jacks")
            break

    remaining = 100 - completed

    if remaining > 0:
        print(remaining, "jumping jacks remaining")

else:
    print("Congratulations! You completed the workout")