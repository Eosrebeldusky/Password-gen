from ast import Break
import random
import os
from tokenize import Number

f = open ('D:\Python-pruebas\Password\password.txt','w')

lower ='abcdefghijklmnopqrstuvwxyz'
upper ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number ='1234567890'
symmbols = '[]()*;/,-+'

all = lower + upper + number + symmbols 
length = None

while True:
    try:
        length = int(input('Defina el largo de la constrasena'))
    except ValueError:
        print('Cargue un numero en el largo de la contrasena')
        continue
    password =''.join(random.sample(all,length))
    print (password)
    f.write(password)
    f.close()
    os.startfile('D:\Python-pruebas\Password\password.txt')
    break
