class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero = 0

        for elem in nums:
            if elem == 0:
                
                zero+=1
        for i in range(zero):
            nums.remove(0)
        for elem in range(zero):
            nums.append(0)
        