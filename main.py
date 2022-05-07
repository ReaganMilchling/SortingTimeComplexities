from functools import partial
from matplotlib import pyplot
import random
import timeit
import math


def BubbleSort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def InsertionSort(A):
    for j in range(len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = key


def Merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(n1):
        L.append(A[p + i])
    for j in range(n2):
        R.append(A[q + j + 1])
    L.append(math.inf)
    R.append(math.inf)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1


def MergeSort(A, p, r):
    if p < r:
        q = math.floor((p + r) / 2)
        MergeSort(A, p, q)
        MergeSort(A, q + 1, r)
        Merge(A, p, q, r)


def runFunctions():
    num = 1000
    x = []
    y = []
    for i in range(num):
        lst = []
        for i in range(i):
            r = random.randint(1, num)
            lst.append(r)

        timer = timeit.Timer(partial(MergeSort, lst, 0, len(lst) - 1))
        t = timer.timeit(number=1)
        t = t
        x.append(i)
        y.append(t)
    p1 = pyplot.plot(x, y, color='green')

    x = []
    y = []
    for i in range(num):
        lst = []
        for i in range(i):
            r = random.randint(1, num)
            lst.append(r)

        timer = timeit.Timer(partial(InsertionSort, lst))
        t = timer.timeit(number=1)
        t = t
        x.append(i)
        y.append(t)
    p1 = pyplot.plot(x, y, color='red')

    x = []
    y = []
    for i in range(num):
        lst = []
        for i in range(i):
            r = random.randint(1, num)
            lst.append(r)

        timer = timeit.Timer(partial(BubbleSort, lst))
        t = timer.timeit(number=1)
        t = t
        x.append(i)
        y.append(t)
    p1 = pyplot.plot(x, y, color='blue')

    pyplot.xlabel("Iterations")
    pyplot.ylabel("Time(s)")
    pyplot.title("MergeSort (green) vs InsertionSort (red) vs BubbleSort (blue)")
    # pyplot.title("MergeSort (green) vs InsertionSort (red)")
    pyplot.show()




def test(a):
    arr = a.copy()
    print(arr)
    MergeSort(arr, 0, len(arr) - 1)
    print("Merge Sort: ", arr)
    InsertionSort(a)
    print("Insertion sort: ", a)
    print()


if __name__ == '__main__':
    test([15, 12, 17, 22, 99, 6, 7, 5, 4, 3])
    test([10, 9, 8, 7, 6, 5])
    test([54, 3, 99, 1, 2])

    runFunctions()
