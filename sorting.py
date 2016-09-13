import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

#create a list in random order
def randomList(length):
	randomList = [i for i in range(length)]
	random.shuffle(randomList)
	return randomList

#create a sorted list
def sortedList(length):
	sortedList = [i for i in range(length)]
	return sortedList

#create a list in reverse order
def reverseList(length):
	sortedList = [i for i in range(length)]
	reverseList = []
	for i in range(length):
		reverseList.append(sortedList.pop())
	return reverseList	

#function to find the average
def average(results):
    total = 0
    for i in results:
        total += float(i)
    return '%f' % round(total / 5, 6)

#function to calculate time to run bubble sort
def bubble(sortList, resultList):
    startTime = time.perf_counter()
    bubbleSort(sortList)
    endTime = time.perf_counter()
    elapsedTime = endTime - startTime
    resultList.append(elapsedTime)

#function to calculate time to run selection sort
def selection(sortList, resultList):
    startTime = time.perf_counter()
    selectionSort(sortList)
    endTime = time.perf_counter()
    elapsedTime = endTime - startTime
    resultList.append(elapsedTime)

#function to calculate time to run insertion sort
def insertion(sortList, resultList):
    startTime = time.perf_counter()
    insertionSort(sortList)
    endTime = time.perf_counter()
    elapsedTime = endTime - startTime
    resultList.append(elapsedTime)

#function to calculate time to run shell sort
def shell(sortList, resultList):
    startTime = time.perf_counter()
    shellSort(sortList)
    endTime = time.perf_counter()
    elapsedTime = endTime - startTime
    resultList.append(elapsedTime)

#function to calculate time to run merge sort
def merge(sortList, resultList):
    startTime = time.perf_counter()
    mergeSort(sortList)
    endTime = time.perf_counter()
    elapsedTime = endTime - startTime
    resultList.append(elapsedTime)

#function to calculate time to run quick sort
def quick(sortList, resultList):
    startTime = time.perf_counter()
    quickSort(sortList)
    endTime = time.perf_counter()
    elapsedTime = endTime - startTime
    resultList.append(elapsedTime)    

