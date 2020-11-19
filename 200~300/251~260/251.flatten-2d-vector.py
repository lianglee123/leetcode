from typing import *




class Solution:
    def __init__(self, vec2d):
        self.row = 0
        self.col = 0
        self.vec2d = vec2d

    def next(self):
        res =  self.vec2d[self.row][self.col]
        self.col += 1
        return res

    def hasNext(self):
        while self.row < len(self.vec2d) and self.col >= len(self.vec2d[self.row]):
            self.row, self.col = self.row + 1, 0
        return self.row < len(self.vec2d)