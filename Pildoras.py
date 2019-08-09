my_name = "Felipe López"
first = 10
second = 50

print (type(my_name))
print (type(first))
print (type(second))

if first < second:
    print("First is lower, only has ")
    a = 0
    for i in range (first):
        a+=1
        print(a)
elif first > second:
    print("First is higher")
else:
    print("First is like Second")