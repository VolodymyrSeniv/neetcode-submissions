class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) < 2:
            return [-1]
        greatest_from_the_right = 0
        final_arr = []
        for i in range(1, len(arr)):
            final_arr.append(max(arr[i:]))
        final_arr.append(-1)
        return final_arr
        