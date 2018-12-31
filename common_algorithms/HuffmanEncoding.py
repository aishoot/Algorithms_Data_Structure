# Huffman编码
class Node:
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.lchild = None
        self.rchild = None

# 哈夫曼树
class HuffmanTree:
    # 以叶子节点为基础，反向建立Huffman树
    def __init__(self, ch_w):
        self.a = [Node(part[0], part[1]) for part in ch_w]  # 根据输入的字符及频数生成叶子节点
        while len(self.a) != 1:
            self.a.sort(key=lambda node: node.value, reverse=True)  # 从高到低
            c = Node(value=(self.a[-1].value + self.a[-2].value))
            c.lchild = self.a.pop(-1)
            c.rchild = self.a.pop(-1)
            self.a.append(c)
        self.root = self.a[0]   # root就是整个Huffman树
        self.b = list(range(10))  # 保存每个叶子节点的Haffuman编码,range的值只需不小于树的深度

    # 用递归的思想生成编码
    def pre(self, tree, length):  # length是编码的长度，也就是该节点路径长度
        node = tree
        if not node:
            return
        elif node.name:
            print(node.name + ":", end=' ')
            for i in range(length):
                print(self.b[i], end='')
            print('')
            return
        self.b[length] = 0
        self.pre(node.lchild, length + 1)
        self.b[length] = 1
        self.pre(node.rchild, length + 1)

    # 生成哈夫曼编码
    def get_code(self):
        self.pre(self.root, 0)


if __name__ == "__main__":
    char_weights = [('a',9), ('b',12), ('c',6), ('d',3), ('e',5), ('f',15)]
    #char_weights = [('a',0.07), ('b',0.19), ('c',0.02), ('d',0.06),
    #                ('e',0.32), ('f',0.03), ('g',0.21), ('h',0.10)]  # 教材上的例子
    tree = HuffmanTree(char_weights)
    tree.get_code()
