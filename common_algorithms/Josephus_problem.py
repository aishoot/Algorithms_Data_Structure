# Josephus Problem
"""
n个人(1,2,3,...,n)围成一个环，从1号人开始数, 数到m的人就退出游戏，直到最后一个人
求最后一个剩下的人是几号？

递推公式：
f(n, m) = (f(n−1, m) + m) % n
f(n, m)表示，n个人报数，每报到m时杀掉那个人，最终胜利者的编号
f(n−1, m)表示，n-1个人报数，每报到m时杀掉那个人，最终胜利者的编号
"""

def josephus(n, m):
    lis = list(range(1, n+1))
    i = 0
    while len(lis) > 1:
        i = (m-1 + i) % len(lis)  # 递推公式
        print('Kill:', lis[i])
        lis.pop(i)
    print('Survive:', lis[0])

if __name__ == '__main__':
    josephus(7, 3)
