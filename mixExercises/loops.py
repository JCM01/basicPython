r = 0
i = 0
while i <= 100:
    r += i
    i += 1
print(r)

for i in range(1, 100):
    if i % 2 != 0:
        print(i)
        if i == 55:
            break

ciudades =[ 'madrid', 'sevilla', 'burgos', 'barcelona', 'granada']

for i in ciudades:
    print(i[::-1])

ciudades.append('San Martín de la Vega del Alberche')
print(ciudades)

for i in ciudades:
    if(len(i)<=9):
        print(i)

