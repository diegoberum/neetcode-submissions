class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums: 
            if num not in counts: 
                counts[num] = 1
            elif num in counts:
                counts[num] += 1

        sort_count = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)
        return list(sort_count[:k])
        
        