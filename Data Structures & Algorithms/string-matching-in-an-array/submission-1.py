class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        if not words:
            return []

        def is_sub(elt,arr):
            for w in arr:
                if elt in w:
                    return True
            return False

        res = []
        for i in range(len(words)):
            print(words[:i],words[i+1:])
            if is_sub(words[i],words[:i]) or is_sub(words[i],words[i+1:]):
                res.append(words[i])

        return res