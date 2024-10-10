import moduletest
from moduletest import simpleFunction
import platform


#simple call module
def checkModule():
   checkRecurzive = moduletest.recurzive(10)
   print(checkRecurzive)
   
#import module function
def moduleFunction():
    cllCheck = simpleFunction()
    print(cllCheck)
   
#builtin function
def builtInfunction():
    x = platform.system()
    print(x) 
    y= dir(platform)
    print(y) 
# checkModule()
# moduleFunction()
builtInfunction()