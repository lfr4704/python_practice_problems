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
    return (n*(n+1))/2 # this is a O(n**2/2)


# using setitem
t = timeit.Timer()

print 'TIMEIT:'
print "sum1 is " + str(sum1(100)) + " and the time for sum1 " + str(t.timeit(sum1(100)))
print "sum2 is " + str(sum2(100)) + " and time for sum2 " + str(t.timeit(sum2(100)))
