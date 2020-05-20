from array import *

arr = array('i',[1,2,3,4,5,6,7,8])
print(arr[2])

for val in arr:
    print(val, end="  ")

print(arr.buffer_info())
arr.insert(0,98)
arr.append(78)
arr.remove(98)
for val in arr:
    print(val, end="  ")
print(arr.index(4))
print(arr.pop(4))

print(arr)

print(arr.pop())