list = ['a', 'b', 'c']

try:
    print(list[1])

except IndexError:
    print('test')

finally:
    print('Finaly')
