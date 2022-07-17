# WAP to find the Second Largest Number in a list using Bubble Sort.

data = [7,5,4,3,6,9,2,1]
n = len(data)

for i in range(1,n):
    for j in range(0,n-i):
        if(data[j] > data[j+1]):
            data[j],data[j+1]=data[j+1],data[j]
    
print("Second Largest Number: ",data[-2])

# OR 

data = [7,5,4,3,6,9,2,1]
n = len(data)
#l = int(input("Enter which largest no. you want: "))
k=1
for j in range(1,n):
    for i in range(0,n-j):
        if(data[i] > data[i+1]):
            data[i], data[i+1] = data[i+1], data[i]
    #if(k==l):      #condition for n th largest number
    if(k==2):
        print("Second Largest Number: ",data[i+1])
        break
    k += 1
