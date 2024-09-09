from functools import reduce

list1 = [5, 10, 15, 20, 25]

# Filter numbers greater than or equal to 10
filtered = filter(lambda x: x >= 10, list1)
filtered_list = list(filtered)  # Convert filter object to list

print(filtered_list)  # Print filtered results

# Map to double each number
mapped = map(lambda x: x * 2, filtered_list)
mapped_list = list(mapped)  # Convert map object to list

print(mapped_list)  # Print mapped results

# Reduce to sum the numbers, with an initial value of 0
reduced = reduce(lambda x, y: x + y, mapped_list, 0)

print(reduced)  # Print the reduced result
