neighbours = ["Max", "Rostyslav", "Lena", "Evgeniy", "Kristina", "Andrey"]
print("This is original list:")
print(neighbours)

# ------------------------------

# Sorted не только временно сортирует список
print("\nHere is sorted list:")
print(sorted(neighbours))

# ------------------------------

# reverse не сортирует в обратном алфавитном порядке как это делает sorted или sort
# он просто разварачивает список на постоянно
print("\nHere is sorted reversed list:")
neighbours.reverse()
print(neighbours)

print("\nHere is original list again:")
print(neighbours)

print(f"\nHere is lenght of my neighbors: {len(neighbours)}")


