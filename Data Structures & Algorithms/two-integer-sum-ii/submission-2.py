class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sorted(numbers)
        left, right = 0, len(numbers) -1
        print(numbers[left])
        print(numbers[right])
        while left < right:
            comp = numbers[left] + numbers[right]
            print(comp)
            if comp == target:
                return [left + 1, right + 1]
            else:
                if comp < target:
                    left += 1
                else:
                    right -= 1
        return []