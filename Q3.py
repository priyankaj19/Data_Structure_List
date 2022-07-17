# WAP to sort the list according to second element in sublist.
data = [[11,41,3],[25,35,45],[4,5,7,8],[0,1,15,75]]
#data=[["Priya",7,5,4],["Prakash",9,11],["Jinturkar",5]]
#data=[[51,28],[23,19],[15,32]]
print("Original List:",data)
n=len(data)
for i in range(1,n):
    for j in range(0,n-i):
        if(data[j][1]>data[j+1][1]):
            data[j],data[j+1]=data[j+1],data[j]
print("Sorted List:",data)