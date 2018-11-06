list1 = ["hey", "what", "is", "up", "my dude"]
print(list1)

list2 = [2,3,4,5]
list2[0] = 1
list2[1] = 2
list2[2] = 3
list2[3] = 4
print(list2)

list3 = [7,2,6,8,4,1,9,3,5,10]
list3.sort()
print(list3)

list4 = [1,2,3,4]
list5 = [2,3,4,5]
list6 = list4 + list5
print(max(list6))

list7 = [1,2,3,4,5]
for x in list7:
    print(x)

even_nums = []
for x in list7:
    if x % 2 == 0:
        even_nums.append(x)
print(even_nums)