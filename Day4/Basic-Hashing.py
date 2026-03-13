import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# #Q1)Highest Occurring Element in an Array
# class Solution:
#     def mostFrequentElement(self, nums):
#         n = len(nums)
#         maxFreq = 0
#         maxEle = 0
#         mpp = {}

#         for num in nums:
#             if num in mpp:
#                 mpp[num] += 1
#             else:
#                 mpp[num] = 1
#         for ele,freq in mpp.items():
#             if freq > maxFreq:
#                 maxFreq = freq
#                 maxEle = ele
#             elif freq == maxFreq:
#                 maxEle = min(maxEle,ele)
#         return maxEle        
# if __name__ == "__main__":
#     nums = [4, 4, 5, 5, 6]
#     sol = Solution()
#     ans = sol.mostFrequentElement(nums)
#     print("The highest occurring element in the array is:", ans)

# #Q2)Second Highest Occurring Element
# from collections import defaultdict
# class Solution:
#     def secondMostFrequentElement(self, nums):
#             n = len(nums)
#             maxFreq = 0
#             secMaxFreq = 0

#             maxEle = -1
#             secMaxEle = -1

#             mpp = defaultdict(int)

#             for num in nums:
#                 mpp[num] +=1
#             for ele,freq in mpp.items():
#                 if freq > maxFreq:
#                       secMaxFreq = maxFreq
#                       maxFreq = freq
#                       secMaxEle = maxEle
#                       maxEle = ele
#                 elif freq == maxFreq:
#                     maxEle = min(maxEle, ele)
#                 elif freq > secMaxFreq:
#                     secMaxFreq = freq
#                     secMaxEle = ele
#                 elif freq == secMaxFreq:
#                     secMaxEle = min(secMaxEle, ele)
#             return secMaxEle
                
# if __name__ == "__main__":
#     nums = [4, 4, 5, 5, 6]
#     sol = Solution()
#     ans = sol.secondMostFrequentElement(nums)
    
#     print(f"The second highest occurring element in the array is: {ans}")

#Q3)Sum of Highest and Lowest Frequency
from collections import defaultdict
class Solution:
    def sumHighestAndLowestFrequency(self, nums):
            n = len(nums)
            maxFreq = 0
            minFreq = n
            mpp={}
            for num in nums:
                if num in mpp:
                     mpp[num] += 1
                else:
                    mpp[num] = 1
            for freq in mpp.values():
                maxFreq = max(maxFreq,freq)
                minFreq = min(minFreq,freq)
            return maxFreq + minFreq
            
                
if __name__ == "__main__":
    nums = [1, 2, 2, 3, 3, 3]
    sol = Solution()
    ans = sol.sumHighestAndLowestFrequency(nums)
    
    print(f"The sum of highest and lowest frequency in the array is: {ans}")