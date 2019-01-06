""" 使用 Dijkstra 算法计算指定点 v0 到图 G 中任意点的最短路径的距离
 一种贪婪算法, 但不能解决负权值边的图
"""
from heapq import heappop, heappush

def Dijkstra(G, v0, INF=float('inf')):  # INF 为设定的无限远距离值
    selected_vertex = set()   # 就是MWeb笔记中的集合S, 已经选择的顶点
    current_v = v0  #  当前选择的出发找下一个的顶点
    v0_dis = dict((k, INF) for k in G.keys())  # 源顶点v0到其余各顶点的初始路程
    v0_dis[v0] = 0  # 自身到自身
    while len(selected_vertex) < len(G):
        selected_vertex.add(current_v)
        for w in G[current_v]:  # 以当前点的中心向外扩散
            if v0_dis[current_v] + G[current_v][w] < v0_dis[w]:  # 如果从当前点扩展到某一点的距离小与已知最短距离
                v0_dis[w] = v0_dis[current_v] + G[current_v][w]
        # 从当前寻找最小权值的出发的顶点
        new_min = INF  # 从剩下的未确定点中选择最小距离点作为新的扩散点
        for v in v0_dis.keys():
            if v in selected_vertex:
                continue
            if v0_dis[v] < new_min:
                new_min = v0_dis[v]
                current_v = v
    return v0_dis

# 实现方法2-利用堆
def Dijkstra2(G, s):
    v0_dis, P, Q, selected_vertex = {s: 0}, {s: None}, [(0, s, None)], set()
    while Q:
        du, u, p = heappop(Q)
        if u in selected_vertex:
            continue
        selected_vertex.add(u)
        v0_dis[u], P[u] = du, p
        for v in G[u]:
            if v not in selected_vertex:
                heappush(Q, (du + G[u][v], v, u))
    return v0_dis


# MWeb笔记中的图; G如果某个结点没有出度, 可记录为6:{6:0}, 保证len(G)正确
G = {'A': {'B':6, 'C':3},
     'B': {'A':6, 'C':2, 'D':5},
     'C': {'A':3, 'B':2, 'D':3, 'E':4},
     'D': {'B':5, 'C':3, 'E':2, 'F':3},
     'E': {'C':4, 'D':2, 'F':5},
     'F': {'D':3, 'E':5}}
v0_dis = Dijkstra(G, 'A')
print("点A到其余各点最短距离分别是:", v0_dis)
