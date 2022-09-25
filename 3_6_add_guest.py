guest = ["Bob", "Tom", "Jerry"]
print(f"Would you like to come round for a meal today, {guest}")

print(f"{guest[0]} cannot keep the appointment.")
guest[0] = "James"

print(f"Would you like to come round for a meal today, {guest}")

print("I found a lager dinning-table.")
guest.insert(0, "Curry")
guest.insert(2, "Harry")
guest.append("Joe")
print(f"Would you like to come round for a meal today, {guest}")

