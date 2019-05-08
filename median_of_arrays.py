# find the median of two sorted arraysself.
# eg
# arr1 = [1,3,5]
# arr2 = [2,4,6]

# median(arr1, arr2) = 3.5
#Questions for interviewer:
#1. Are the arrays the same lenght?
#2. How do you want to deal with the two median elements (this example is averaging them, but he may said just return the two median elements)

#the O(n) way not acceptable in interview
def find_median_of_arrays(arr1, arr2):
    arr1.extend(arr2) # this merges arrays
    arr1.sort()

    n=len(arr1)

    if n % 2 == 0: # if array is odd we need to take average  + middle -1
        return (arr1[n/2] + arr1[n/2 -1]) / 2.0 #make one number float for python 2
    else:
        return arr1[n/2] # if array is even we need to take middle number

print("answer for odd array " + str(find_median_of_arrays([1,2,3],[4,5,6,7])))
print("answer for even array " + str(find_median_of_arrays([1,2,3],[4,5,6,])))


#the O(log n) way - this is the respose you need to provide in interviews

# concept to solve the problem:
# 1. define a range that contains the kth elements
# 2. repeatedly eliminate half (or any fraciton) of the elements in the rage


# We consider array1[i] to be the first element in array1
# We consider array2[x] to be the first element in array2
def getKth(array1, i, array2, x, k):
    if i == len(array1):
        return array2[x + k]
    elif x == len(array2):
        return array1[i + k]
    elif k == 0:
        return min(array1[i], array2[x])

    mid1 = min(len(array1) - i, (k + 1)/2)
    mid2 = min(len(array2) - x, (k + 1)/2)
    a = array1[i + mid1 - 1]
    b = array2[x + mid2 - 2]

    if a < b:
        return getKth(array1, i + mid1, array2, x, k - mid1)
    return getKth(array1, i, array2, x + mid2, k - mid2)

#This function assumes that we have at least 1 number in the array
def findMedianSortedArrays(nums1, nums2):
    total_nums = len(nums1) + len(nums2)
    midpoint = total_nums/2 + 1

    if total_nums % 2 == 0:
        first = getKth(nums1, 0, nums2, 0, total_nums/2 -1)
        second = getKth(nums1, 0, nums2, 0, total_nums/2)
        return (first + second) / 2.0
    else:
        return getKth(nums1, 0, nums2, 0, total_nums//2)

# print getKth([1,2,3],0,[4,5,6],0,2)
# print getKth([1,2,3],0,[4,5,6],0,3)
print findMedianSortedArrays([1,2,3], [4,5,6])
