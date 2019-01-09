"""
Math 590
Project 1
Fall 2018

Partner 1: Yuefan Yu(yy225)
Partner 2: Chentao Wang(cw373)
Date: 10-24-2018
"""

# Import time, random, plotting, stats, and numpy.
import time
import random
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy
"""
SelectionSort
Description: Sorting the array using Selection Sort, an in-place algorithm, O(n^2)
Input: array(contains and only contains numbers, at least one number)
Output:Sorted array
"""
def SelectionSort(A):

    # the number before i are currently sorted
    # the number after i include i are unsorted
    for i in range(0, len(A)):
        minIndex = i

        # find the min number in unsorted list
        for j in range(i+1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j

        # place the min number we found at the last of sorted list
        A[i], A[minIndex] = A[minIndex], A[i]
    return A


"""
InsertionSort
Description: Sorting the array using Insertion Sort, an in-place algorithm, O(n^2)
Input:array(contains and only contains numbers, at least one number)
Output:Sorted array
"""
def InsertionSort(A):

    # the number before i and i are currently sorted
    # the number after i are unsorted
    for i in range(0, len(A)-1):
        curIndex = i+1    # the first number in the unsorted list
        j = i

        # swap that number and any number larger than it within the sorted list
        # until it is at the right position
        while A[curIndex] < A[j] and j >= 0:
            A[curIndex], A[j] = A[j], A[curIndex]
            curIndex = j
            j = j-1
    return A
"""
BubbleSort
Description: Sorting the array using Bubble Sort, and in-place algorithm, O(n^2)
Input:array(contains and only contains numbers, at least one number)
Output:Sorted array
"""
def BubbleSort(A):

    # go through whole array twice
    for i in range(0, len(A)-1):
        count = 0
        for j in range(0, len(A)-i-1):

            # swap two numbers if first one is larger than the second
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
                count = count+1

        # finish sorting if no swap in arbitrary loop
        if count == 0:
            break
    return A


"""
Merge2Array
Description: Merge 2 Sorted array (B, C) and store the merged array in A
Input:Array(store the result), array(the first sorted list), array(the second sorted list)
Output: None
"""
def Merge2Array(A, B, C):

    # put all numbers in B into A
    for i in range(0, len(B)):
        A[i] = B[i]
    i = len(C)-1
    j = len(B)-1
    k = len(A)-1

    # sort from the last position of A to the beginning
    # compare the element in B and C from end to beginning
    # pick the larger one into A
    while i >= 0:
        if C[i] < A[j] and j >= 0:
            A[k] = A[j]
            j = j-1
        else:
            A[k] = C[i]
            i = i-1
        k = k-1

"""
MergeSort
Description: Sorting the array using Merge Sort, O(nlogn)
Input:array(contains and only contains numbers, at least one number)
Output:sorted array
"""
def MergeSort(A):

    # Base Cases: If the array has 1 element, it is sorted.
    # If the array has 2 elements, swap if needed and return.
    if len(A) == 1:
        return A
    elif len(A) == 2:
        if A[0] > A[1]:
            A[0], A[1] = A[1], A[0]
        return A

    # split the list into two halves
    B = A[0:len(A)//2]
    C = A[len(A)//2:len(A)]

    # sort each half of the array
    B = MergeSort(B)
    C = MergeSort(C)

    # merge the two already sorted halves
    Merge2Array(A, B, C)
    return A


"""
QuickSort
Description: Sorting the array using Quick Sort, in-place algorithm, O(nlogn)
Input:array(contains and only contains numbers, at least one number),i(the beginning of the array),j(the length of the array)
Output: sorted array

Sort a list A with the call QuickSort(A, 0, len(A)).
"""
def QuickSort(A, i, j):
    start = i
    len = j

    # base case: if there is 0 or 1 number in array, no more operation
    if len <= 1:
        return A
    j = start+len-1

    # pick the pivot
    pivot = i
    while i < j:

        # find the number larger than pivot from right to left
        while A[j] >= A[pivot]and j > i:
            j = j-1
        # find the number smaller than pivot from left to right
        while A[i] <= A[pivot] and i < j:
            i = i+1

        # swap those two numbers
        A[i], A[j] = A[j], A[i]

    # swap the pivot with the number where i and j met
    A[pivot], A[i] = A[i], A[pivot]

    # sort the element smaller than pivot
    QuickSort(A, start, i-start)
    # sort the element larger than pivot
    QuickSort(A, i+1, len-i+start-1)
    return A
"""
isSorted

This function will take in an original unsorted list and a sorted version of
that same list, and return whether the list has been properly sorted.

Note that this function does not change the unsorted list.

INPUTS
unA: the original unsorted list
sA:  the supposedly sorted list

OUTPUTS
returns true or false
"""


def isSorted(unA, sA):
    # Copy the unsorted list.
    temp = unA.copy()
    # Use python's sort.
    temp.sort()
    # Check equality.
    return temp == sA

"""
testingSuite

This function will run a number of tests using the input algorithm, check if
the sorting was successful, and print which tests failed (if any).

This is not an exhaustive list of tests by any means, but covers the edge
cases for your sorting algorithms.

INPUTS
alg: a string indicating which alg to test, the options are:
    'SelectionSort'
    'InsertionSort'
    'BubbleSort'
    'MergeSort'
    'QuickSort'

OUTPUTS
Printed statements indicating which tests passed/failed.
"""
def testingSuite(alg):
    # First, we seed the random number generator to ensure reproducibility.
    random.seed(1)

    # List of possible algs.
    algs = ['SelectionSort', 'InsertionSort', \
            'BubbleSort', 'MergeSort', 'QuickSort']

    # Make sure the input is a proper alg to consider.
    if not alg in algs:
        raise Exception('Not an allowed algorithm. Value was: {}'.format(alg))
    
    # Create a list to store all the tests.
    tests = []

    # Create a list to store the test names.
    message = []

    # Test 1: singleton array
    tests.append([1])
    message.append('singleton array')

    # Test 2: repeated elements
    tests.append([1,2,3,4,5,5,4,3,2,1])
    message.append('repeated elements')

    # Test 3: all repeated elements
    tests.append([2,2,2,2,2,2,2,2,2,2])
    message.append('all repeated elements')

    # Test 4: descending order
    tests.append([10,9,8,7,6,5,4,3,2,1])
    message.append('descending order')

    # Test 5: sorted input
    tests.append([1,2,3,4,5,6,7,8,9,10])
    message.append('sorted input')

    # Test 6: negative inputs
    tests.append([-1,-2,-3,-4,-5,-5,-4,-3,-2,-1])
    message.append('negative inputs')

    # Test 7: mixed positive/negative
    tests.append([1,2,3,4,5,-1,-2,-3,-4,-5,0])
    message.append('mixed positive/negative')

    # Test 8: array of size 2^k - 1
    temp = list(range(0,2**6-1))
    random.shuffle(temp)
    tests.append(temp)
    message.append('array of size 2^k - 1')

    # Test 9: random real numbers
    tests.append([random.random() for x in range(0,2**6-1)])
    message.append('random real numbers')

    # Store total number of passed tests.
    passed = 0

    # Loop over the tests.
    for tInd in range(0,len(tests)):
        # Copy the test for sorting.
        temp = tests[tInd].copy()

        # Try to sort, but allow for errors.
        try:
            # Do the sort.
            eval('%s(tests[tInd])' % alg) if alg != 'QuickSort' \
            else eval('%s(tests[tInd],0,len(tests[tInd]))' % alg)
            # Check if the test succeeded.
            if isSorted(temp, tests[tInd]):
                print('Test %d Success: %s' % (tInd+1, message[tInd]))
                passed += 1
            else:
                print('Test %d FAILED: %s' % (tInd+1, message[tInd]))

        # Catch any errors.
        except Exception as e:
            print('')
            print('DANGER!')
            print('Test %d threw an error: %s' % (tInd+1, message[tInd]))
            print('Error: ')
            print(e)
            print('')

    # Done testing, print and return.
    print('')
    print('%d/9 Tests Passed' % passed)
    return

"""
measureTime

This function will generate lists of varying lengths and sort them using your
implemented fuctions. It will time these sorting operations, and store the
average time across 30 trials of a particular size n. It will then create plots
of runtime vs n. It will also output the slope of the log-log plots generated
for several of the sorting algorithms.

INPUTS
sortedFlag: set to True to test with only pre-sorted inputs
    (default = False)
numTrials: the number of trials to average timing data across
    (default = 30)

OUTPUTS
A number of genereated runtime vs n plot, a log-log plot for several
algorithms, and printed statistics about the slope of the log-log plots.
"""
def measureTime(sortedFlag = False, numTrials = 30):
    # Print whether we are using sorted inputs.
    if sortedFlag:
        print('Timing algorithms using only sorted data.')
    else:
        print('Timing algorithms using random data.')
    print('')
    print('Averaging over %d Trials' % numTrials)
    print('')
    
    # First, we seed the random number generator to ensure consistency.
    random.seed(1)

    # We now define the range of n values to consider.
    if sortedFlag:
        # Need to look at larger n to get a good sense of runtime.
        # Look at n from 20 to 980.
        # Note that 1000 causes issues with recursion depth...
        N = list(range(1,50))
        N = [20*x for x in N]
    else:
        # Look at n from 10 to 500.
        N = list(range(1,51))
        N = [10*x for x in N]

    # Store the different algs to consider.
    algs = ['SelectionSort', 'InsertionSort', \
            'BubbleSort', 'MergeSort', \
            'QuickSort', 'list.sort']

    # Preallocate space to store the runtimes.
    tSelectionSort = N.copy()
    tInsertionSort = N.copy()
    tBubbleSort = N.copy()
    tMergeSort = N.copy()
    tQuickSort = N.copy()
    tPython = N.copy()

    # Create some flags for whether each sorting alg works.
    correctFlag = [True, True, True, True, True, True]

    # Loop over the different sizes.
    for nInd in range(0,len(N)):
        # Get the current value of n to consider.
        n = N[nInd]
        
        # Reset the running sum of the runtimes.
        timing = [0,0,0,0,0,0]
        
        # Loop over the 30 tests.
        for test in range(1,numTrials+1):
            # Create the random list of size n to sort.
            A = list(range(0,n))
            A = [random.random() for x in A]

            if sortedFlag:
                # Pre-sort the list.
                A.sort()

            # Loop over the algs.
            for aI in range(0,len(algs)):
                # Grab the name of the alg.
                alg = algs[aI]

                # Copy the original list for sorting.
                B = A.copy()
                
                # Time the sort.
                t = time.time()
                eval('%s(B)' % alg) if aI!=4 else eval('%s(B,0,len(B))' % alg)
                t = time.time() - t

                # Ensure that your function sorted the list.
                if not isSorted(A,B):
                    correctFlag[aI] = False

                # Add the time to our running sum.
                timing[aI] += t

        # Now that we have completed the numTrials tests, average the times.
        timing = [x/numTrials for x in timing]

        # Store the times for this value of n.
        tSelectionSort[nInd] = timing[0]
        tInsertionSort[nInd] = timing[1]
        tBubbleSort[nInd] = timing[2]
        tMergeSort[nInd] = timing[3]
        tQuickSort[nInd] = timing[4]
        tPython[nInd] = timing[5]

    # If there was an error in one of the plotting algs, report it.
    for aI in range(0,len(algs)-1):
        if not correctFlag[aI]:
            print('%s not implemented properly!!!' % algs[aI])
            print('')

    # Now plot the timing data.
    for aI in range(0,len(algs)):
        # Get the alg.
        alg = algs[aI] if aI != 5 else 'Python'

        # Plot.
        plt.figure()
        eval('plt.plot(N,t%s)' % alg)
        plt.title('%s runtime versus n' % alg)
        plt.xlabel('Input Size n')
        plt.ylabel('Runtime (s)')
        if sortedFlag:
            plt.savefig('%s_sorted.png' % alg, bbox_inches='tight')
        else:
            plt.savefig('%s.png' % alg, bbox_inches='tight')

    # Plot them all together.
    plt.figure()
    fig, ax = plt.subplots()
    ax.plot(N,tSelectionSort, label='Selection')
    ax.plot(N,tInsertionSort, label='Insertion')
    ax.plot(N,tBubbleSort, label='Bubble')
    ax.plot(N,tMergeSort, label='Merge')
    ax.plot(N,tQuickSort, label='Quick')
    ax.plot(N,tPython, label='Python')
    legend = ax.legend(loc='upper left')
    plt.title('All sorting runtimes versus n')
    plt.xlabel('Input Size n')
    plt.ylabel('Runtime (s)')
    if sortedFlag:
        plt.savefig('sorting_sorted.png', bbox_inches='tight')
    else:
        plt.savefig('sorting.png', bbox_inches='tight')

    # Now look at the log of the sort times.
    logN = [(numpy.log(x) if x>0 else -6) for x in N]
    logSS = [(numpy.log(x) if x>0 else -6) for x in tSelectionSort]
    logIS = [(numpy.log(x) if x>0 else -6) for x in tInsertionSort]
    logBS = [(numpy.log(x) if x>0 else -6) for x in tBubbleSort]
    logMS = [(numpy.log(x) if x>0 else -6) for x in tMergeSort]
    logQS = [(numpy.log(x) if x>0 else -6) for x in tQuickSort]

    # Linear regression.
    mSS, _, _, _, _ = stats.linregress(logN,logSS)
    mIS, _, _, _, _ = stats.linregress(logN,logIS)
    mBS, _, _, _, _ = stats.linregress(logN,logBS)

    # Plot log-log figure.
    plt.figure()
    fig, ax = plt.subplots()
    ax.plot(logN,logSS, label='Selection')
    ax.plot(logN,logIS, label='Insertion')
    ax.plot(logN,logBS, label='Bubble')
    legend = ax.legend(loc='upper left')
    plt.title('Log-Log plot of runtimes versus n')
    plt.xlabel('log(n)')
    plt.ylabel('log(runtime)')
    if sortedFlag:
        plt.savefig('log_sorted.png', bbox_inches='tight')
    else:
        plt.savefig('log.png', bbox_inches='tight')

    # Print the regression info.
    print('Selection Sort log-log Slope (all n): %f' % mSS)
    print('Insertion Sort log-log Slope (all n): %f' % mIS)
    print('Bubble Sort log-log Slope (all n): %f' % mBS)
    print('')

    # Now strip off all n<200...
    logN = logN[19:]
    logSS = logSS[19:]
    logIS = logIS[19:]
    logBS = logBS[19:]
    logMS = logMS[19:]
    logQS = logQS[19:]

    # Linear regression.
    mSS, _, _, _, _ = stats.linregress(logN,logSS)
    mIS, _, _, _, _ = stats.linregress(logN,logIS)
    mBS, _, _, _, _ = stats.linregress(logN,logBS)
    mMS, _, _, _, _ = stats.linregress(logN,logMS)
    mQS, _, _, _, _ = stats.linregress(logN,logQS)

    # Print the regression info.
    print('Selection Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mSS))
    print('Insertion Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mIS))
    print('Bubble Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mBS))
    print('Merge Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mMS))
    print('Quick Sort log-log Slope (n>%d): %f' \
          % (400 if sortedFlag else 200, mQS))

    # Close all figures.
    plt.close('all')


if __name__=="__main__":
    print('SelectionSort')
    testingSuite('SelectionSort')
    print('InsertionSort')
    testingSuite('InsertionSort')
    print('BubbleSort')
    testingSuite('BubbleSort')
    print('MergeSort')
    testingSuite('MergeSort')
    print('QuickSort')
    testingSuite('QuickSort')
    measureTime()
