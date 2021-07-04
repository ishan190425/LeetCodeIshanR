class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        ind = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                ind.append(i)
                if len(ind) > 2 :
				## need to swap more than one time
                    return False
        if len(ind) == 0:
            return True
		
        return len(ind) == 2 and s1[ind[0]] == s2[ind[1]] and s1[ind[1]] == s2[ind[0]]
