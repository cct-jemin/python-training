#simple list
def simpleList() :
    mylist = ["apple", "banana", "cherry"]
    if "apple" in mylist :
        print("yes apple in this array")
    print(mylist)


#change list item
def changelistItem() :
    mylist = ["apple", "banana", "cherry"]
    mylist2 = ["Strawberry","Mango","Kiwi"]
    mylist[0] = 'watermallon'
    mylist.insert(2,"pinepale") #insert in list
    mylist.append('Avocado') #append in list
    mylist.extend(mylist2) #extend(merge 2 list)
    mylist.remove('Kiwi') #remove
    mylist.pop(1) #remove using index
    del mylist[0] #delete first item
    # del mylist #delete whole list
    # mylist.clear() #clear list
    mylist.sort() #sort assending
    mylist.sort(reverse = True)#sort desending
    mylist2 = mylist.copy() #copy list
    print(mylist)
    print(mylist2)
    
#loop on list
def listLoop() :
    mylists = ["apple", "banana", "cherry"]
    for mylist in mylists :
        print(mylist)
        
#loop on range
def listRangeloop():
    mylists = ["apple", "banana", "cherry"]
    for i in range(len(mylists)) :
        print(mylists[i])
        
#loop with if
def loopWithIf():
    mylists = ["apple", "banana", "cherry"]
    newlist = [mylist for mylist in mylists if "apple" in mylist]
    print(newlist)
    
#nested normal loop
def nestedNormalLoop():
    matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]
   
    mainArray = []
    for i in range(4):
        rowArray = []
        for matrixRow in matrix :
            rowArray.append(matrixRow[i])
        mainArray.append(rowArray)
            
    print(mainArray)
    
#nested optimized loop
def nestedOptimizedLoop():
    matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]
    mainArray = []
    for i in range(4):
        rowArray = [matrixRow[i] for matrixRow in matrix]
        mainArray.append(rowArray)
    print(mainArray)
    

#full optimized loop
def nestedfullOptimizedLoop():
    matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]
    mainArray = [[matrixRow[i] for matrixRow in matrix]for i in range(4)]
    print(mainArray)
    
#normal tuple
def normalTuple():  
    thistuple = ("apple", "banana", "cherry", "apple", "cherry") #allow dupplicate
    print(thistuple)
    
#update value in tuple
def updateTuple():  
    thistuple = ("apple", "banana", "cherry", "apple", "cherry")
    convertList = list(thistuple)
    convertList[3] = 'orange'
    thistuple = tuple(convertList)
    (x,y,z,a,b) = thistuple
    print(x,y,z,a,b)
    
#normal set
def normalSet():
    mySet = {"apple","mango","cherry","apple"} #dupplicate not allow
    newset = [mydataSet for mydataSet in mySet if "apple" != mydataSet]
    print(newset)
    
#normal dictionary
def normalDictionary():
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict['colors'] = "blue"
    dictKey = thisdict.keys()
    dictValue = thisdict.values()
    dict = thisdict.items()
    thisdict.update({"year": 2020})
    print(dictKey)
    print(dictValue)
    print(dict)
    
#nested dictionary
def nestedDictionary():
    myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
    }
    for a,b in myfamily.items() :
        print(a)
        for d in b:
            print(f'{d}:{b[d]}')

# simpleList()
# changelistItem()
# listLoop()
# listRangeloop()
# loopWithIf()
# nestedNormalLoop()
# nestedOptimizedLoop()
# nestedfullOptimizedLoop()
# normalTuple()
# updateTuple()
# normalSet()
# normalDictionary()
nestedDictionary()
