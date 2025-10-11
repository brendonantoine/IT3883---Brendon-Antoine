def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


# load data
data = []
with open("p2.txt", 'r') as fin:
    for line in fin:
        data.append(int(line))

print("Unsorted Array")
print(len(data), "items")

size = len(data)
quickSort(data, 0, size - 1)

duplicates = {}

for i in range(0, len(data)):
    if data[i] == data[i+1]:
        if i not in duplicates:
            duplicates[i] = 1
        else:
            duplicates[i] += 1

count_duplicates = 0
for c in duplicates.values():
    count_duplicates += c

print("Found", count_duplicates, "duplicates")
