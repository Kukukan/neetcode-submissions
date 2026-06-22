class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp = {}
        stack = []
        for n in nums2:
            while stack and n > stack[-1]:
                mp[stack.pop()] = n
            stack.append(n)

        return [mp.get(num, -1) for num in nums1]