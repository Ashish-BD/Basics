a_set = {1,2,3,4,1}
#print(a_set)
#print(type(a_set))

#a_set.add(5)

#print(a_set)

#a_set.update((2,8,9),{89,34})

#print(a_set.pop())

#print(a_set)

#l = sorted(a_set)
#print(type(l))
#l.reverse()
#print(l)
#V = set(l)
#print(type(V))

set_1 = {1,2,3,4}
set_2 = {6,7,8,9,1}

#set1_unionset2 = set_1.union(set_2)
#set2Unionset1 = set_2.union(set_1)

#print(set1_unionset2)
#print(set2Unionset1)
#print(set_1)

#setInitersec = set_1.intersection(set_2)
#print(setInitersec)


#setdiff = set_1.difference(set_2)
#print(setdiff)

#print(set_1)

setdiff = set_1.difference(set_2)
print(setdiff)

setdiff = set_1.difference_update(set_2)
print(setdiff)

print(set_1)