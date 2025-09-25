# 49. Group Anagrams
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

# 解释：

# 在 strs 中没有字符串可以通过重新排列来形成 "bat"。
# 字符串 "nat" 和 "tan" 是字母异位词，因为它们可以重新排列以形成彼此。
# 字符串 "ate" ，"eat" 和 "tea" 是字母异位词，因为它们可以重新排列以形成彼此。
class Solution:
    def groupAnagrams(self, strs):
        hash = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in hash:
                hash[key].append(s)
            else:
                hash[key] = [s]
        return list(hash.values()) # hash.values() is dict_values, need to convert to list
    
if __name__ == "__main__":
    strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs1))  # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]