# 二叉堆的实现(建立最小堆)
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    # 最小孩子结点
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:  # 孩子结点超出堆长度
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:  # 左孩子结点小于右孩子结点
                return i * 2
            else:
                return i * 2 + 1

    # 最小堆，小元素“上浮”
    def percUp(self, i):  # i:元素索引号
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:  # 元素小于父节点，元素位置互换
                self.heapList[i//2],self.heapList[i] = self.heapList[i],self.heapList[i//2]
            i = i // 2

    # 将新元素加入到堆中
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)  # 从最后一个位置插入只能上浮

    # 最小堆，大元素“下沉”
    def percDown(self, i):  # i:元素索引号
        while i * 2 <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                self.heapList[i],self.heapList[mc] = self.heapList[mc],self.heapList[i]
            i = mc  # 可能还不是最大，继续往下沉

    # 返回堆中的最小项，同时从堆中删除
    def delMin(self):
        retval = self.heapList[1]  # 最小顶
        self.heapList[1] = self.heapList[self.currentSize]  # 将最后一个元素放到堆顶
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)  # 堆顶元素下沉
        return retval

    # 从列表建立二叉堆，索引从1开始；这里应该是最小堆
    def buildHeap(self, alist):
        i = len(alist) // 2  # 非叶子结点个数，结点下沉
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]  # 首位从0开始
        while i > 0:  # i=2,1是非叶子结点编号
            self.percDown(i)
            i = i - 1


if __name__ == "__main__":
    bh = BinHeap()
    bh.buildHeap([9, 5, 6, 2, 3])

    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())
    print(bh.delMin())