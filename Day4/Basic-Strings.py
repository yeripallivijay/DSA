import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

# # Q1) Reverse a String II
# class Solution:
#     def reverseString(self, s):
#         start = 0
#         end = len(s)-1

#         while start < end:
#             s[start],s[end] = s[end],s[start]
#             start += 1
#             end -= 1
#         return


# if __name__ == "__main__":
#     str_list = ['h', 'e', 'l', 'l', 'o']
#     sol = Solution()
#     sol.reverseString(str_list)

#     print("".join(str_list))

# # Q2) Palindrome Check
# class Solution:
#     def palindromeCheck(self, s):
#         #your code goes here
#         start = 0
#         end = len(s)-1
#         while start < end:
#             if s[start] != s[end]:
#                 return False
#             start += 1
#             end -=1
#         return True
        


# if __name__ == "__main__":
#     solution = Solution()
#     str = "racecar"  

#     if solution.palindromeCheck(str):
#         print(f"{str} is a palindrome.")
#     else:
#         print(f"{str} is not a palindrome.")

# # Q3) Largest Odd Number in a String
# class Solution:
#     def largeOddNum(self, s: str) -> str:
#         start = 0
#         end = len(s) - 1
    
#         while end >= start and int(s[end]) % 2 == 0:
#             end -= 1
    
#         while start <= end and s[start] == '0':
#             start += 1
    
#         return s[start:end + 1]
        


# if __name__ == "__main__":
#     solution = Solution()
# num = "5347"
# result = solution.largeOddNum(num)
# print("Largest odd number:", result)

# # Q4) Longest Common Prefix
# class Solution:
#     def longestCommonPrefix(self, strs):
#         if not strs:
#             return""
#         strs.sort()
#         first = strs[0]
#         last = strs[-1]
#         ans = []

#         for  i in range(min(len(first),len(last))):
#             if first[i] != last[i]:
#                 return ''.join(ans)
#             ans.append(first[i])
#         return ''.join(ans)
        


# if __name__ == "__main__":
#     solution = Solution()
#     input_strs = ["flower", "flow", "flight"]
#     result = solution.longestCommonPrefix(input_strs)
#     print("Longest Common Prefix:", result) 

# Q5) Isomorphic String
class Solution:
    def isomorphicString(self, s, t):
        m1,m2 = [0]*256,[0]*256

        n = len(s)

        for i in range(n):
            if m1[ord(s[i])] != m2[ord(t[i])]:
                return False
            
            m1[ord(s[i])] = i + 1
            m2[ord(t[i])] = i + 1
        return True
        


if __name__ == "__main__":
    solution = Solution()
    s = "egg"
    t = "add"
    if solution.isomorphicString(s, t):
        print("Strings are isomorphic.")
    else:
        print("Strings are not isomorphic.")