# WAP to find the intersection of two lists.
# without using buildin function

list1 = [12,45,34,89,63,56,78,33]
list2 = [65,89,88,45,33,69,12,90]
l3 = []
for i in list1:
    if (i in list2):
        l3 += [i]
print("Intersection of list1 and list2: ",l3)

# intersection function

def intersection(l1,l2):
    l3=[value for value in l1 if value in l2]
    return l3

l1=[11,23,35,14,57,36]
l2=[1,36,5,11,29,57,8]
print("Intersection of l1 and l2",intersection(l1,l2))