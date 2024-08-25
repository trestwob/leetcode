class Twosum:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    
    def twosum(self):
        numToIndex = {}
        for i, num in enumerate(self.nums):
            targetNumber = self.target - num
#            print(targetNumber)
#            print(numToIndex)
            if targetNumber in numToIndex:
                return [numToIndex[targetNumber],i]

            numToIndex[num] = i
        
        return None
