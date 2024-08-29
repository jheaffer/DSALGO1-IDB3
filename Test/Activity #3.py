# Bubble Sort Implementation
dataset1 = [23, 89, 7, 56, 44]
print("Original dataset1:", dataset1)
n = len(dataset1)

for i in range(n):
    for j in range(0, n - i - 1):
        if dataset1[j] > dataset1[j + 1]:
            dataset1[j], dataset1[j + 1] = dataset1[j + 1], dataset1[j]

print("Sorted dataset1 (Bubble Sort, Ascending):", dataset1)


# Insertion Sort Implementation
dataset2 = [12, 78, 91, 34, 62]
print("Original dataset2:", dataset2)

for i in range(1, len(dataset2)):
    key = dataset2[i]
    j = i - 1
    while j >= 0 and key < dataset2[j]:
        dataset2[j + 1] = dataset2[j]
        j -= 1
    dataset2[j + 1] = key

print("Sorted dataset2 (Insertion Sort, Ascending):", dataset2)


# Selection Sort Implementation (Descending Order)
dataset3 = [5, 99, 48, 15, 67]
print("Original dataset3:", dataset3)

for i in range(len(dataset3)):
    max_idx = i
    for j in range(i + 1, len(dataset3)):
        if dataset3[j] > dataset3[max_idx]:
            max_idx = j
    dataset3[i], dataset3[max_idx] = dataset3[max_idx], dataset3[i]

print("Sorted dataset3 (Selection Sort, Descending):", dataset3)


# Insertion Sort Implementation (Descending Order)
dataset4 = [38, 82, 25, 74, 13]
print("Original dataset4:", dataset4)

for i in range(1, len(dataset4)):
    key = dataset4[i]
    j = i - 1
    while j >= 0 and key > dataset4[j]:
        dataset4[j + 1] = dataset4[j]
        j -= 1
    dataset4[j + 1] = key

print("Sorted dataset4 (Insertion Sort, Descending):", dataset4)


# Values from the second and third indices of the datasets
dataset1 = [23, 89, 7, 56, 44]
dataset2 = [12, 78, 91, 34, 62]
dataset3 = [5, 99, 48, 15, 67]
dataset4 = [38, 82, 25, 74, 13]

# Extract values from the second and third indices
values_from_indices = [dataset1[2], dataset1[3], dataset2[2], dataset2[3], dataset3[2], dataset3[3], dataset4[2], dataset4[3]]

# Sort in ascending and descending order
sorted_ascending = sorted(values_from_indices)
sorted_descending = sorted(values_from_indices, reverse=True)

print("Values from second and third indices:", values_from_indices)
print("Sorted Ascending:", sorted_ascending)
print("Sorted Descending:", sorted_descending)


# Combine all values from datasets
combined_all = dataset1 + dataset2 + dataset3 + dataset4
print("Original combined_all:", combined_all)

# Selection Sort for Ascending Order
n = len(combined_all)
for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
        if combined_all[j] < combined_all[min_idx]:
            min_idx = j
    combined_all[i], combined_all[min_idx] = combined_all[min_idx], combined_all[i]

print("Sorted combined_all (Selection Sort, Ascending):", combined_all)


# Extract even and odd values from the sorted combined list
evens = [x for x in combined_all if x % 2 == 0]
odds = [x for x in combined_all if x % 2 != 0]

print("Even Values:", evens)
print("Odd Values:", odds)
