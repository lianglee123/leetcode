from typing import *


class Solution:
    """
    https://www.cnblogs.com/grandyang/p/5240774.html
    """
    def canAttendMeetings(self, meetings: List):
        meetings.sort(key=lambda x: x[0])
        for i in range(1, len(meetings)):
            if meetings[i][0] < meetings[i-1][1]:
                return False
        return True

