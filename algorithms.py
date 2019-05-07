import sys;
import timeit;

# Big-O notation describes how quickly runtime will grow relative to the input as the input gets arbitrarily large.


def sum1(n):
    #take an input of n and return the sume of the numbers from 0 to n
    final_sum = 0;
    for x in range(n+1): # this is a O(n)
        final_sum += x
    return final_sum


def sum2(n):
    return (n*(n+1))/2 # this is a O(n**2)


# using setitem
t = timeit.Timer()

print 'TIMEIT:'
print "sum1 is " + str(sum1(100)) + " and the time for sum1 " + str(t.timeit(sum1(100)))
print "sum2 is " + str(sum2(100)) + " and time for sum2 " + str(t.timeit(sum2(100)))


#O(1) constant

def func_constant (values):
    '''
    print first item in a list of value
    '''
    print values[0]

func_constant([1,2,3,4,5,6,7]) # no matter how big the list gets the output will always be constant (1)

#O(n) Linear is going to be a little more computational than a constant (will take longer)
def func_lin (lst):
    '''
    takes in list and prints out all values
    '''
    for val in lst:
        print val

func_lin([1,2,3,4,5,6,7])

#O(n^2) Quadratic

def func_quadratic(lst):
    #prints pairs for every item in list

    for item_1 in lst:
        for item_2 in lst:
            print (item_1, item_2)
lst = [1,2,3]

print func_quadratic(lst) #this will always have to do an n * n so it will be Quadratic as n grows

# time complexity vs. space complexity

def memory(n):
    for x in range(n): # time complexity O(n)
        print ('memory') # space complexity O(1) - becuase memory is a constant, never changes

memory(4)
