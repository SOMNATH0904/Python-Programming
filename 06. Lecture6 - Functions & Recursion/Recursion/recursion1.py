def show(n):
    if(n == 0): #Base case
        return
    print(n)
    show(n-1)
    print("END")

show(3)