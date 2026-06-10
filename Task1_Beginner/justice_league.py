justice_league = [
    "Superman",
    "Batman",
    "Wonder Woman",
    "Flash",
    "Aquaman",
    "Green Lantern"
]

print("Justice League Members:")
print(justice_league)

print("Number of members:", len(justice_league))
justice_league.append("Batgirl")
justice_league.append("Nightwing")

print("After adding new members:")
print(justice_league)
justice_league.remove("Wonder Woman")

justice_league.insert(0, "Wonder Woman")

print("After making Wonder Woman leader:")
print(justice_league)
justice_league.remove("Green Lantern")

flash_index = justice_league.index("Flash")

justice_league.insert(flash_index + 1, "Green Lantern")

print("After separating Flash and Aquaman:")
print(justice_league)
justice_league = [
    "Cyborg",
    "Shazam",
    "Hawkgirl",
    "Martian Manhunter",
    "Green Arrow"
]

print("New Justice League:")
print(justice_league)
justice_league.sort()

print("Sorted Justice League:")
print(justice_league)

print("New Leader:", justice_league[0])