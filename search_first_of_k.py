def search_first_of_k(a, k):
    left, right, result = 0, len(a), -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] > k:
            right = mid - 1
        elif a[mid] == k:
            result = a[mid]
            right = mid - 1
        else:
            left = mid + 1
    return result


def square_root(k):
    left, right, result = 0, k, -1
    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1
