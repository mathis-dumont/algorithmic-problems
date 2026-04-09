class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        n = len(s)
        l,r = 0,0
        res = 0
        freq = {}
        max_freq = 0

        while r < n:
            # on regarde la longueur de la sous listes et on soustrait la freq max
            # si <= k, c'est bon, res = longeur de la sous liste
            # dans le cas contraire on rétrécit la sous liste*

            # On mappe les frequences des lettres de la sous liste
            freq[s[r]] = freq.get(s[r],0) + 1
            # On stocke de manière optimale la freq max de la sous liste
            max_freq = max(max_freq, freq[s[r]])

            window_length = r - l + 1

            if window_length - max_freq <= k:
                res = max(res, window_length)

            else :
                freq[s[l]] -=1
                l+=1

            r += 1
        return res



        