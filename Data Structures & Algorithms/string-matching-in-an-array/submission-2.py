class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        if not words :
            return []

        res = []
        blob = " ".join(words)

        for w in words:
            if blob.count(w)>1:
                res.append(w)

        return res