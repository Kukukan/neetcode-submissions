class Solution:
    def isValid(self, s: str) -> bool:
        chars = {')' : '(', '}' : '{', ']' : '['}
        st = []
        for c in s:
            if c in chars:
                if st and st[-1] == chars[c]:
                    st.pop()
                else:
                    return False
            else:
                st.append(c)
        return True if not st else False