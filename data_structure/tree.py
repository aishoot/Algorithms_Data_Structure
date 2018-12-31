#!/usr/bin/python
# -*- coding: utf-8 -*-
# 二叉树结点表示及树的创建
class Node:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree:
    def __init__(self, root=None):
        self.root = root

    # 为树添加节点
    def add(self, elem):
        node = Node(elem)
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)  # 所有的节点都在里边
            # 对已有的节点进行层次遍历
            while queue:  # 当列表中还存在元素
                cur = queue.pop(0)  # 弹出队列第一个元素
                if cur.lchild == None:
                    cur.lchild = node   # 原来的self.root会跟着被添加，对象地址相同
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:   # 如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    # 递归实现先序遍历
    def preorder(self, root):
        if root == None:
            return []
        result = [root.elem]
        left_item = self.preorder(root.lchild)
        right_item = self.preorder(root.rchild)
        return result + left_item + right_item

    # 递归实现中序遍历
    def inorder(self, root):
        if root == None:
            return []
        result = [root.elem]
        left_item = self.inorder(root.lchild)
        right_item = self.inorder(root.rchild)
        return left_item + result + right_item

    # 递归实现后序遍历
    def postorder(self, root):
        if root == None:
            return []
        result = [root.elem]
        left_item = self.postorder(root.lchild)
        right_item = self.postorder(root.rchild)
        return left_item + right_item + result

    # 利用队列实现树的层次遍历(广度优先搜索)BFS
    def BFS(self, root):
        if root == None:
            return []
        result = []  # 所有结果
        queue = []
        queue.append(self.root)
        while queue:  # queue中还有元素时
            cur = queue.pop(0)
            result.append(cur.elem)
            if cur.lchild != None:
                queue.append(cur.lchild)
            if cur.rchild != None:
                queue.append(cur.rchild)
        return result


if __name__ == "__main__":
    t = Tree()
    for i in range(10):
        t.add(i)
    print("层次遍历BFS:", t.BFS(t.root))
    print("先序遍历:", t.preorder(t.root))
    print("中序遍历:", t.inorder(t.root))
    print("后序遍历:", t.postorder(t.root))
