class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        if str(x).endswith('0'):
            x = str(x)[:len(str(x)) - 1]
        x = int(x)
        if  x < 0:
            x = abs(x)
            x = str(x)
            x = x[::-1]
            x = int(x) * -1
        elif x > 0:
            x = str(x)
            x = x[::-1]
        x =int(x)
        if (2 ** 31) * -1 > x or x > 2 ** 31 - 1:
            return 0
        return int(x)


if __name__ == '__main__':
    s = Solution()
    temp = s.reverse(1534236469)
    print(temp)
