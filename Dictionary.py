#DICTIONARY {}: Data structure Like Tuple or List
#It's possible save elements,list or tuples in a dictionary
firstDictionary = {"Germany":"Berlin", "France":"Paris", "England":"London", "Spain":"Madrid"}

#To print a value, It's necessary say its KEY
print(firstDictionary)
print(firstDictionary["England"])

#ADD element
firstDictionary["México"]="León"
print(firstDictionary)

#MODIFY element value
firstDictionary["México"]="Ciudad de México"
print(firstDictionary)

#DELETE element
del firstDictionary["France"]
print(firstDictionary)

secondDictionary = {"Team":"Chicago Bulls", 1:"23", 23:"Michael Jordan"}
print(secondDictionary)

#TUPLE for use as KEY and asign VALUES in a DICTIONARY
languageTuple = ["México", "France", "Brazil", "Italy"]
languageDictionary = {languageTuple[0]:"Spanish", languageTuple[1]:"French", languageTuple[2]:"Portuguese", languageTuple[3]:"Italian"}
print(languageDictionary)
print(languageDictionary["Brazil"])

#
alumnDictionary = {1:"Aguirre", 2:"Biurcos", 3:"Cazares", 4:"Durazo", "Group":{"year":["1st F", "2nd F", "3th F"]}}
print(alumnDictionary["Group"])
print[alumnDictionary.keys()]