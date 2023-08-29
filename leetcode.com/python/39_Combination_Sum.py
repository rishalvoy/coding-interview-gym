class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        allCandidates ,runningCandidate = [], []
        self.generateCandidates(candidates, runningCandidate, target, allCandidates)
        return allCandidates

    def generateCandidates(self, originalCandidates, runningCandidate, target, allCandidates):
        if sum(runningCandidate) >= target:
            finalCandidate = sorted(list(runningCandidate))
            if sum(finalCandidate) == target and finalCandidate not in allCandidates:
                allCandidates.append(finalCandidate)
            return

        for i in range(len(originalCandidates)):
            candidate = originalCandidates[i]
            runningCandidate.append(candidate)
            self.generateCandidates(originalCandidates, runningCandidate, target, allCandidates)
            runningCandidate.pop() # Backtracking
