class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int res = INT_MIN;
        stack<int> st;
        int n = heights.size();
        vector<int> left(n), right(n, n);
        for(int i =0; i <n; ++i) {
            while(!st.empty() && heights[st.top()] >= heights[i]) {
                st.pop();
            }
            left[i] = st.empty() ? -1 : st.top();
            st.push(i);
        }

        // clear stack
        while(!st.empty()) {
            st.pop();
        }

        for(int i = n-1; i>=0; --i) {
            while(!st.empty() && heights[st.top()] >= heights[i]) {
                st.pop();
            }
            right[i] = st.empty() ? n : st.top();
            st.push(i);
        }
        for(int i = 0; i < n; ++i) {
            int width = right[i] - left[i] -1;
            int tmp = width*heights[i];
            res = max(res, tmp);
        }
        return res;
    }
};
