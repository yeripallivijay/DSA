import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

import random
class Solution:
    def partition(self, arr, low, high):
        randomIndex = low + random.randint(0, high - low)
        arr[low], arr[randomIndex] = arr[randomIndex], arr[low]
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while arr[i] <= pivot and i <= high - 1:
                i += 1
            while arr[j] > pivot and j >= low + 1:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        arr[low], arr[j] = arr[j], arr[low]
        return j

    def quickSortFinal(self, arr, low, high):
        if low < high:
            pIndex = self.partition(arr, low, high)
            self.quickSortFinal(arr, low, pIndex - 1)
            self.quickSortFinal(arr, pIndex + 1, high)

    def quickSort(self, nums):
        n = len(nums)
        self.quickSortFinal(nums, 0, n - 1)
        return nums

if __name__ == "__main__":
    arr = [4, 6, 2, 5, 7, 9, 1, 3]
    n = len(arr)

    print("Before Sorting Array: ")
    for i in range(n):
        print(arr[i], end=" ")
    print()

   
    solution = Solution()

    
    sortedArr = solution.quickSort(arr)

    print("After Sorting Array: ")
    for i in range(n):
        print(sortedArr[i], end=" ")
    print()