from typing import Dict, Union, Optional
#Dict[keyType, valueType], .update() method for updating dictionaries
fruits: Dict[str, Union[str,int]] = {"name": "Ali", "age": 18, "city": "Lahore"}
print(list(fruits).index("city")) #fruits.items() will return key with value

squared_numbers = {i: i**2 for i in range(5)}
print(squared_numbers)
def testPrint(text_parameter):
    print(text_parameter)

testPrint("I am Ali")