arr = [1, 1, 12, 0, 3, 5, 7, 7, -9]
nodupe_arr = list(set(arr))
new_arr = [i + 2 for i in nodupe_arr if i > 5]
print(arr)
print(new_arr)