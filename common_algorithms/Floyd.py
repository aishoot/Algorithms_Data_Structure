# Floyd算法求最短路径
import copy

def back_path(path, i, j, shortestPath):  # 递归回溯
    #print("path[%s][%s] = " % (i, j), path[i][j])
    if -1 != path[i][j]:
        shortestPath = back_path(path, i, path[i][j], shortestPath)
        shortestPath = back_path(path, path[i][j], j, shortestPath)
    if j not in shortestPath:
        shortestPath.append(j)
    return shortestPath


def getShortestPath(graph, path, i, j):
    shortestPath = []
    if graph[i][j] == float('inf') or i == j:
        #print("顶点%s 不能到达 顶点%s！" % (i, j))
        return shortestPath
    elif path[i][j] == -1:
        shortestPath.append(i)
        shortestPath.append(j)
    else:
        shortestPath.append(i)
        shortestPath = back_path(path, i, j, shortestPath)
    #print("顶点%s 到 顶点%s 的路径为：" % (i, j), shortestPath)
    return shortestPath


def getAllShortestPath(graph, path):
    #print("------正在生成全局最短路径------")
    ShortestPath_dict = {}
    for i in range(N):
        ShortestPath_dict[i] = {}
        for j in range(N):
            #print("尝试生成顶点%s到顶点%s的最短路径..." % (i, j))
            if i != j:
                shortestPath = getShortestPath(graph, path, i, j)
                ShortestPath_dict[i][j] = shortestPath
            #print("--------------------------------")
    return ShortestPath_dict


# 图定义
M = float('inf')  # 无穷大
graph = [[0, 30, 15, M, M, M],
         [5, 0, M, M, 20, 30],
         [M, 10, 0, M, M, 15],
         [M, M, M, 0, M, M],
         [M, M, M, 10, 0, M],
         [M, M, M, 30, 10, 0]]
N = len(graph)
path = [[-1]*N for _ in range(N)]

# Floyd算法
for k in range(N):  # 写到最下面一行是错误的
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = k

print("最短路径最后的图:\n", graph)
print("所有路径:\n", path)
print("两两所有点最短路径\n", getAllShortestPath(graph, path))
