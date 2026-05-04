class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for n in nums:
            if n in hashSet: # Checking if duplicate exists in the hash set
                return True
            hashSet.add(n) # If not present, add the number in the hash set
        return False
