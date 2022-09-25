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

print("Sorry, I can only keep two guest.")

print(f"Sorry,{guest.pop()}")
print(f"Sorry,{guest.pop()}")
print(f"Sorry,{guest.pop()}")
print(f"Sorry,{guest.pop()}")
print(f"{guest[0]} still in the list")
print(f"{guest[1]} still in the list")

del guest[0]
del guest[0]
print(guest)


