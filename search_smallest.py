def search_smallest(a):
    left, right = 0, len(a) - 1
    while left < right:
        mid = (left + right) // 2
        if a[mid] > a[right]:
            left = mid + 1
        else:  # a[mid] < a[right]
            right = mid
    return a[left]


a = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]
print(search_smallest(a))
