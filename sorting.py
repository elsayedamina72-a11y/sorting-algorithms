books = [
    {"title": "Clean Code", "year": 2008},
    {"title": "The Pragmatic Programmer", "year": 1999},
    {"title": "Python Crash Course", "year": 2015},
    {"title": "Design Patterns", "year": 1994},
    {"title": "Introduction to Algorithms", "year": 2009},
]

# ---------- Insertion Sort ----------
def insertion_sort(arr, key):
    arr = arr.copy()
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and arr[j][key] > current[key]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current
    return arr

# ---------- Merge Sort (Divide & Conquer) ----------
def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)    
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)      

def merge(left, right, key):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# ---------- ----------
print("Insertion Sort (by year):")
for b in insertion_sort(books, "year"):
    print(b["year"], "-", b["title"])

print("\nMerge Sort (by title):")
for b in merge_sort(books, "title"):
    print(b["title"], "-", b["year"])
def quick_sort(arr, key):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left   = [x for x in arr if x[key] < pivot[key]]
    middle = [x for x in arr if x[key] == pivot[key]]
    right  = [x for x in arr if x[key] > pivot[key]]
    return quick_sort(left, key) + middle + quick_sort(right, key)

# ---------- ----------
print("Quick Sort (by year):")
for b in quick_sort(books, "year"):
    print(b["year"], "-", b["title"])
