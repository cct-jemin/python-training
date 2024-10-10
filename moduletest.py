def simpleFunction():
    check = "hello simple function call"
    return check
    
    
#recursiv function
def recurzive(num):
    if num > 0 :
        result = num + recurzive(num-1)
        print(result)
    else :
        result = 0
        
    return result