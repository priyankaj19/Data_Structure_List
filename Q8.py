# WAP to print 1 to 100 in snakes and ladder pattern.

# without using inbuild function
for i in range(10,0,-1):
    x = i*10
    data = []
    for j in range(0,10):
        data += [x-j]
    if(i%2 != 0):
        data = data[::-1]
    # print(data)
    for y in data:
        print(y,end=" ")
    print()

# with using inbuild function
for i in range(10,0,-1):
    x = i*10
    data = []
    for j in range(0,10):
        data.append(x-j)
    if(i%2 != 0):
        data.reverse()
    # print(data)
    for y in data:
        print(y,end=" ")
    print()