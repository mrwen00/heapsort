
def maxHeapify(A, length, i):      ### Heap: is likes as binary tree which has left and right node
    left = 2*i + 1
    right = 2*i + 2
    if left <= length - 1 and A[left] > A[i]:
        largest = left
    else:
        largest = i
    if right <= length - 1 and A[right] > A[largest]:
        largest = right
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, length, largest)


def buildMaxHeap(A, length):
    for i in range((length - 1)/2, -1, -1):
        maxHeapify(A,length, i)


def heapSort(A):
    buildMaxHeap(A, len(A))
    print "Build max heap ", A
    HeapSize = len(A)
    for i in range(len(A)):
        A[0], A[HeapSize - 1] = A[HeapSize - 1], A[0]
        HeapSize = HeapSize - 1
        maxHeapify(A, HeapSize, 0)

def bubbleSort(A):
    for i in range(len(A)):
        for j in range(len(A)-1, i, -1):
            if A[j] < A[j - 1]:
                A[j], A[j-1] = A[j-1], A[j]


A = [16,4,10,14,7,9,3,2,8,1,11,13,25,51,39,24,5,10]

#bubbleSort(A)
heapSort(A)
print A
    
    
