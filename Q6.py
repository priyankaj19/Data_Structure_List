# WAP to find the Union of two Lists.

#l1 = [12,34,26,58,9,45,76]
#l2 = [98,9,67,45,89,52,34]
l1 = ['A6','M3','Viper','Charger','Seena','Supra','Stingray']
l2 = ['M3','Supra','Hurican','MachE','Phantom','Gwagan']
l3 = []

for i in l1:
    if(i not in l2):
        l3 += [i]
l3 += l2
print(l3)

# OR
l1 = ['A6','M3','Viper','Charger','Seena','Supra','Stingray']
l2 = ['M3','Supra','Hurican','MachE','Phantom','Gwagan']
l3 = []

for i in l1+l2:
    if(i not in l3):
        l3 += [i]
print(l3)

# Using inbuild function

l1 = [12,34,26,58,9,45,76]
l2 = [98,9,67,45,89,52,34]
l3 = []
l1.extend(l2)
l3 = list(set(l1))
print(l3)