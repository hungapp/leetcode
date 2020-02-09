import itertools
import heapq


def sort_approximately_sorted_array(sequence, k):
    result = []
    min_heap = []
    # add the first k elements into min_heap. stop if there are fewer than k elements
    for x in itertools.islice(sequence, k):
        heapq.heappush(min_heap, x)
        print(x)
    # for every new element, add it to min_heap an extract the smallest
    for x in sequence[k:]:
        smallest = heapq.heappushpop(min_heap, x)
        result.append(smallest)
    # sequence is exhauted, iteratively extract the remaining elements
    while min_heap:
        smallest = heapq.heappop(min_heap)
        result.append(smallest)
    return result


print(sort_approximately_sorted_array([3, -1, 2, 6, 4, 5, 8], 2))
print(*itertools.islice([1, 2, 3, 4], 3))
print(*itertools.islice([1, 2, 3, 4], 1, 2))
