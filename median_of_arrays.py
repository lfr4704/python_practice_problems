import pdb;
import math;

# find the median of two sorted arraysself.
# eg
# arr1 = [1,3,5]
# arr2 = [2,4,6]

# median(arr1, arr2) = 3.5
#Questions for interviewer:
#1. Are the arrays the same lenght?
#2. How do you want to deal with the two median elements (this example is averaging them, but he may said just return the two median elements)

#the O(n) way not acceptable in interview
# def find_median_of_arrays(arr1, arr2):
#     arr1.extend(arr2) # this merges arrays
#     arr1.sort()
#
#     n=len(arr1)
#
#     if n % 2 == 0: # if array is odd we need to take average  + middle -1
#         return (arr1[n/2] + arr1[n/2 -1]) / 2.0 #make one number float for python 2
#     else:
#         return arr1[n/2] # if array is even we need to take middle number
#
# print("answer for odd array " + str(find_median_of_arrays([1,2,3],[4,5,6,7])))
# print("answer for even array " + str(find_median_of_arrays([1,2,3],[4,5,6,])))


#the O(log n) way - this is the respose you need to provide in interviews

# concept to solve the problem:
# 1. define a range that contains the kth elements
# 2. repeatedly eliminate half (or any fraciton) of the elements in the rage


# We consider array1[i] to be the first element in array1, index = 0
# We consider array2[x] to be the first element in array2, index = 0

# def getKth(array1, i, array2, x, k):
#     if i == len(array1): #checks for empty array1
#         return array2[x + k]
#     elif x == len(array2): #checks for empty array2
#         return array1[i + k]
#     elif k == 0: # if combined total_nums = 1, then total_nums/2 = 0
#         return min(array1[i], array2[x])
#
#     # code below will execute if all the conditions above are false
#     mid1 = min(len(array1) - i, (k + 1)/2)
#     mid2 = min(len(array2) - x, (k + 1)/2)
#     a = array1[i + mid1 - 1]
#     b = array2[x + mid2 - 2]
#
#     if a < b:
#         return getKth(array1, i + mid1, array2, x, k - mid1)
#     return getKth(array1, i, array2, x + mid2, k - mid2)
#
# #This function assumes that we have at least 1 number in the array
# def findMedianSortedArrays(nums1, nums2):
#     total_nums = len(nums1) + len(nums2)
#
#     if total_nums % 2 == 0:
#         first = getKth(nums1, 0, nums2, 0, total_nums/2 -1)
#         second = getKth(nums1, 0, nums2, 0, total_nums/2)
#         return (first + second) / 2.0
#
#     else:
#         return getKth(nums1, 0, nums2, 0, total_nums/2)
#
# # print getKth([1,2,3],0,[4,5,6],0,2)
# # print getKth([1,2,3],0,[4,5,6],0,3)
# print findMedianSortedArrays([1,2,3], [4,5,6])
# pbd.set_trace()


#my attempt to solve the problem above in a O(log(n+m))
#watch this video for explanation https://www.youtube.com/watch?v=LPFhl65R7ww
def getMedianOfSortedArray(input_1, input_2):
    if len(input_1) > len(input_2):
        return getMedianOfSortedArray(input_2,input_1)

    x = len(input_1)
    y = len(input_2)
    start = 0
    high = x

    while start <= high:
        partitionX = (start + high)/2
        partitionY = (x + y + 1)/2 - partitionX

        # if partitionX is 0 it means nothing is there on the left side, use -INF for maxLeftX
        #if partitionX is lenght of input array then there is nothing on the right side, use +Inf for minRightX
        if partitionX == 0:
            maxLeftX = float('-inf')
        else:
            maxLeftX = input_1[partitionX - 1]

        if partitionX == x:
            minRightX = float('inf')
        else:
            minRightX = input_1[partitionX]

        if partitionY == 0:
            maxLeftY = float('-inf')
        else:
            maxLeftY = input_2[partitionY - 1]

        if partitionY == y:
            minRightY = float('inf')
        else:
            minRightY = input_2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX,maxLeftY) + min(minRightX, minRightY)) / 2.0

            else:
                return max(maxLeftX, maxLeftY)

        elif maxLeftX > minRightY:
            high = partitionX - 1

        else:
            start = partitionX + 1
    else:
        print "illegal argument exception"

    pdb.set_trace()

print getMedianOfSortedArray([1,3,8,9,15],[7,11,18,19,21,25])
print getMedianOfSortedArray([23,26,31,35],[3,5,7,9,11,16])
print getMedianOfSortedArray([23,26,31,35,45,56,78],[3,5,7,9,11,16])
