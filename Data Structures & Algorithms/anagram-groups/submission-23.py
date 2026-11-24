class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # base case 
        if len(strs) == 1:
            return [strs]

        # anagram is just words that have same frequence of letters
        # can use the letters as key and value can be list of words with those letters

        res = defaultdict(list) 
        
        for s in strs:
            count = [0] * 26 # a ... z
            for c in s:
                count[ord(c) - ord("a")] += 1
            res[tuple(count)].append(s)
        
        return list(res.values())


        
        
        