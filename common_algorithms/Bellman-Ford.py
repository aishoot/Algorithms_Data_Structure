"""
Bellman-Ford算法
定理：
在一个含有n个顶点的图中，任意两点之间的最短路径最多包含n-1条边
最短路径肯定是一个不包含回路的简单路径(回路包括正权回路与负权回路), 理由:
1. 如果最短路径中包含正权回路，则去掉这个回路，一定可以得到更短的路径
2. 如果最短路径中包含负权回路，则每多走一次这个回路，路径更短，则不存在最短路径
因此最短路径肯定是一个不包含回路的简单路径，即最多包含n-1条边，所以进行n-1次松弛即可
"""
def getEdges(G):
    """ 输入图G，返回其边与端点的列表 """
    v1, v2, w = [], [], []  # v1:出发点; v2:对应的相邻到达点; w:顶点v1到顶点v2的边的权值。三个表的值分别对应
    for i in G:
        for j in G[i]:
            if G[i][j] != 0:
                w.append(G[i][j])
                v1.append(i)
                v2.append(j)
    return v1, v2, w

def Bellman_Ford(G, v0, INF=float('inf')):  # INF 为设定的无限远距离值
    v1, v2, w = getEdges(G)
    v0_dis = dict((k, INF) for k in G.keys())  # 初始化源点与所有点之间的最短距离
    v0_dis[v0] = 0

    # 核心算法
    for k in range(len(G) - 1):  # 循环 n-1轮
        check = 0  # 用于标记本轮松弛中dis是否发生更新
        for i in range(len(w)):  # 对每条边进行一次松弛操作
            if v0_dis[v1[i]] + w[i] < v0_dis[v2[i]]:
                v0_dis[v2[i]] = v0_dis[v1[i]] + w[i]
                check = 1
        if check == 0:
            break

    # 检测负权回路; 如果在 n-1 次松弛之后，最短路径依然发生变化，则该图必然存在负权回路
    flag = 0
    for i in range(len(w)):  # 对每条边再尝试进行一次松弛操作
        if v0_dis[v1[i]] + w[i] < v0_dis[v2[i]]:
            flag = 1
            break
    if flag == 1:
        return False
    return v0_dis

if __name__ == "__main__":
    G = {'A': {'B': 6, 'C': 3},
         'B': {'A': 6, 'C': 2, 'D': 5},
         'C': {'A': 3, 'B': 2, 'D': 3, 'E': 4},
         'D': {'B': 5, 'C': 3, 'E': 2, 'F': 3},
         'E': {'C': 4, 'D': 2, 'F': 5},
         'F': {'D': 3, 'E': 5}}
    v0 = 'A'  # 源结点，从该结点搜索到其他所有结点的最短路径
    v0_dis = Bellman_Ford(G, v0)
    print(v0_dis)