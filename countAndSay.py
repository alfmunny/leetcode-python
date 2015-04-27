class Solution:
    # @return a string
    def countAndSay(self, n):
        res = "1"
        for i in range(n-1):
            integer = res[0]
            counter = 0
            update = ""
            for j in range(len(res)):
                if res[j] == integer:
                    counter += 1
                else:
                    update = update + str(counter) + integer
                    integer = res[j]
                    counter = 1
            update = update + str(counter) + integer
            res = update
        return res

if __name__ == '__main__':
    s = Solution()
    print s.countAndSay(1)
    print s.countAndSay(2)
    print s.countAndSay(3)
    print s.countAndSay(4)
    print s.countAndSay(5)
    print s.countAndSay(6)
    print s.countAndSay(7)
