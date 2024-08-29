myArray = [24, 16, 71, 78, 90]
print("This is the initial order of the array")
print(myArray)
n = len(myArray)

for i in range(n):
    for j in range(0, n - 1 - 1):
        if (myArray[j] > myArray[j + 1]):
            myArray[j], myArray[j + 1] = myArray[j + 1], myArray[j]
print(myArray)

myArray1 = [24, 16, 71, 78, 90]
print("I am printing the unsorted array: ")
print(myArray1)
for i in range(len(myArray1)):
    min_idx = 1
    for j in range(i + 1, len(myArray1)):
        if myArray1[min_idx] > myArray1[j]:
            min_idx = j
            myArray1[i], myArray1[min_idx] = myArray1[min_idx], myArray1[i]
print(myArray1)

myArray2 = [24, 16, 71, 78,90]
print("I am printing the unsorted array: ")
print(myArray2)
for i in range(1, len(myArray2)):
    key = myArray2[i]
    j = i - 1
    while j >= 0 and key < myArray2[j]:
        myArray2[j + 1] = myArray2[j]
        j-=1
        myArray2[j + 1] = key
print("The sorted array using the Insertion Sort: ")
print(myArray2)