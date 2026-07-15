from typing import List, Union, Dict, Tuple



#Tuple of a string
number: Tuple[str,int] = ("Alice,30")
print(number)


#Dictionary with string keys and integer values
score: Dict[str, int] = {"Alice" : 90, "Bob": 85}
print(score)



#Union type foe variablke that can hold multiple types
identifier: Union[int, str] = "ID123" # this contain str and int
identifier = 123 # Also valid
# ------------------------------------------
n : int = 5
name: str = "Sayma"
print(name)



# ------------------------------
def sum(a :int,b :int) -> int:
    return a+b
a = sum(3,5)
print(a)




