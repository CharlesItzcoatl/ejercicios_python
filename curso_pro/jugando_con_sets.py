my_set1 = {1, 2, 3, 4, 5}
my_set2 = {3, 4, 5, 6, 7}
my_set3 = {'a', 'b', 'c', 'd', 'e', 1, 2}

print(f'Unión: {my_set1 | my_set2}')
print(f'Intersección: {my_set1 & my_set2}')
print(f'Diferencia: {my_set1 - my_set2}')
print(f'Diferencia simétrica: {my_set1 ^ my_set2}\n')


print(f'Unión: {my_set1 | my_set3}')
print(f'Intersección: {my_set1 & my_set3}')
print(f'Diferencia: {my_set1 - my_set3}')
print(f'Diferencia simétrica: {my_set1 ^ my_set3}\n')


print(f'Unión: {my_set2 | my_set3}')
print(f'Intersección: {my_set2 & my_set3}')
print(f'Diferencia: {my_set2 - my_set3}')
print(f'Diferencia simétrica: {my_set2 ^ my_set3}')