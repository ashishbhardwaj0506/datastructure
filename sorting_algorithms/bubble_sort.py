"""
Bubble sort repeatedly swaps adjacent elements until the array is sorted.
It's not suggestible for large amount of data due to high complexity
Best complexity O(n)
Worst complexity 0(n~2)
Average complexity 0(n~2)
space complexity 0(1)
stability Yes
"""

class BubbeSort:

    def __init__(self, arr):
        self.arr = arr

    def sort_arr(self):
        # We calculate the array length before the nested loop, so there is no need to recalculate it within the loop.
        len_of_arr = len(self.arr)
        for i in range(len_of_arr):
            check_changes_in_list = False
            for j in range(len_of_arr - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    check_changes_in_list = True
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
            # for implementing best case scenario
            if not check_changes_in_list:
                break
        return self.arr

arr = [5, 1, 9, 100, 3, 0, 10]
bubble = BubbeSort(arr)
print(bubble.sort_arr())