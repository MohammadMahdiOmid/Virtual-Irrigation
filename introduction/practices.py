import keyword
import sys
import decimal
import fractions
import numpy

# key words in python
print(keyword.iskeyword('break'))

# all of key words in python
help('keywords')

# maximum integer in python
print(sys.maxsize)

p = 10
# type of variable
print(type(p))

# e=10 power anythings
print(3e2)

# exchange
a = 10
print(float(a))

# complex = real part+ imaginary part
n = 3 + 4j
print(n, type(n))

# complex
print(complex(10, 25))

# decimal
i = 0.1 + 0.1 + 0.1
print(i)
print(decimal.Decimal(i))

# fraction
a = 1
b = 2
f = fractions.Fraction(a, b)
print(f)
print(fractions.Fraction('0.3'))

# Boolean
a = True
print(a)
print('\n', int(a), '\n', float(a), '\n', int(True), '\n', float(False))

# continue
number = 0
while number <= 20:
    number += 1
    if number % 2 != 0:
        continue
    print(number)

# break
count = 0
while count < 100:
    if count == 10:
        break
    print(count)
    count += 1

# for

for i in [1, 2, 3, 5]:
    print(i)
for char in 'mahdi omid':
    print(char)
# dictionary
landsat = {'numberOfBand:': 10, 'country:': 'USA', 'spatialResolution:': 20}
for val, key in landsat.items():
    print(val, key)


landsat['mahdi:']=20
print("landsat is:",landsat)

print(landsat.keys())
print(landsat.values())
print(landsat.pop('country:'))
print(landsat.get('numberOfBand:'))

#string
var="mahdi is the best"

print(var[0])
print(var[0:])
print(var[:])
print(var[2:10])
print(var[:15])
print(len(var))


#lists

satellite=['landsat','modis','sentinel','noaa',10]

print(satellite[0],satellite[4])
print(satellite[0:2])

#append
satellite.append('spot')
print(satellite)
#change
satellite[3]='change'
print(satellite)
#delete
del satellite[2]
print(satellite)
#add
satellite=satellite+[10,20,30]
print(satellite)

#tuple

satellite=('landsat','modis','sentinel','noaa',10)
print(satellite)
#Error
#print(satellite.append(10))