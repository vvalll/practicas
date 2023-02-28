'''
import random 
countries = ["Col", "Mex", "Bol", "Pe"]

population = {country: random.randint(1,100) for country in countries}
print(population)
'''

# ---- 

'''
names = ["Val", "Jesus", "Nicolas", "Vvalll"]
ages = [18, 17, 17, 19]

dic = {names:ages for (names,ages) in zip(names, ages)}
print(dic)
'''

# ----
''' 
dias =["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
temp = [30.5,32.6,31.8,33.4,29.8,30.2,29.9]

dic = {dias:temp for (dias,temp) in zip(dias,temp)}
print(dic)
'''

#----------
text = "Hola, soy Vall"
unique = {v: v.upper() for v in text if v in "aeiou"}
print(unique)
