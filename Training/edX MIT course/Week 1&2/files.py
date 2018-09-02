name_handle = open('fExample.py', 'w')

for i in range(2):
    name = input('Enter name: ')
    name_handle.write(name + '\n')
name_handle.close()


