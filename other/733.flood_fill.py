from typing import *


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or not image[0]:
            return image
        recorder = set()
        self.dfsSearch(image, sr, sc, image[sr][sc], recorder)
        for r, c in recorder:
            image[r][c] = newColor
        return image


    def dfsSearch(self, image, r, c, targetColor, recorder: Set):
        print(r, c)
        if image[r][c] != targetColor: # 此路不通
            return

        if (r, c) in recorder:  # 此路已经走过
            return
        recorder.add((r, c))

        preR = r - 1
        if preR >= 0:
            self.dfsSearch(image, preR, c, targetColor, recorder)

        nextR = r + 1
        if nextR < len(image):
            self.dfsSearch(image, nextR, c, targetColor, recorder)

        preC = c - 1
        if preC >= 0:
            self.dfsSearch(image, r, preC, targetColor, recorder)

        nextC = c + 1
        if nextC < len(image[0]):
            self.dfsSearch(image, r, nextC, targetColor, recorder)

if __name__ == '__main__':
    from utils import pprint
    s = Solution().floodFill
    # image = [
    #     [1,1,1],
    #     [1,1,0],
    #     [1,0,1]
    # ]
    # sr = 1
    # sc = 1
    # newColor = 2
    # pprint(s(image, sr, sc, newColor))
    image = [
        [0, 0, 0],
        [0, 0, 0]
    ]
    pprint(s(image, 0, 0, 2))