"""
Kruskal与Prim两种最小生成树算法
ancestors：存储祖先节点；初始化，v1=u1,v2=u2.... 如a-b-c-d {a:a, b:a, c:b, d:c}
w_edges：一条边及对应的权重，存放着形如(w,vertex1,vertex2)的字典，w:权值，vertex1:源点，vertex2:目标点
"""
from heapq import heappop, heappush

# 寻找代表节点(祖先节点), 这里使用路径压缩的方法(path compression)
def find(ancestors, vertex):
    if ancestors[vertex] != vertex:
        ancestors[vertex] = find(ancestors, ancestors[vertex])
    return ancestors[vertex]

def kruskal(graph):
    w_edges = sorted([(graph[v1][v2], v1, v2) for v1 in graph for v2 in graph[v1]])  # 按权值升序
    selected_edges = []
    ancestors = {vertex:vertex for vertex in graph}
    for _, vertex1, vertex2 in w_edges:
        ancestor_v1 = find(ancestors, vertex1)
        ancestor_v2 = find(ancestors, vertex2)
        if ancestor_v1 != ancestor_v2:   # 边的源点的祖先不等于边的目的祖先
            selected_edges.append((vertex1, vertex2))
            ancestors[ancestor_v1] = ancestor_v2  # 合并，使目标节点变成生成树的一部分(修改其祖先)
    return selected_edges, ancestors

def prim(graph, s):  # s:开始的顶点
    selected_vertex, heap = {}, [(0, s, None)]
    while heap:
        w, v1, v2 = heappop(heap)  # 出堆的都是最小权重
        if v1 in selected_vertex:
            continue   # 如果目标点在生成树中，跳过
        selected_vertex[v1] = v2   # 记录目标点不在生成树中
        for v3, w in graph[v1].items():
            heappush(heap, (w, v3, v1))  # 将u点的出边入堆
    selected_edges = [(v, selected_vertex[v]) for v in selected_vertex]  # 字典转换为列表
    return selected_edges


if __name__ == "__main__":
    # Markdown笔记中的连通图
    graph = {
         'A': {'B':12, 'F':16, 'G':14},
         'B': {'A':12, 'F':7, 'C':10},
         'C': {'B':10, 'F':6, 'D':3, 'E':5},
         'D': {'C':3, 'E':4},
         'E': {'D':4, 'C':5, 'F':2, 'G':8},
         'F': {'B':7, 'C':6, 'E':2, 'G':9, 'A':16},
         'G': {'A':14, 'F':9, 'E':8}}

    # Kruskal算法
    sum1 = 0
    selected_edges, final_ancestors = kruskal(graph)
    for vertex1, vertex2 in selected_edges:
        sum1 += graph[vertex1][vertex2]
    print("Kruskal最小生成树总权重是:", sum1)
    print("Kruskal最小生成树的边是:", selected_edges)

    # Prim算法
    selected_edges = prim(graph, 'A')  # 从顶点'A'开始
    sum2 = 0
    for v1, v2 in selected_edges:
        if v2 !=None:
            sum2 += graph[v1][v2]
    print("Prim最小生成树总权重:", sum2)
    print("Prim最小生成树顶点:", selected_edges)
