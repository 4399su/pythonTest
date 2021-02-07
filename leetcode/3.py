class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict = {}
        countdict = {}
        count = 0
        for index, item in enumerate(s):

            if item in dict:
                for i in list(dict):
                    if i == item:
                        dict.pop(i)
                        count=len(dict)+1
                        break
                    dict.pop(i)
                    countdict[index] = count
                dict[item] = index
            else:
                dict[item] = index
                count = count + 1
                countdict[index] = count

        if len(s) == 0:
            return 0
        return max(countdict.values())


if __name__ == '__main__':
    s = Solution()
    count = s.lengthOfLongestSubstring("ckilbkd")
    print(count)
