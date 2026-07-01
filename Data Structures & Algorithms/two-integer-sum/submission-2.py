class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []
        for i, num in enumerate(nums): # enumerate()函数，遍历nums，取得index和value
            A.append([num, i])         # 将[值, 索引]添加到A中

        A.sort()
        i,j = 0, len(A) - 1
        while i < j:
            cur = A[i][0] + A[j][0]
            if cur == target:
                return [min(A[i][1], A[j][1]), 
                        max(A[i][1], A[j][1])]
            elif cur < target:
                i += 1
            else:
                j -= 1
        return []
        

        