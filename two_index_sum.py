import pdb;

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        h is a hash table, a hash table is the best way to maintain a mapping
        of each element in an array to its index
        """
        h = {}
        for i, num in enumerate(nums):
            # i starts at 0
            # print "i is =%s " %(i)
            n = target - num
            if n not in h:
                h[num] = i
                # prints in the format of {enum, i}, where enum starts at 0
                print h
            else:
                return [h[n], i]

my_function = Solution()

# why is dubbuger not working with class?
# pdb.set_trace()

print my_function.twoSum([1,2,3,4,5,6], 10)
