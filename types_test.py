def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

#using type
def get_names(firstname:str,lastname:str):
    full_name = firstname.title()+" "+lastname.title()
    return full_name

#check name with age
def getNameWithAge(name:str,age:int):
    nameAge = f"my name is {name} and age is {str(age)}"
    return nameAge

#in list type
def listType(fruites:list[str]):
    copyFruit = []
    for fruite in fruites:
        copyFruit.append(fruite.capitalize())
        
    return copyFruit

#check union
def process_item(item: int | str):
    return item

# print(get_full_name("john", "doe"))
# print(get_names("john", "doe"))
# print(getNameWithAge("john", "doe"))
# print(listType(["apple", "banana", "cherry"]))
print(process_item(19))