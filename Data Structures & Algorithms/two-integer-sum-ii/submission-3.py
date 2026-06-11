class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers)-1
            tmp = target - numbers[i]
            while l <= r:
                m = l + (r-l)//2
                if tmp == numbers[m]:
                    return [i+1, m + 1]
                elif tmp > numbers[m]:
                    l = m + 1
                else:
                    r = m - 1
        return []