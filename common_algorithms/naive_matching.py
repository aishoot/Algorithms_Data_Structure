# 字符串匹配
def naive_matching(t, p):
    m, n = len(t), len(p)
    i, j = 0, 0
    while i < m and j < n:
        if t[i] == p[j]:
            i, j = i+1, j+1
        else:
            i, j = i-j+1, 0
    if j == n:
        return i - j
    return -1

t = "acgccatgsdad"
p = "ccatg"
is_in = p in t
print("Python自带函数:", is_in)
print(naive_matching(t, p))