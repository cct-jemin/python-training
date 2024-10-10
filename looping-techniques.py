import math
#technique for list
def listTech():
    myLists = ['tic', 'tac', 'toe']
    for myList,val in enumerate(myLists):
        print(myList,val)
        
#technique for pair 2 array
def listArrayPair():
    questions = ['name', 'age', 'color']
    answere = ['jemin','18','black']
    for q,a in zip(questions,answere):
        print('What is your {0}?  It is {1}.'.format(q, a))

#reverse loop
def reverseRange():
    for i in reversed(range(1,10,2)) :
        print(i)
        
#filter list
def filterList():
    rawData = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    filterData = []
    for row in rawData:
        if not math.isnan(row) :
            filterData.append(row)
            
    print(filterData)
# listTech()
# listArrayPair()
# reverseRange()
filterList()