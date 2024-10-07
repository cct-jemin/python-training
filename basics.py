"""
This is a file
for basic demo
of python
"""
#syntax test
def syntax():
    print("First python program")
    if 5 > 2 :
        print('5 is greater then 2')

#variable test
def variable():
    global testVar 
    myvariable = 'basics demo'
    _myvariable = 'basics demo'
    my_variable = 'basics demo'
    myvariable_ = 'basics demo'
    myVariable = 'basics demo'      
    myVariable2 = 'basics demo'

    outputVariable = "this is output"
    a = "this"
    b = "is"
    c = "test"
    
    testVar = "global variable"
    
    print(myvariable)
    print(_myvariable)
    print(my_variable)
    print(myvariable_)
    print(myVariable)
    print(myVariable2)
    print(outputVariable)
    print(a,b,c)
    print(a+b+c)
    
#Some built in functions
def builtInFunctions():
    print("this is print function") #print
    checkString = 'length of string test'
    testInteger = '10'
    testArray = [1,2,3,4,5]
    name = input("Enter your name: ") #input
    nagative = -5
    roundoff = 5.6
    
    print(len(checkString)) #len 
    print(type(checkString)) #type
    print(int(testInteger)) #int
    print(str(testInteger)) #str
    print(float(testInteger)) #float
    print(sum(testArray)) #float
    print(max(testArray)) #max
    print(min(testArray)) #min
    print(f"Hello:{name}") #input
    print(sorted(testArray)) #sort
    print(abs(nagative)) #sort
    print(round(roundoff)) #sort
    print(isinstance(nagative,int)) #isinstance check type



builtInFunctions()
# print(testVar)