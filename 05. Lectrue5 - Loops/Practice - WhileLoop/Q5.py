# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int(input("Enter a number to Search :"))
i = 0
while(i < len(nums)):
    if(nums[i] == x):
        print(x,"is present in the tuple at index",i)
        break
    else:
        print("Finding ...")
    i += 1