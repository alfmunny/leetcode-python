class Solution:
    def reverseString(self, s):
        a = ["a"] * len(s)
        l = len(s)
        for i in range(int((l+1)/2)):
            a[i] = s[l - 1 - i]
            a[l - 1 -i] = s[i]

        return "".join(a)

s = Solution()

print(s.reverseString("hello"))
print(s.reverseString("hell"))
print(s.reverseString("hel"))
print(s.reverseString("he"))
print(s.reverseString("h"))
print(s.reverseString(""))
