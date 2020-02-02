# Function recap

def add(a, b):
    return a+b

result1 = add(23, 45) 
result2 = add(11, 22)
print(result1, result2)


def add2(a, b=0):
    return a+b
    """ a and b is an int, b has default value 0"""


result3 = add2(12)
print(result3)
print(add(40, 50))
def car_description(model, year, features):
    """ model: str, year : int, features ; list This function describe the car base on input""" 
    print(f"The car's model is {model}.")
    print(f"It was manufactured in {year}.")
    print(f"It has folowing features: ")
    for feature in features:
        print(f"\t{feature.title()}.")

car_description("Model Y", 2019, ['cool design', 'fancy doors', 'techy tires', 'ugly windows'])

car_tesla = {'model': ['Model X', 'Model Y'], 
             'year': [2020, 2019], 
            'owner': ['Zakaria', 'Oleh']}
def cars_description(car):
    for field, values in car.items():
        for value in values:
            print(f"Your car's {field} is {value}.")


cars = []
cars_description(car_tesla)


