"""
Binary search use for searching element in sorted array
"""

class BinarySearch:

    def __init__(self, arr):
        self.arr = arr

    def search(self, ele):
        low = 0
        high = len(self.arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.arr[mid] == ele:
                return "Element found"
            elif self.arr[mid] < ele:
                low = mid + 1
            else:
                high = mid - 1

        return "Element doesn't found"

arr = [1, 4, 5, 8, 15, 19, 20]
binary = BinarySearch(arr)
print(binary.search(1))
print(binary.search(4))
print(binary.search(5))
print(binary.search(8))
print(binary.search(15))
print(binary.search(19))
print(binary.search(20))
print(binary.search(22))
