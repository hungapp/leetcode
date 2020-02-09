# seaching ch11
import operator
import random


def find_kth_largest(k, a):
    def find_kth(comp):
        def partition_around_pivot(left, right, pivot_idx):
            pivot_value = a[pivot_idx]
            new_pivot_idx = left
            a[pivot_idx], a[right] = a[right], a[pivot_idx]
            for i in range(left, right):
                if comp(a[i], pivot_value):
                    a[i], a[new_pivot_idx] = a[new_pivot_idx], a[i]
                    new_pivot_idx += 1
            a[right], a[new_pivot_idx] = a[new_pivot_idx], a[right]
            return new_pivot_idx

        left, right = 0, len(a) - 1
        while left <= right:
            pivot_idx = random.randint(left, right)
            new_pivot_idx = partition_around_pivot(left, right, pivot_idx)
            # if there are exactly k-1 elements greater than the pivot then the pivot must be the kth largest element
            if new_pivot_idx == k - 1:
                return a[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:
                left = new_pivot_idx + 1
    return find_kth(operator.gt)


a = [3, 1, -1, 2]
print(find_kth_largest(1, a))
