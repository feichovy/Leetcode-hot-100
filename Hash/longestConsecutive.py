# 128. Longest Consecutive Sequence
class Solution:
    def longestConsecutive(self, nums):
        hashset = set(nums)
        ans = 0
        for x in hashset:
            # 只有当 x 是序列起点时才往下找
            if x - 1 not in hashset:
                y = x
                while y + 1 in hashset:
                    y += 1
                ans = max(ans, y - x + 1)
        return ans


# example
if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(Solution().longestConsecutive(nums))  # 4
