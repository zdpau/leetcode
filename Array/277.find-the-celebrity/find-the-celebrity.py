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
        
        如果a认识b，则a不会是名人；如果a不认识b，则b不会是名人。因此每询问一次a是否认识b，都可以排除掉一个人。所以在O(n)时间内就可以排除掉n-1个人。
        最后还要检查确认，是否其他人都认识这个人，以及这个人都不认识其他人。

        """
        cand = 0
        # Find the candidate.
        for i in range(1, n):
            if knows(cand, i):    # 
                cand = i          # All candidates < i are not celebrity candidates.
        # Verify the candidate.
        for i in range(n):
            candidate_knows_i = konws(cand,i) # 判断cand是否认识i
            i_knows_candidate = knows(i,cand) # 判断i是否认识cand
            # 假如i不是cand,但是
            if i != cand and candidate_knows_i or not i_knows_candidate: #先or后and。如果i不是cand,并且
                return -1　＃如果不是名人，返回-1
        return cand
