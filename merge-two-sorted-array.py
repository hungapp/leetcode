# merge without using an extra array, on array a
def merge_two_sorted_array(a, m, b, n):
  for i in range(n):
    a.append([])
  i, j, write_idx = m - 1, n - 1, m + n - 1
  while i >= 0 and j >= 0:
    if a[i] > b[j]:
      a[write_idx] = a[i]
      i -= 1
    else:
      a[write_idx] = b[j]
      j -= 1
    write_idx -= 1
  while j >= 0:
    a[write_idx] = b[j]
    write_idx, j = write_idx - 1, j - 1
  return a
  
a = [5, 13, 17]
b = [3, 7, 11, 19]
m = len(a)
n = len(b)

print(*merge_two_sorted_array(a, m, b, n))