def main():

    #list to keep track of all times for random input
    randomResults = []

    #get average time for random input with bubble sort
    results = []
    for i in range(5):
        myList = randomList(10)
        bubble(myList, results)
    bubbleResults = [average(results)]

    results = []
    for i in range(5):
        myList = randomList(100)
        bubble(myList, results)
    bubbleResults.append(average(results))

    results = []
    for i in range(5):
        myList = randomList(1000)
        bubble(myList, results)
    bubbleResults.append(average(results))

    randomResults.append(bubbleResults)

    #get average time for random input with selection sort
    results = []
    for i in range(5):
        myList = randomList(10)
        selection(myList, results)
    selectionResults = [average(results)]

    results = []
    for i in range(5):
        myList = randomList(100)
        selection(myList, results)
    selectionResults.append(average(results))

    results = []
    for i in range(5):
        myList = randomList(1000)
        selection(myList, results)
    selectionResults.append(average(results))

    randomResults.append(selectionResults)

    #get average time for random input with insertion sort
    results = []
    for i in range(5):
        myList = randomList(10)
        insertion(myList, results)
    insertionResults = [average(results)]

    results = []
    for i in range(5):
        myList = randomList(100)
        insertion(myList, results)
    insertionResults.append(average(results))

    results = []
    for i in range(5):
        myList = randomList(1000)
        insertion(myList, results)
    insertionResults.append(average(results))

    randomResults.append(insertionResults)

    #get average time for random input with shell sort
    results = []
    for i in range(5):
        myList = randomList(10)
        shell(myList, results)
    shellResults = [average(results)]

    results = []
    for i in range(5):
        myList = randomList(100)
        shell(myList, results)
    shellResults.append(average(results))

    results = []
    for i in range(5):
        myList = randomList(1000)
        shell(myList, results)
    shellResults.append(average(results))

    randomResults.append(shellResults)

    #get average time for random input with merge sort
    results = []
    for i in range(5):
        myList = randomList(10)
        merge(myList, results)
    mergeResults = [average(results)]

    results = []
    for i in range(5):
        myList = randomList(100)
        merge(myList, results)
    mergeResults.append(average(results))

    results = []
    for i in range(5):
        myList = randomList(1000)
        merge(myList, results)
    mergeResults.append(average(results))

    randomResults.append(mergeResults)

    #get average time for random input with quick sort
    results = []
    for i in range(5):
        myList = randomList(10)
        quick(myList, results)
    quickResults = [average(results)]

    results = []
    for i in range(5):
        myList = randomList(100)
        quick(myList, results)
    quickResults.append(average(results))

    results = []
    for i in range(5):
        myList = randomList(1000)
        quick(myList, results)
    quickResults.append(average(results))

    randomResults.append(quickResults)

    #list to keep track of all times for sorted input
    sortedResults = []

    #get average time for sorted input with bubble sort
    results = []
    for i in range(5):
        myList = sortedList(10)
        bubble(myList, results)
    bubbleResults = [average(results)]

    results = []
    for i in range(5):
        myList = sortedList(100)
        bubble(myList, results)
    bubbleResults.append(average(results))

    results = []
    for i in range(5):
        myList = sortedList(1000)
        bubble(myList, results)
    bubbleResults.append(average(results))

    sortedResults.append(bubbleResults)

    #get average time for sorted input with selection sort
    results = []
    for i in range(5):
        myList = sortedList(10)
        selection(myList, results)
    selectionResults = [average(results)]

    results = []
    for i in range(5):
        myList = sortedList(100)
        selection(myList, results)
    selectionResults.append(average(results))

    results = []
    for i in range(5):
        myList = sortedList(1000)
        selection(myList, results)
    selectionResults.append(average(results))

    sortedResults.append(selectionResults)

    #get average time for sorted input with insertion sort
    results = []
    for i in range(5):
        myList = sortedList(10)
        insertion(myList, results)
    insertionResults = [average(results)]

    results = []
    for i in range(5):
        myList = sortedList(100)
        insertion(myList, results)
    insertionResults.append(average(results))

    results = []
    for i in range(5):
        myList = sortedList(1000)
        insertion(myList, results)
    insertionResults.append(average(results))

    sortedResults.append(insertionResults)

    #get average time for sorted input with shell sort
    results = []
    for i in range(5):
        myList = sortedList(10)
        shell(myList, results)
    shellResults = [average(results)]

    results = []
    for i in range(5):
        myList = sortedList(100)
        shell(myList, results)
    shellResults.append(average(results))

    results = []
    for i in range(5):
        myList = sortedList(1000)
        shell(myList, results)
    shellResults.append(average(results))

    sortedResults.append(shellResults)

    #get average time for sorted input with merge sort
    results = []
    for i in range(5):
        myList = sortedList(10)
        merge(myList, results)
    mergeResults = [average(results)]

    results = []
    for i in range(5):
        myList = sortedList(100)
        merge(myList, results)
    mergeResults.append(average(results))

    results = []
    for i in range(5):
        myList = sortedList(1000)
        merge(myList, results)
    mergeResults.append(average(results))

    sortedResults.append(mergeResults)

    #get average time for sorted input with quick sort
    results = []
    for i in range(5):
        myList = sortedList(10)
        quick(myList, results)
    quickResults = [average(results)]

    results = []
    for i in range(5):
        myList = sortedList(100)
        quick(myList, results)
    quickResults.append(average(results))

    results = []
    for i in range(5):
        myList = sortedList(1000)
        quick(myList, results)
    quickResults.append(average(results))

    sortedResults.append(quickResults)

    #list to keep track of all times for reverse input
    reverseResults = []

    #get average time for reverse input with bubble sort
    results = []
    for i in range(5):
        myList = reverseList(10)
        bubble(myList, results)
    bubbleResults = [average(results)]

    results = []
    for i in range(5):
        myList = reverseList(100)
        bubble(myList, results)
    bubbleResults.append(average(results))

    results = []
    for i in range(5):
        myList = reverseList(1000)
        bubble(myList, results)
    bubbleResults.append(average(results))

    reverseResults.append(bubbleResults)

    #get average time for reverse input with selection sort
    results = []
    for i in range(5):
        myList = reverseList(10)
        selection(myList, results)
    selectionResults = [average(results)]

    results = []
    for i in range(5):
        myList = reverseList(100)
        selection(myList, results)
    selectionResults.append(average(results))

    results = []
    for i in range(5):
        myList = reverseList(1000)
        selection(myList, results)
    selectionResults.append(average(results))

    reverseResults.append(selectionResults)

    #get average time for reverse input with insertion sort
    results = []
    for i in range(5):
        myList = reverseList(10)
        insertion(myList, results)
    insertionResults = [average(results)]

    results = []
    for i in range(5):
        myList = reverseList(100)
        insertion(myList, results)
    insertionResults.append(average(results))

    results = []
    for i in range(5):
        myList = reverseList(1000)
        insertion(myList, results)
    insertionResults.append(average(results))

    reverseResults.append(insertionResults)

    #get average time for reverse input with shell sort
    results = []
    for i in range(5):
        myList = reverseList(10)
        shell(myList, results)
    shellResults = [average(results)]

    results = []
    for i in range(5):
        myList = reverseList(100)
        shell(myList, results)
    shellResults.append(average(results))

    results = []
    for i in range(5):
        myList = reverseList(1000)
        shell(myList, results)
    shellResults.append(average(results))

    reverseResults.append(shellResults)

    #get average time for reverse input with merge sort
    results = []
    for i in range(5):
        myList = reverseList(10)
        merge(myList, results)
    mergeResults = [average(results)]

    results = []
    for i in range(5):
        myList = reverseList(100)
        merge(myList, results)
    mergeResults.append(average(results))

    results = []
    for i in range(5):
        myList = reverseList(1000)
        merge(myList, results)
    mergeResults.append(average(results))

    reverseResults.append(mergeResults)

    #get average time for reverse input with quick sort
    results = []
    for i in range(5):
        myList = reverseList(10)
        quick(myList, results)
    quickResults = [average(results)]

    results = []
    for i in range(5):
        myList = reverseList(100)
        quick(myList, results)
    quickResults.append(average(results))

    results = []
    for i in range(5):
        myList = reverseList(1000)
        quick(myList, results)
    quickResults.append(average(results))

    reverseResults.append(quickResults)

    #output
    print('Input type = Random')
    print('                    avg time   avg time   avg time')
    print('   Sort function     (n=10)    (n=100)    (n=1000)')
    print('-----------------------------------------------------')
    print('      bubbleSort   ', randomResults[0][0], ' ', randomResults[0][1], ' ', randomResults[0][2])
    print('   selectionSort   ', randomResults[1][0], ' ', randomResults[1][1], ' ', randomResults[1][2])
    print('   insertionSort   ', randomResults[2][0], ' ', randomResults[2][1], ' ', randomResults[2][2])
    print('       shellSort   ', randomResults[3][0], ' ', randomResults[3][1], ' ', randomResults[3][2])
    print('       mergeSort   ', randomResults[4][0], ' ', randomResults[4][1], ' ', randomResults[4][2])
    print('       quickSort   ', randomResults[5][0], ' ', randomResults[5][1], ' ', randomResults[5][2])
    print()
    print('Input type = Sorted')
    print('                    avg time   avg time   avg time')
    print('   Sort function     (n=10)    (n=100)    (n=1000)')
    print('-----------------------------------------------------')
    print('      bubbleSort   ', sortedResults[0][0], ' ', sortedResults[0][1], ' ', sortedResults[0][2])
    print('   selectionSort   ', sortedResults[1][0], ' ', sortedResults[1][1], ' ', sortedResults[1][2])
    print('   insertionSort   ', sortedResults[2][0], ' ', sortedResults[2][1], ' ', sortedResults[2][2])
    print('       shellSort   ', sortedResults[3][0], ' ', sortedResults[3][1], ' ', sortedResults[3][2])
    print('       mergeSort   ', sortedResults[4][0], ' ', sortedResults[4][1], ' ', sortedResults[4][2])
    print('       quickSort   ', sortedResults[5][0], ' ', sortedResults[5][1], ' ', sortedResults[5][2])
    print()
    print('Input type = Reverse')
    print('                    avg time   avg time   avg time')
    print('   Sort function     (n=10)    (n=100)    (n=1000)')
    print('-----------------------------------------------------')	
    print('      bubbleSort   ', reverseResults[0][0], ' ', reverseResults[0][1], ' ', reverseResults[0][2])
    print('   selectionSort   ', reverseResults[1][0], ' ', reverseResults[1][1], ' ', reverseResults[1][2])
    print('   insertionSort   ', reverseResults[2][0], ' ', reverseResults[2][1], ' ', reverseResults[2][2])
    print('       shellSort   ', reverseResults[3][0], ' ', reverseResults[3][1], ' ', reverseResults[3][2])
    print('       mergeSort   ', reverseResults[4][0], ' ', reverseResults[4][1], ' ', reverseResults[4][2])
    print('       quickSort   ', reverseResults[5][0], ' ', reverseResults[5][1], ' ', reverseResults[5][2])

main()

