from typing import *


class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        return self.dfsClone({}, node)

    def dfsClone(self, visit, node: Node):
        if not node:
            return None
        if node in visit:
            return visit[node]
        cloneNode = Node(node.val)
        visit[node] = cloneNode
        for neigh in node.neighbors:
            if neigh in visit:
                cloneNode.neighbors.append(visit[neigh])
            else:
                cloneNode.neighbors.append(self.dfsClone(visit, neigh))
        return cloneNode

