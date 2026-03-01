# Read input from file
with open("input2.txt", "r") as f:
    n = int(f.readline().strip())          # Read number of elements
    arr = list(map(int, f.readline().split()))  # Read array
    target = int(f.readline().strip())     # Read target value


# Binary Search Function
def binary_search(arr, target):#we have ued the binary search and we have kept arr and target a parameter 
    low = 0# we have to put the intial value a 0 so it starts from zero
    high = len(arr) - 1 #we check if the highest value i in the target

    while low <= high: #first we check if low is smaller or equal to high by while loop
        mid = (low + high) // 2
        #here we take the avrage of both low + high 

        if arr[mid] == target:#if else condition to check if the value is equal to the mid value
            return mid
        elif arr[mid] < target:#here we check that the mid value is less than the target if it is we add 1 in the mid value
            low = mid + 1
        else:
            high = mid - 1#here we substract 1 from the mid value to if the mid value is greater than the target

    return -1#here we return -1 as per the question when the integer index is found


# Perform search
result = binary_search(arr, target)#here we search for the target value and tore t in the result

# Write output to file
with open("output2.txt", "w") as f:
    f.write(str(result))

print("Result:", result)