#TUPLE (): It's immutable || No Append, Extend, remove. TUPLE it's faster than a LIST
firstTuple = (1, 22, 333) #() no [] - Indexes start 0 || And can use () or not
print(firstTuple[0]) #Use [] for select the index
#INDEX
print(firstTuple.index(1))

#Convert Tuple to List
firstList = list(firstTuple)
print(firstList)

#Convert List to Tuple
secondTuple = tuple(firstList)
print(secondTuple)

#IN - Check if a element exist in the tuple
print(22 in secondTuple)

#COUNT - Count the cuantity of the element is repeated in the tuple
print(secondTuple.count(333))

#LEN - Allow check the long of the tuple || No the quantity of indexes 0,1,2
print(len(secondTuple))

#UNITARY TUPLE - Use a coma
thirdTuple = ("AAA",)
print(len(thirdTuple))

#TUPLE without ()  || TUPLE PACKAGE
fourthTuple = "Felipe", 1986, 1.76, True
print(fourthTuple)

#UNPACKAGE TUPLE - 
fifthTuple = ("Monse", 23, 1.68, True)
name, age, tall, live = fifthTuple #Declare variables without DEF
print (live)
print (name)
print (age)
print (tall)
