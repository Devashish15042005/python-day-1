def find_num( i,target):
    for num in i:
        if num == target:
          print(f"found{target}!")
          break 
    print(f"checked{num}")
find_num([1,2,3,4,5,6],6)
