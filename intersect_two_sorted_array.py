# find intersection of two sorted arrays
def intersect_two_sorted_arrays(a, b):
  i, j, intersection_a_b = 0, 0, []
  while i < len(a) and j < len(b):
    if a[i] == b[j]:
      if i == 0 or a[i] != a[i - 1]:
        intersection_a_b.append(a[i])
      i, j = i + 1, j + 1
    elif a[i] > b[j]:
      j += 1
    else:
      i += 1
  return intersection_a_b

a = [2, 3, 3, 5, 7, 11]
b = [3, 3, 7, 15, 31]

print(*intersect_two_sorted_arrays(a, b))


