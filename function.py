#simple function call
def simpleFunction():
    print("hello simple function call")
    
#simeple function with argument
def simpleFunctionArg(name):
    print(f"my name is {name}")
    
#arbitary arguments
def arbitaryArg(*name):
    print(name[1])
    
#keyword argument
def keyWordArg(child1,child2):
    print(child1)
    
#arbitary keywords
def arbtaryKeywords(**name):
    print(f"my name is {name['fname']} {name['lname']}")
    
#default parameter
def defaultParameter(city='surat'):
    print(city)
    
#positinaol only aregument
def positionalOnly(name,/):
    print(name)
    
#keyword only aregument
def keyWordOnly(*,name):
    print(name)
    
#combine positional and keyword only
def combineFunction(name1,name2,/,*,age1,age2):
    print(name1)
    print(name2)
    print(age1)
    print(age2)
    
#recursiv function
def recurzive(num):
    if num > 0 :
        result = num + recurzive(num-1)
        print(result)
    else :
        result = 0
        
    return result

#combine arbitary argument and arbitary keyword dynamic
def demoFunction(name,*address,**longaddress):
    print(f"my name is {name}")
    for addr in address :
        print(addr)
        
    for addr in longaddress :
        print(f'{addr} :- {longaddress[addr]}')

    
# simpleFunction()
# simpleFunctionArg('ravi')
# arbitaryArg('jems','ravi')
# keyWordArg(child2='ravi',child1='sweta')
# arbtaryKeywords(fname='jemin',lname='shah')
# defaultParameter() 
# positionalOnly('jemin')
# keyWordOnly(name='jemin')
# combineFunction('jemin','ravi',age1 = 29,age2 = 32)
# recurzive(6)
demoFunction('jemin','adajan gam surat','new address surat','office address surat',full='16 adajangam surat',short='ffff')
