"""
# Binary Search 

> Complexity: `o(log n)`

Note: Will only work to find a single value in a **sorted** array[list]
"""

arr = [1, 4, 5, 10, 10, 13]

inp = int(input("number to find:"))

# Start and end variables to declare
start = 0
end = len(arr) - 1
found = False

while start <= end or found:
    mid = (start + end) // 2

    if arr[mid] == inp:
        print(f"{inp} is to be found on index {mid}")
        found = True
        break
    elif arr[mid] < inp:
        start = mid + 1
    elif arr[mid] > inp:
        end = mid - 1

if found == False:
    print("value not Found!")
