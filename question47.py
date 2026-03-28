# Dictionary
data = {
    "A": 40,
    "B": 10,
    "C": 30,
    "D": 20
}

# Sort dictionary by value (ascending)
sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))

print("Sorted Dictionary (Ascending):")
for key, value in sorted_data.items():
    print(key, ":", value)


# Sort dictionary by value (descending)
sorted_desc = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))

print("\nSorted Dictionary (Descending):")
for key, value in sorted_desc.items():
    print(key, ":", value)