'''*Today's Assignment*
Create a set and perform union, intersection and difference'''


# Creating two sets
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union of set_a and set_b (all elements from both sets)
union_result = set_a.union(set_b)
print("Union:", union_result)

# Intersection of set_a and set_b (elements common to both sets)
intersection_result = set_a.intersection(set_b)
print("Intersection:", intersection_result)

# Difference of set_a and set_b (elements in set_a but not in set_b)
difference_result = set_a.difference(set_b)
print("Difference:", difference_result)
