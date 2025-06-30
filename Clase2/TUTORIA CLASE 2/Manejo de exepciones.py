#evento
'''
nombre=input('ingrese su nombre')
print('hola', nombre)

# EL BLOQUE TRY SE UTILIZA PARA ENVOLVER EL CODIGO QUE PUEDA GENERAR EXCEPCIONES SI OCURRE UNA EXEPCION, EJECUTA EL BLOQUE EXCEPT
try:
   num = int(input('ingrese un numero: '))
   print(f'el doble es : {num*2}')
except ValueError:
   print('Error: no ingresaste un numero valido')
#  EL BLEQUE ELSE SE EJECUTA SOLO SI NO OCCURE  NINGUNA EXXEPCION DENTRO DEL BLOQUE TRY
else:
   print(f'el numero ingresado es: {num}')
# EL BLOQUE FINALLY SIEMPRE SE EJECUTA INDEPENDIENTEMENTE SI OCURRE O NO UNA EXCEPTION, ES UTIL PARA LIBERAR RECURSOS, CERRAR ARCHIVOS
#CONEXIOONES O BASES DE DATO ETC.
try:
   archivo = open('archivo.txt','r')
   contenido = archivo.read()
   print(contenido)
except FileNotFoundError:
   print('Error: el archivo no existe')
finally:
    try:
       archivo.close()
       print('archivo cerrado')
    except NameError:
       print('el archhivo no se abrio, no hay que cerrar')
'''
#MANEJO DE MULTIPLES EXCEPCOINES, SE PUEDEN MANEJAR MULTIPLES EXCEPCIONES EN EL BLOQUE SEPARADOOS POR EXEP O AGRUPADOS EN UNA TUPLA
try: 
    num=int(input('ingrese un  numero valido.'))
    resultado = 10/num
except ValueError:
    print('error: no ingresaste un nummero valido')
except ZeroDivisionError:
    print('error: no se puede dividir por cero')

