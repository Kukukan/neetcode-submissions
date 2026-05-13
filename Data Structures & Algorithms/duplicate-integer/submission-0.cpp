class Solution {
public:
    bool hasDuplicate(vector<int>& a) {
        unordered_set<int> s;
        for(auto i : a) {
            if(s.count(i)) {
                return true;
            }
            s.insert(i);
        }
        return false;
    }
};
