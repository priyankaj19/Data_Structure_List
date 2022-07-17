#WAP to sort a list according to the lenth of the elements within the list.

# By bubble sort method

data = ["Priyanka","Prakash","Jinturkar","a","mam","me"]
n = len(data)

for i in range(1,n):
    for j in range(0,n-i):
        if(len(data[j]) > len(data[j+1])):
            data[j],data[j+1]=data[j+1],data[j]
print(data)

# By selection sort method

data = ["Priyanka","Prakash","Jinturkar","a","mam","me"]
n = len(data)
for i in range(0,n):
    min = data[i]
    index = i
    for j in range(i+1,n):
        if(len(min) > len(data[j])):
            min = data[j]
            index = j
    data[i],data[index] = data[index],data[i]
print(data)