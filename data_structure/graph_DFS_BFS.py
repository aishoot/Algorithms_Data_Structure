#coding=utf-8
class Gragh():
    # 将其他的图存储格式转化为格式如 {'A': ['C','D','F'], 'B': ['C']}
    def __init__(self, nodes, edges):
        self.sequense = {}
        edge_temp = []  # 临时变量，保存与指定点相连接的点, 无严格顺序
        for node in nodes:
            for u,v in edges:
                if node == u:
                    edge_temp.append(v)
                elif node == v:
                    edge_temp.append(u)
            # 当一个结点连接多个结点时按照名称顺序访问，故升序排列
            self.sequense[node] = sorted(edge_temp)
            edge_temp = []

    """
    Depth-First-Search, 深度优先算法
    node0: 开始搜索的结点
    """
    def DFS(self, node0):
        stack, order = [], []  # order里面存放具体的访问路径
        stack.append(node0)
        while stack:
            v = stack.pop()
            order.append(v)
            for w in self.sequense[v][::-1]:  # 逆序append顺序访问
                if w not in order and w not in stack:
                    stack.append(w)
        return order

    '''
     Beadth-First-Search, 广度优先搜索
    '''
    def BFS(self, node0):
        queue, order = [], []  # order存放的是具体的访问路径
        queue.append(node0)
        order.append(node0)
        while queue:
            v = queue.pop(0)
            for w in self.sequense[v]:
                if w not in order:
                    order.append(w)
                    queue.append(w)
        return order


if __name__ == "__main__":
    # nodes = [i+1 for i in range(8)]
    # edges=[ (1, 2),
    #         (1, 3),
    #         (2, 4),
    #         (2, 5),
    #         (4, 8),
    #         (5, 8),
    #         (3, 6),
    #         (3, 7),
    #         (6, 7)]

    # MWeb笔记中的无向图
    nodes = ['A','B','C','D','E','F','G']
    edges = [('A', 'C'),
             ('A', 'D'),
             ('A', 'F'),
             ('C', 'D'),
             ('C', 'B'),
             ('F', 'G'),
             ('G', 'E')]
    G = Gragh(nodes, edges)
    print("深度DFS: ", G.DFS('A'))
    print("广度BFS: ", G.BFS('A'))