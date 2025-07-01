#excepciones personalizadas
'''
class ErrorPago(Exception):
    pass
class PasarelaPago():
    #creacion de metodo estatico
    @staticmethod
    def procesar_Pago(numero_tarjeta, monto):

        if not  numero_tarjeta.startswith('4'):
            raise ErrorPago('el numero de la tarjeta no es valida')
        if monto <=0:
            raise ErrorPago('el monto debe ser mayor a cero')
        return f'pago del {monto} fue procesado con exito'
def procesarPagoCliente(nombre_cliente, numero_tarjeta, monto):
    try:
        print(f'iniciando el proceso de pago para {nombre_cliente}')
        resultado = PasarelaPago.procesar_Pago(numero_tarjeta, monto)
    except ErrorPago as e:
        print(f'error al procesar el pago{e}')
        #ponemos una exepcion general
    except Exception as e:
        print(f'se produjo un error inesperado{e}')
    else:
        print(resultado)
    finally:
        print('registro finalizado')

if __name__=='__main__':
    #procesarPagoCliente('jose','432689',90.880)
    #procesarPagoCliente('luis', '1233588', 100)
    procesarPagoCliente('carolina', '456789',0)
'''
#tipos de eventos
#1. DEBUG
#2. INFO
#3. WARNING
#4. ERROR
#5. CRITICAL
import  logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s -%(message)s')

logging.info('mensaje de deupracioon')
        