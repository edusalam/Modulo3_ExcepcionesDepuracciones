'''
ESTRUCTURA BASICA DE EXCEPCIONES: TELEFONO PROFE LUIS MOLERO @3187862501, CORREO LUISGUILLERMOMOLERO@GMAIL.COM
try: #es donde se coloca la logica del proyecto
    #codiigo

except AlgunaExcepcion as e:  # cuando se capturan los errores
    #codigo

else: #si todo correo bien se ejecuta el else
    #codiigo

finally: #siempre se va a ejecutar
    #codigo

#PROGRAMA DIVIDIR DOS NUMEROS
#con captura de excepciones
def division_cero(numero1, numero2):
    try:
        resultado = numero1 / numero2
        print(f'resultado es{resultado}')
    except ZeroDivisionError as e:
        print('la division entre cero no se puede lograr')
        return None
division_cero(2,0)

   #sin captuura de e xcepciones     
 def division_cero(numero1, numero2):
    try:
        resultado = numero1 / numero2
        print(f'resultado es{resultado}')
    except ZeroDivisionError as e:
        print('la division entre cero no se puede lograr')    
division_cero(2,0)

              EJERCICIO 2   
#explicacion las exepciones multiples
def division_segura():

    try:
        numerador = int(input('intgrese por favor el numerador de la divisiion'))

        denominador = int(input('ingrese por favor el denommiinador'))

        resultado = numerador / denominador

        print(f'el resultado de la division de {numerador } entre el {denominador} es igual a . {resultado}') 

    except (ZeroDivisionError, ValueError) as e:
        print(f'error{e}')

division_segura()

                #ejercicio 3, manejo de excepciones especificas exepcion <<no es recomendable siempre ya que puede esconder errores>>

def abrir_archivo():
    try:
        with open('datos.txt', 'r') as archivo:
            contenido = archivo.read()
            numero = int(contenido.strip())
            print(numero)
    except Exception as e:
        print(f'se produjo un error{e}')        

abrir_archivo() 


               #USO DEL ELSE Y FINALLY, ejercicio de division por cero

def division_completa():
    try:
        numero = int(input('ingrese un numero'))
        resultado = 10 / numero        
    except ValueError as e: #CAPTURA
        print(f'error: {e}')
    except ZeroDivisionError as e: #DIVISION POR CERO
        print(f'error: {e}')
    else:
        print(f'el resultado de la division es {resultado}')
    finally:
        print('la operacion finalizo...')
division_completa()

          #APP QUE PERMITA PROCESAR PEDIDOS
def procesarPedidos():
    try:
        codigoProducto = input('ingrese el codigo del producto: ')
        cantidad = int(input('ingrese la cantiidad del producto'))

        if not codigoProducto.isalnum(): #validar el codigo del producto sea alfanumerico y validar que la cantidad sea mayor a cero
            raise ValueError('el codigo del producto debe ser alfanumerico')
        
        if cantidad <= 0:
            raise ValueError('la cantidad del producto debe ser mayor a cero')
        precioUnitario = 50
        total = precioUnitario * cantidad

    except ValueError as e:
        print(f'error al proocesar el pedido: {e}')
    
    else:
        print(f'total a pagar: {total}')
    finally:
        print('operacion finalizada')
procesarPedidos()
'''
               #ULTIMO EJERCICIO, EXCEPCIONES PERSONALIZADAS
class ErrorProducto(Exception):
    def __init__(objeto, message = 'el producto no esta disponible en stock'):
        objeto.message = message
        





    

          
 
 