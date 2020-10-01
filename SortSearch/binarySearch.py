def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == mid:
            return True
        elif target > mid:
            left = mid + 1
        elif target < mid:
            right = mid - 1
    return False


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    target = 2
    print(binarySearch(arr, target))
