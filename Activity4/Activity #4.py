# 1. Create a list with squares of even numbers from 1 to 20
ev_sqr = []
for n in range(1, 20):
    if n % 2 == 0:
        ev_sqr.append(n**2)
print("Squares of even numbers:", ev_sqr)

# 2. Linear Search
search_vals = [8**2, 4**2, 2**2, 25, 144]  # Added values both present (64, 16) and not present (25, 144)
for t in search_vals:
    idx = -1
    for i in range(len(ev_sqr)):
        if ev_sqr[i] == t:
            idx = i
            break
    result = 'The Data is Present' if idx != -1 else 'The Data is Not Present'
    print(f"Linear search for {t}: {result}")

# 3. Append odd numbers
for n in range(1, 21):
    if n % 2 != 0:
        ev_sqr.append(n)
print("List after appending odd numbers:", ev_sqr)

# 4. Sort using selection sort
for s in range(len(ev_sqr)):
    min_idx = s
    for c in range(s + 1, len(ev_sqr)):
        if ev_sqr[c] < ev_sqr[min_idx]:
            min_idx = c
    ev_sqr[s], ev_sqr[min_idx] = ev_sqr[min_idx], ev_sqr[s]
print("List after selection sort:", ev_sqr)

# 5. Binary Search Returning True or False
search_vals_bin = [3, 17, 19, 21, 64, 144]  # Added values both present (64) and not present (144)
ev_sqr.sort()  # Ensure the list is sorted before binary search
for t in search_vals_bin:
    lo = 0
    hi = len(ev_sqr) - 1
    found = False
    while lo <= hi:
        mid = (lo + hi) // 2
        if ev_sqr[mid] == t:
            found = True
            break
        elif ev_sqr[mid] < t:
            lo = mid + 1
        else:
            hi = mid - 1
    print(f"Binary search for {t}: {'TRUE' if found else 'FALSE'}")

# 6. Sort the first half using insertion sort in descending order
half_idx = len(ev_sqr) // 2
first_half = ev_sqr[:half_idx]

for i in range(1, len(first_half)):
    key = first_half[i]
    j = i - 1
    while j >= 0 and first_half[j] < key:
        first_half[j + 1] = first_half[j]
        j -= 1
    first_half[j + 1] = key

print("First half sorted in descending order:", first_half)

# 7. Sort the second half using shell sort in descending order
second_half = ev_sqr[half_idx:]
n = len(second_half)
g = n // 2

while g > 0:
    for i in range(g, n):
        temp = second_half[i]
        j = i
        while j >= g and second_half[j - g] < temp:
            second_half[j] = second_half[j - g]
            j -= g
        second_half[j] = temp
    g //= 2

print("Second half sorted in descending order:", second_half)
