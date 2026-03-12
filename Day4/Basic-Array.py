import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# # Q1) Sum of Array Elements
# class Solution:
#     def sum(self,arr, n):
#         sum = 0
#         for i in range(n):
#             sum = sum + arr[i]
#         return sum
    
# if __name__ == "__main__":
#     n = 4
#     arr = [1, 2, 3, 8]
#     sol = Solution()
#     result = sol.sum(arr, n)

# print("The sum of array elements is:", result)

# # Q2) Count of odd numbers in array
# class Solution:
#     def countOdd(self,arr, n):
#         count = 0
#         for i in range(n):
#             if (arr[i]%2==1):
#                 count = count + 1
#         return count
    
# if __name__ == "__main__":
#     arr = [1, 2, 3, 8]
#     sol = Solution()
#     n = len(arr)

#     count = sol.countOdd(arr, n)
#     print("Count of odd numbers:", count)

# # Q3) Check if the Array is Sorted I
# class Solution:
#     def arraySortedOrNot(self, arr, n):
#         for i in range(1,n):
#             if (arr[i]<arr[i-1]):
#                 return False
#         return True
    
# if __name__ == "__main__":
#     solution = Solution()
#     arr = [1, 2, 3, 4, 5]
#     n = len(arr)

#     sorted = solution.arraySortedOrNot(arr, n)
#     if sorted:
#         print("Array is sorted.")
#     else:
#         print("Array is not sorted.")

# Q4) Reverse an array
class Solution:
    def reverse(self, arr: list, n: int) -> None:
        left = 0
        right = n - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

def printArray(arr, n):
    for i in range(n):
        print(arr[i], end=" ")
    print()
    
if __name__ == "__main__":
    n = 5
    arr = [5, 4, 3, 2, 1]
    solution = Solution()

    print("Original array: ", end="")
    printArray(arr, n)
    solution.reverse(arr, n)
    print("Reversed array: ", end="")
    printArray(arr, n)