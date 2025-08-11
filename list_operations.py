# Step one: Create an empty list
my_list = []

# Step two: Append elements 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert 15 at the second position (index 1)
my_list.insert(1, 15)

# Step 4: Extend with [50, 60, 70]
my_list.extend([50, 60, 70])

# step 5: Remve the last element
my_list.pop()

# Step s6: Sort in ascending order
my_list.sort()

# Step 7: Find and print index of value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# last step: Final list for reference
print("Final list:", my_list)