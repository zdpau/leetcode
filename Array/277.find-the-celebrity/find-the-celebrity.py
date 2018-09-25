# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        cand = 0
        # Find the candidate.
        for i in range(1, n):
            if knows(cand, i):
                cand = i          # All candidates < i are not celebrity candidates.
        # Verify the candidate.
        for i in range(n):
            candidate_knows_i = konws(cand,i)
            i_knows_candidate = knows(i,cand)
            if i != cand and candidate_knows_i or not i_knows_candidate: # 先ｏｒ后ａｎｄ。
                return -1　＃如果不是名人，返回-1
        return cand
