__author__ = 'alfmunny'

'''
Title:
Merge k Sorted Lists

Questions:

Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

# Definition for singly-linked list.
# class ListNode:
# def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def __init__(self):
        pass

    def mergeKLists(self, lists):
        # use timsort O(n)
        nodes = []
        for head in lists:
            while head:
                nodes.append(head)
                head = head.next

        if not nodes:
            return

        nodes.sort(key=lambda x: x.val)

        for i in xrange(1, len(nodes)):
            nodes[i-1].next = nodes[i]

        nodes[-1].next = None
        return nodes[0]


class Solution_2:
    def __init__(self):
        pass

    def mergeKLists(self, lists):

        heap = []
        merged_list = []
        if len(lists) == 0:
            return merged_list
        if len(lists) == 1:
            return lists[0]

        for i in lists:
            for j in i:
                self.heap_push(heap, j)

        while len(heap) > 1:
            heap[1], heap[-1] = heap[-1], heap[1]
            merged_list.append(heap.pop())
            self.sink(heap, 1)

        return merged_list

    def heap_push(self, array, item):
        if len(array) == 0:
            array.append(None)

        array.append(item)
        key = len(array) - 1
        self.swim(array, key)

    def swim(self, array, key):
        while key > 1 and array[key / 2] < array[key]:
            array[key], array[key / 2] = array[key / 2], array[key]
            key /= 2

    def sink(self, array, key):
        N = len(array) - 1
        while 2*key <= N:
            child_l = 2*key
            if 2*key < N and array[2*key] < array[2*key+1]:
                    child_l = 2*key+1

            if array[key] > array[child_l]:
                break

            array[key], array[child_l] = array[child_l], array[key]
            key = child_l

def print_list(l):
    # @param {ListNode} l
    p_l = l
    while p_l is not None:
        print p_l.val,
        p_l = p_l.next


if __name__ == '__main__':

    a = [1, 3, 5, 7, 9]
    b = [2, 4, 6, 8, 10]

    s = Solution_2()
    c = s.mergeKLists([a, b])
    print c