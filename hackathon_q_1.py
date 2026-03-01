# Read input from file
with open("input.txt", "r") as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split(',')))  
    k = int(f.readline())

# Sort the array
arr.sort()

# k-th smallest element
result = arr[k-1]

# Write output
with open("output.txt", "w") as f:
    f.write(str(result))