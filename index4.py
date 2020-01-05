
inp = int(input("enter  a number"))
lst = []
for i in range(1,inp + 1):
    if(i == inp):
        print(inp**i)
    else:
        print(inp**i, end="+")
    lst.append(inp**i)
print("\n")
print(sum(lst))
