"""
Selection sort search for smallest element index and replace it with starting element until array is sorted.
Best complexity O(n~2)
Worst complexity 0(n~2)
Average complexity 0(n~2)
space complexity 0(1)
stability No
"""

class SelectionSort:

    def __init__(self, arr):
        self.arr = arr

    def sort_arr(self):
        # We calculate the array length before the nested loop, so there is no need to recalculate it within the loop.
        len_of_arr = len(self.arr)
        for i in range(len_of_arr):
            index = i
            for j in range(i, len_of_arr):
                if self.arr[index] > self.arr[j]:
                    index = j
            self.arr[index], self.arr[i] = self.arr[i], self.arr[index]
        return self.arr

arr = [5, 1, 9, 100, 3, 0, 10]
selection = SelectionSort(arr)
print(selection.sort_arr())