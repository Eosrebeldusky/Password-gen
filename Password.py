import random
import os

f = open ('D:\Python-pruebas\Password\password.txt','w')

lower ='abcdefghijklmnopqrstuvwxyz'
upper ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number ='1234567890'
symmbols = '[]()*;/,-+'

all = lower + upper + number + symmbols 

try:
    length = int(input('Defina el largo de la constrasena'))
except ValueError:
    print('Cargue un numero en el largo de la contrasena')

password =''.join(random.sample(all,length))
print (password)
f.write(password)
f.close()
os.startfile('D:\Python-pruebas\Password\password.txt')
