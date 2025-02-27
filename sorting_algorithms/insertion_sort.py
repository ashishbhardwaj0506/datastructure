"""
Insertion sort work by iteratively insertion elements of unsorted list for it's correct position.
It works similarly to how we manage our cards while playing.
Best complexity O(n)
Worst complexity 0(n~2)
Average complexity 0(n~2)
space complexity 0(1)
stability Yes
"""

class InsertionSort:

    def __init__(self, arr):
        self.arr = arr

    def sort_arr(self):
        for step in range(1, len(self.arr)):
            ele = self.arr[step]
            index = step - 1
            while index >= 0 and ele < self.arr[index]:
                self.arr[index + 1] = self.arr[index]
                index = index - 1
            self.arr[index + 1] = ele

        return self.arr

arr = [5, 1, 9, 100, 3, 0, 10]
insertion = InsertionSort(arr)
print(insertion.sort_arr())