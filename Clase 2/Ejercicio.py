#implementar un sistema de monitoreo para facturacion, va atener manejo de exepciones por consola .log
import logging
from dataclasses import dataclass
#utilizamos el mismo manejador
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='ejercicio2.log',
    filemode='w' #parametro a o w 
    )
#crear un nuevo manejador handler para gestionar mensajes de gestion por .log y por consola
console_handler = logging.StreamHandler() #CREANDO UN NUEVO OBJETO PARA GESTIONAR LOS MENSAJES DE AUDITORIA (creando una instancia)
console_handler.setLevel(logging.DEBUG)#configurar el nivel del logging, el nivel mas leve
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',))#estamos dando formato de salida al logging
logging.getLogger().addHandler(console_handler)#estamos agregando la instancia o objeto un manejador

@dataclass
class Factura:
    cliente: str
    cantidad: int
    precio_unitario: float

    def procesar(self):
        try:
            logging.info(f'iniciando el proceso de facturacion para el cliente {self.cliente}')
            if self.cantidad <= 0:
                raise ValueError(f'la cantidad del producto debe ser mayor a cero')
            if self.precio_unitario <= 0:
                raise ValueError(f'el precio debe ser mayor a cero')
            total = self.cantidad * self.precio_unitario
            logging.info(f'factura fue procesada con exito. total de la compra{total } - cliente {self.cliente}')
        except ValueError as e:
            logging.error(f'error de validacion del cliente {self.cliente}: {e}')
        except Exception as e:
            logging.critical(f'error inesperado al momento de proceesar la factura de {self.cliente}: {e}')
        finally:
            logging.info(f'el  proceso de facturacion para {self.cliente} finallizo')
if __name__ ==  '__main__':
    factura1 = Factura('carlos',100,1500.25)
    factura1.procesar()


        




