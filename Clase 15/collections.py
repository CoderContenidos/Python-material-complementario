"""
from collections import namedtuple
 
# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB']) #Crea una clase Student
 
# Adding values
S = Student('Nandini', '19', '2541997') #Instancia!
 
# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)


from collections import Counter

# empty Counter
counter = Counter()
print(counter)  # Counter()

# Counter with initial values
counter = Counter(['a', 'a', 'b'])
print(counter)  # Counter({'a': 2, 'b': 1})

counter = Counter(a=2, b=3, c=1)
print(counter)  # Counter({'b': 3, 'a': 2, 'c': 1})



from datetime import datetime

dt = datetime.now()

print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.microsecond)

#########

import math

x = math.sqrt(64.74646)

print(f"Raiz cuadrada:{x}")

"""

########
import random
lista = [1, 2, "Coder", -1, "Nico", 3]
print(random.choice(lista))

#Aleatorios en un rango
print(random.randrange(20, 50))

#Aleatorios en un rango
print(random.randrange(20, 50,7))
