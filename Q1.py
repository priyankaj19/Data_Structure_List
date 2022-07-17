# WAP to put Even and Odd elements of a list into Two Different List.
# without using inbuild function

list = [56,23,45,78,90,13,22,56,33,79]
print("Given List",list)
odd_list = []
even_list = []
for x in list:
    if(x%2 == 0):
        even_list += [x]
    else:
        odd_list += [x]
print("Even elements List: ",even_list)
print("Odd elements List: ",odd_list)

# With using inbuild function

list = [56,23,45,78,90,13,22,56,33,79]
print("Given List",list)
odd_list = []
even_list = []
for x in list:
    if(x%2 == 0):
        even_list.append(x)
    else:
        odd_list.append(x)
print("Even elements List: ",even_list)
print("Odd elements List: ",odd_list)