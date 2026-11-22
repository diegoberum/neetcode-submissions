class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        
        sort_counts = sorted(counts.keys(), key=lambda x: counts[x], reverse=True)

        return sort_counts[:k]

        
        