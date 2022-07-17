# WAP to merge two lists and sort it.
# without using inbuild function.

l1 = [12,5,34,98,346,44]
l2 = [76,3,56,90,32,39,47]
l1 += l2
print("Merged list: ",l1)
n = len(l1)
# print("length: ",n)
for i in range(0,n):
    min = l1[i]
    index = i
    for j in range(i+1,n):
        if (min > l1[j]):
            min = l1[j]
            index = j
    l1[i],l1[index] = l1[index],l1[i]
print("Sorted list: ",l1)

# OR

l1=[1,2,20,56,13,3,4,5]
l2=[10,34,45,20,30,40,50]
l3=[]
x=len(l1)
l3[0:x]=l1
l3[x:]=l2
print("original List: ",l3)
n=len(l3)
for j in range(0,n):
    min=l3[j]
    index=j
    for i in range(j+1,n):
        if(min>l3[i]):
            min=l3[i]
            index=i
    l3[j],l3[index]=l3[index],l3[j]
print("Sorted list: ",l3)

# with using inbuild function

l1 = [12,5,34,98,346,44]
l2 = [76,3,56,90,32,39,47]
for x in l2:
    l1.append(x)
print("Merged List: ",l1)
l1.sort()
print("Sorted List: ",l1)