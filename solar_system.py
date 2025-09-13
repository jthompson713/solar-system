from math import pi 
from random import choice as ch

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)
r = 0

if random_planet == planets[0]:
  r = 2440
elif random_planet == planets[1]:
  r = 6052
elif random_planet == planets[2]:
  r = 6371
elif random_planet == planets[3]:
  r = 3390
elif random_planet == planets[4]:
  r = 58232
else:
  print('Oops! An error occurred.')

area = (4 * pi * (r ** 2))

print(f'The surface area of {random_planet} is {area:,.2f} square kilometers')
