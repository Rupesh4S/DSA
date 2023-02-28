from collections import Counter


class Solution:
    """Return Top k elements which are more frequent"""

    def find_top_k_elements(self, k, nums):
        buckets = [[] for _ in range(len(nums))]
        Count = Counter(nums).items()
        for num, freq in Count:
            buckets[freq].append(num)
        flatten = [item for bucket in buckets for item in bucket]
        return flatten[::-1][:k]


print(Solution().find_top_k_elements(2, [1, 1, 1, 2, 2, 3]))
