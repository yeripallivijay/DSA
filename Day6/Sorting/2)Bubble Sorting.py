import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

class Solution:
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n-1,-1,-1):
            isSwapped = False
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    isSwapped = True
            if not isSwapped:
                break
        return nums
    

if __name__ == "__main__":
    
    solution = Solution()

    nums = [7, 4, 1, 5, 3]

    print("Array Before Using Bubble Sort:", nums)

    
    sorted_nums = solution.bubbleSort(nums)

    print("Array After Using Bubble Sort:", sorted_nums)