"""
Knuth-Morris-Pratt算法实现字符串查找
参考链接：https://blog.csdn.net/chiang97912/article/details/83005577
"""

def getNextList(s):  # 部分匹配表
    n = len(s)
    nextList = [0, 0]
    j = 0
    for i in range(1, n):
        while j > 0 and s[i] != s[j]:
            j = nextList[j]
        if s[i] == s[j]:
            j += 1
        nextList.append(j)
    return nextList

def KMP(s, p):
    n = len(s)
    m = len(p)
    nextList = getNextList(p)
    print(nextList)
    indies = []
    j = 0
    for i in range(n):
        while s[i] != p[j] and j > 0:
            j = nextList[j]

        if s[i] == p[j]:
            j += 1
            if j == m:
                indies.append(i-m+1)
                j = nextList[j]
    return indies

source_str = "BBC ABCDAB ABCDABCDABDE  adhABCDABD"
pattern_str = "ABCDABD"
indexs = KMP(source_str, pattern_str)
print(indexs)