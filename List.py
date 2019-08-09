# LIST []
nameList = ["Mary","Celeste","Claudia", "Miriam","Tatiana","Alejandra"]

print (nameList[:]) #Shows all indexes
print (nameList[-0]) #Shows the first position 
print (nameList[5]) #Shows the position 10 
print (nameList[-1]) #Shows the first position from end to begin 

print (nameList[0:4]) #Shows/Extracts from the index 0 to 3
print (nameList[:4]) #Shows/Extracts from the index 0 to 3 without use 0
print (nameList[4:]) #Shows/Extracts from the index 4 to the end without use 0
print (nameList[0:1]) #Only shows/Extracts the index 0

#EXTEND - Join a new list in other
nameList.extend(["María","Paulina", "Citlalli","Monserrat"]) 
print (nameList)

#APPEND - To ADD a new element at the end
nameList.append("NeitherRemember") 

#INSERT - To ADD a new element in the index 
nameList.insert(0,"IDontKnow") 
print (nameList)

#INDEX - Shows the index of the element found
print(nameList.index("María")) 

#Search the element in the list and displays if it's true or false
print("Tatiana" in nameList) 
print("Sandra" in nameList)

#REMOVE - Search and remove the element
nameList.remove("NeitherRemember") 
print(nameList[:])

#POP - Remove the last element
nameList.pop() 
print(nameList[:])

# +,* JOIN and REPEAT lists
newList = ["Text", True, 12345, 999.88]
thirdList = ["AAA", "BBB", "CCC"] * 3 #* Allow repeat the list
fourthList = newList + thirdList #+ Joins the lists
print(fourthList[:])

