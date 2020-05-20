num1 =10

if (num1 > 20):
    print("num1 > 20")
elif(num1 == 20):
    print("num1 > 20")
else:
    print("num1 < 20")


count =0

while count < 10:
    print("count", count)
    count += 1
else:
    print("count must be grater that or equal to 10 value:", count)

a_string = "This is python"
for char in a_string:  #char is variable
    print(char)


for i in range(1,20, 2):
   print(i)


for num in range(10,-1,-2):
    print(num)


for num in range(10,5):
    print(num)

a_list = [1,2,3,4]
print(a_list)
print(len(a_list))
print([1,2,3] + [4,5,6])
#print([Hi]*4)

print(max([1,2,3,4]))
#print(max(['A',1,2,3]))
print(1 in a_list)

a_string = "Python"
print(a_string)
print(list(a_string))

print(a_list.append(110))
print(a_list.count(1))
print(a_list.index(2))

b_list = [12,13,14]
#a_list.append(b_list)
for a in b_list:
    print( a_list.append(a))
    print(a_list)

print(a_list.extend(b_list) )
print(a_list)