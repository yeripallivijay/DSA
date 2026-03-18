import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')


class Solution:
    def selectionSort(self,nums):
        n = len(nums)-1
        for i in range(n):
            min_index = i
            for j in range(i+1,len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            if min_index != i:
                nums[i],nums[min_index] = nums[min_index],nums[i]
        return nums


if __name__ == "__main__":
    solution = Solution()
    nums = [64, 25, 12, 22, 11]
    sorted_nums = solution.selectionSort(nums)
    print("Sorted array:", sorted_nums)