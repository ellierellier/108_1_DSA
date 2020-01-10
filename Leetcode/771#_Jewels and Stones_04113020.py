class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        J_set = []
        count = 0
        for index in range(len(J)):
            if J[index] not in J_set:
                J_set.append(J[index])

        for i in range(len(S)):
            if S[i] in J_set:
                count += 1
        return count