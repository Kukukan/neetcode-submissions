class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []

        leftm = [-1] *n
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                leftm[i] = st[-1]
            st.append(i)
        
        st = []
        rightm = [n] *n
        for i in range(n-1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                rightm[i] = st[-1]
            st.append(i)
        res = 0
        for i in range(n):
            width = rightm[i] - leftm[i] - 1
            area = width*heights[i]
            res = max(res, area)
        return res