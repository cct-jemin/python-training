# prctic varible
x = "Hello"
y = "world"


# first function

def firstFunction():
    global x
    x = 'change'
    print(type(x))
    print(x,y)

# string loop
def testLoop(): 
    for i in "banana" :
        print(i)

def stringOperation():
    b = "Hi jemin i am here"
    print(b[2:8])

def listPractic():
    fruits = ["apple","banana","mango"]
    for x in fruits:
        if("apple" in x):
            print(x)

def optimizeLoop():
    fruits = ["apple","banana","mango","cherry"]
    # newlist = [fruit for fruit in fruits if 'c' in fruit]
    newlist = [fruit for fruit in fruits if fruit != 'apple']
    print(newlist)

def toupleExreciess():
    fruits = ("apple","banana","mango","cherry")
    convertList = list(fruits)
    convertList[0] = "pineple"
    fruits = tuple(convertList)
    print(fruits)

def dictionaryExreciess():
    carDetail = {'color':'red','type':'luxery','year':1995}
    print(carDetail.values())
    carDetail['color'] = 'blue'
    carDetail['city'] = 'surat'
    print(carDetail)



dictionaryExreciess()