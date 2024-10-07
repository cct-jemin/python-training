#Basic if else
def basicIf(a,b):
    if a > b :
        print("a is greater then b")
    elif a < b:
        print("b is greater then a")
    else :
        print("a and b are equal")
        
#One liner if else
def oneLineIf(a,b):
   print("a") if a > b else print("b") if a < b else print("=")
   
#if with and and or
def withAnd(a,b,c):
    if a > b and b > c :
        print("both conditin are true")
    elif a > b or b > c :
        print("any one condition are equal")
    else:
        print("all condton are false")
        
#if with pass
def withPass(a,b):
    if a > b :
        pass
# having an empty if statement like this, would raise an error without the pass statement

    
#dynamic practic if
def ifPractis():
    a = int(input("Enter an integer:"))
    if a < 0 :
        print("enter number is nagative")
    elif a == 0 :
        print("enter number is 0")
    elif a == 1 :
        print("enter number is 1")
    else:
        print("enter number is more")
        
        
#while loop
def whileDemo(num):
    if num > 0 :
        i = 0
        while(i < num) :
            print(i)
            i += 1
    else:
        print("added number is nagative")
        
#while with break
def whileWithBreakDemo(num):
    if num > 0 :
        i = 0
        while(i < num) :
            print(i)
            if i == 3:
                break 
            i += 1
    else:
        print("added number is nagative")
        
#while with continue
def whileWithContinueDemo(num):
    if num > 0 :
        i = 0
        while(i < num) :
            i += 1
            if i == 3:
                continue 
            print(i)
            
    else:
        print("added number is nagative")
        
#for loop
def forloopdemo():
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits :
        print(fruit)
        
#for loop with break
def forloopBreakdemo():
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits :
        # print(fruit)
        if(fruit == "banana") :
            break
        print(fruit)

#for loop with continue       
def forloopContinuedemo():
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits :
        # print(fruit)
        if(fruit == "banana") :
            continue
        print(fruit)
        
#for loop with range       
def forloopRange():
    for i in range(2,20) :
        print(i)
        
# range in loop       
def rangeLoop():
    fruits = ["apple", "banana", "cherry"]
    for fruit in range(len(fruits)) :
        print(fruits[fruit])
       
#for loop with dictionary
def forwithDictionary():
    users = {'jems': 'active', 'jemin': 'inactive', 'sweta': 'active'}
    for user, status in users.copy().items():
        if(status == 'inactive') :
            del users[user]
        
    print(users)    
    
#create new collection
def createCollection() : 
    users = {'jems': 'active', 'jemin': 'inactive', 'sweta': 'active'}
    active_users = {}
    for user, status in users.items():
        if status == 'inactive':
            active_users[user] = status
                
    print(active_users)
    
#get error for matche
def getError():
    error = errorCase(400)
    print(error)
    
#matchDomo
def errorCase(code):
    print(code)
    match code :
        case 400:
            return "bad requet"
        case 404:
            return "not found"
        case 418 :
            return "i am teapost"
        case _:
            return "something went wrong"
        
        
# basicIf(50,50)
# oneLineIf(100,50)
# withAnd(2,1,5)
# withPass(100,50)
# ifPractis()
# whileDemo(5)
# whileWithBreakDemo(5)
# whileWithContinueDemo(5)
# forloopdemo()
# forloopBreakdemo()
# forloopContinuedemo()
# forloopRange()
# forwithDictionary()
# createCollection()
# getError ()
rangeLoop()
