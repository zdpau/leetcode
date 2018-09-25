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
        
        因为celebrity是所有人都认识他，但他不认识任何一个人。所以如果假设0为初始的备选candidate，然后for (int i = 1; i < n; i++)这样loop下去，
        遇到第一个备选candidate认识的，就把备选candidate替换成那个被认识的（因为它破坏了不认识任何人的规则），
        若k为candidate，则0~k-1不可能是celebrity，因为肯定认识至少一个人；k+1~n-1也不可能是celebrity，因为有至少一个人（candidate）不认识他。
        一个合法的candidate，应该要做到不认识loop之后剩下的所有人，这样loop到最后，你就会产生一个candidate，然后做同样的验证即可。
        """
        cand = 0
        # Find the candidate.
        for i in range(1, n):
            if knows(cand, i):    # 相当于if True: cand = i. 如果cand认识i,那么将i设置为cand. 0认识1，将1设为cand,但1认不认识0不知道
                cand = i          # All candidates < i are not celebrity candidates.
        # Verify the candidate.
        for i in range(n): 
            # 由于candidate后面的人和candidate，knows(candidate,i)肯定都为0，所以不用再判断！
            candidate_knows_i = knows(cand,i) # 要返回1的话，应该认识。如果是名人的话，是false
            i_knows_candidate = knows(i,cand) # 要返回1的话，不应该认识。
            if i != cand and candidate_knows_i or not i_knows_candidate: 
                #等价于(i!= cand && knows(cand,i))和(i!= cand && !knows(i, cand)) return -1;
                #i是否都认识candidate，有一个认识，就不是celebrity。
                #candidate不认识前面的人，认识的话，就不是celebrity
                return -1　＃如果不是名人，返回-1
        return cand
