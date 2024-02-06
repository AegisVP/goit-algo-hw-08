import heapq


def find_min_sums(heap):
    min_sum = 0
    while len(heap) > 1:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        min_sum += x + y
        heapq.heappush(heap, x + y)
        heapq.heapify(heap)

    return min_sum


if __name__ == '__main__':

    nums = [1, 9, 3, 8, 6, 7, 5, 2]
    heapq.heapify(nums)

    print('Купа:')
    print(nums)
    print()
    print('Мінімальна сума:')
    print(find_min_sums(nums))
