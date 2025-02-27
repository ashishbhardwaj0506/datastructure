"""
Linear search is simple searching technique in array one by one
worst time complexity O(n)
best time complexity O(1)
space complexity O(1)
"""

class LinearSearch:

    def __init__(self, arr):
        self.arr = arr

    def search(self, ele):
        for indx in range(len(self.arr)):
            if self.arr[indx] == ele:
                return "Element found"

        return "Element doesn't found"

arr = [5, 1, 9, 100, 3, 0, 10]
linear = LinearSearch(arr)
print(linear.search(110))
