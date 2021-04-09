# numar de teste=9
# test 0 n=1000   max=32610
# test 1 n=10000  max=32766
# test 2 n=100000 max=32767
# test 3 n=10000  max=9
# test 4 n=10000  max=32766
# test 5 n=10000  max=32766
# test 6 n=10000  max=10000
# test 7 n=10000  max=10000
# test 8 n=10000  max=12345
# Count sort

def count_sort(v):
    contori = []
    nr_max = max(v)
    for i in range(nr_max + 1):
        contori.append(v.count(i))
    v.clear()
    for i in range(len(contori)):
        while contori[i] != 0:
            contori[i] = contori[i] - 1
            v.append(i)


# Bubble sort
def bubble_sort(v):
    for i in range(len(v)):
        for j in range(len(v) - i - 1):
            if v[j + 1] < v[j]:
                v[j + 1], v[j] = v[j], v[j + 1]


# Radix sort
def count(v, x):
    result = [0] * (len(v))
    count = [0] * 10
    for i in range(0, len(v)):
        index = (v[i] / x)
        count[int(index % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = len(v) - 1
    while i >= 0:
        index = (v[i] / x)
        result[count[int(index % 10)] - 1] = v[i]
        count[int(index % 10)] -= 1
        i -= 1
    i = 0
    for i in range(0, len(v)):
        v[i] = result[i]


def radix_sort(v):
    nr_max = max(v)
    x = 1
    while nr_max / x > 0:
        count(v, x)
        x *= 10


def merge_sort(v):
    if len(v) > 1:
        mijloc = len(v) // 2
        stanga = v[:mijloc]
        dreapta = v[mijloc:]
        merge_sort(stanga)
        merge_sort(dreapta)
        i = j = k = 0
        while i < len(stanga) and j < len(dreapta):
            if stanga[i] < dreapta[j]:
                v[k] = stanga[i]
                i += 1
            else:
                v[k] = dreapta[j]
                j += 1
            k += 1
        while i < len(stanga):
            v[k] = stanga[i]
            i += 1
            k += 1
        while j < len(dreapta):
            v[k] = dreapta[j]
            j += 1
            k += 1


# Quick sort
def quick_sort(v, stanga, dreapta):
    if stanga < dreapta:
        m = (stanga + dreapta) // 2
        aux = v[stanga]
        v[stanga] = v[m]
        v[m] = aux
        i = stanga
        j = dreapta
        d = 0
        while i < j:
            if v[i] > v[j]:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
                d = 1 - d
            i += d
            j -= 1 - d
        quick_sort(v, stanga, i - 1)
        quick_sort(v, i + 1, dreapta)


import time

# Test 0

print("Test 0:")
f = open("test_0", 'r')
s = f.read()
sir = s.split("\n")
vector = []
for i in sir:
    vector.append(int(i))
v = vector
start = time.time()
bubble_sort(v)
stop = time.time()
print("Durata bubble sort: ", stop - start)
v = vector
start = time.time()
count_sort(v)
stop = time.time()
print("Durata count sort: ", stop - start)
v = vector
start = time.time()
radix_sort(v)
stop = time.time()
print("Durata radix sort: ", stop - start)
v = vector
start = time.time()
merge_sort(v)
stop = time.time()
print("Durata merge sort: ", stop - start)
v = vector
start = time.time()
quick_sort(v, 0, len(v) - 1)
stop = time.time()
print("Durata quick sort: ", stop - start)

# Test 1

print("Test 1:")
f = open("test_1", 'r')
s = f.read()
sir = s.split("\n")
vector = []
for i in sir:
    vector.append(int(i))
v = vector
start = time.time()
bubble_sort(v)
stop = time.time()
print("Durata bubble sort: ", stop - start)
v = vector
start = time.time()
count_sort(v)
stop = time.time()
print("Durata count sort: ", stop - start)
v = vector
start = time.time()
radix_sort(v)
stop = time.time()
print("Durata radix sort: ", stop - start)
v = vector
start = time.time()
merge_sort(v, )
stop = time.time()
print("Durata merge sort: ", stop - start)
v = vector
start = time.time()
quick_sort(v, 0, len(v) - 1)
stop = time.time()
print("Durata quick sort: ", stop - start)

# Test 2

print("Test 2:")
f = open("test_2", 'r')
s = f.read()
sir = s.split("\n")
vector = []
for i in sir:
    vector.append(int(i))
v = vector
start = time.time()
# bubble_sort(v)
stop = time.time()
print("Durata bubble sort: >1min")
v = vector
start = time.time()
count_sort(v)
stop = time.time()
print("Durata count sort: ", stop - start)
v = vector
start = time.time()
radix_sort(v)
stop = time.time()
print("Durata radix sort: ", stop - start)
v = vector
start = time.time()
merge_sort(v)
stop = time.time()
print("Durata merge sort: ", stop - start)
v = vector
start = time.time()
quick_sort(v, 0, len(v) - 1)
stop = time.time()
print("Durata quick sort: ", stop - start)

# Test 3

print("Test 3:")
f = open("test_3", 'r')
s = f.read()
sir = s.split("\n")
vector = []
for i in sir:
    vector.append(int(i))
v = vector
start = time.time()
bubble_sort(v)
stop = time.time()
print("Durata bubble sort: ", stop - start)
v = vector
start = time.time()
count_sort(v)
stop = time.time()
print("Durata count sort: ", stop - start)
v = vector
start = time.time()
radix_sort(v)
stop = time.time()
print("Durata radix sort: ", stop - start)
v = vector
start = time.time()
merge_sort(v)
stop = time.time()
print("Durata merge sort: ", stop - start)
v = vector
start = time.time()
# quick_sort(v, 0, len(v) - 1)
stop = time.time()
print("Durata quick sort: maximum recursion depth exceeded in comparison")

# Test 4

print("Test 4:")
f = open("test_4", 'r')
s = f.read()
sir = s.split("\n")
vector = []
for i in sir:
    vector.append(int(i))
v = vector
start = time.time()
bubble_sort(v)
stop = time.time()
print("Durata bubble sort: ", stop - start)
v = vector
start = time.time()
count_sort(v)
stop = time.time()
print("Durata count sort: ", stop - start)
v = vector
start = time.time()
radix_sort(v)
stop = time.time()
print("Durata radix sort: ", stop - start)
v = vector
start = time.time()
merge_sort(v)
stop = time.time()
print("Durata merge sort: ", stop - start)
v = vector
start = time.time()
quick_sort(v, 0, len(v) - 1)
stop = time.time()
print("Durata quick sort: ", stop - start)

# Test 5

print("Test 5:")
f = open("test_5", 'r')
s = f.read()
sir = s.split("\n")
vector = []
for i in sir:
    vector.append(int(i))
v = vector
start = time.time()
bubble_sort(v)
stop = time.time()
print("Durata bubble sort: ", stop - start)
v = vector
start = time.time()
count_sort(v)
stop = time.time()
print("Durata count sort: ", stop - start)
v = vector
start = time.time()
radix_sort(v)
stop = time.time()
print("Durata radix sort: ", stop - start)
v = vector
start = time.time()
merge_sort(v)
stop = time.time()
print("Durata merge sort: ", stop - start)
v = vector
start = time.time()
quick_sort(v, 0, len(v) - 1)
stop = time.time()
print("Durata quick sort: ", stop - start)

# Test 6

print("Test 6:")
f = open("test_6", 'r')
s = f.read()
sir = s.split("\n")
vector = []
for i in sir:
    vector.append(int(i))
v = vector
start = time.time()
bubble_sort(v)
stop = time.time()
print("Durata bubble sort: ", stop - start)
v = vector
start = time.time()
count_sort(v)
stop = time.time()
print("Durata count sort: ", stop - start)
v = vector
start = time.time()
radix_sort(v)
stop = time.time()
print("Durata radix sort: ", stop - start)
v = vector
start = time.time()
merge_sort(v)
stop = time.time()
print("Durata merge sort: ", stop - start)
v = vector
start = time.time()
quick_sort(v, 0, len(v) - 1)
stop = time.time()
print("Durata quick sort: ", stop - start)

# Test 7

print("Test 7:")
f = open("test_7", 'r')
s = f.read()
sir = s.split("\n")
vector = []
for i in sir:
    vector.append(int(i))
v = vector
start = time.time()
bubble_sort(v)
stop = time.time()
print("Durata bubble sort: ", stop - start)
v = vector
start = time.time()
count_sort(v)
stop = time.time()
print("Durata count sort: ", stop - start)
v = vector
start = time.time()
radix_sort(v)
stop = time.time()
print("Durata radix sort: ", stop - start)
v = vector
start = time.time()
merge_sort(v)
stop = time.time()
print("Durata merge sort: ", stop - start)
v = vector
start = time.time()
quick_sort(v, 0, len(v) - 1)
stop = time.time()
print("Durata quick sort: ", stop - start)

# Test 8

print("Test 8:")
f = open("test_8", 'r')
s = f.read()
sir = s.split("\n")
vector = []
for i in sir:
    vector.append(int(i))
v = vector
start = time.time()
bubble_sort(v)
stop = time.time()
print("Durata bubble sort: ", stop - start)
v = vector
start = time.time()
count_sort(v)
stop = time.time()
print("Durata count sort: ", stop - start)
v = vector
start = time.time()
radix_sort(v)
stop = time.time()
print("Durata radix sort: ", stop - start)
v = vector
start = time.time()
merge_sort(v)
stop = time.time()
print("Durata merge sort: ", stop - start)
v = vector
start = time.time()
# quick_sort(v, 0, len(v) - 1)
stop = time.time()
print("Durata quick sort: maximum recursion depth exceeded in comparison")