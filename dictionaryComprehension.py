'''
import random 
countries = ["Col", "Mex", "Bol", "Pe"]

population = {country: random.randint(1,100) for country in countries}
print(population)
'''

names = ["Val", "Jesus", "Nicolas", "Vvalll"]
ages = [18, 17, 17, 19]

dic = {names:ages for (names,ages) in zip(names, ages)}
print(dic)