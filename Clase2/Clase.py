import logging
from dataclasses import dataclass, field # definir de forma mas rapido los contructores

# lo primero que se hace luego de traerlo es configurarlo
#valos a crear el handler el manejador del login
#lo primero que creamos es la configuracion
#EJERCICIO BASICO MENSAJES LOGGIN
'''
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.debug('mensaje es del DEBUG')
logging.info('este mensaje es del INFOR')
logging.warning('este mensaje es del WARNING')
logging.error('este mensaje es del error')
logging.critical('este mensaje es del critical')
'''
#app que permite llevar seguimiento de compras y fallos en este tipo de transaccioon
#esta app registrara la cantidad de registros comprados, confirmacion de compras y errores en estas transacciones.
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='registro.log',
    filemode='a'
    )
@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int

    def comprar(self, cantidad : int):
        if cantidad > self.cantidad:
            logging.error(f'Error: no hay suficiente cantidad del producto{self.nombre}. el stock disponible es de {self.cantidad}')
            raise ValueError(f'Error: no hay suficiente cantidad del producto{self.nombre}. el stock disponible es de {self.cantidad}')
        else:
            self.cantidad -= cantidad
            logging.info(f'la compra fue exitosa. el stock restante es {self.cantidad}')
            return self.precio * cantidad
        
@dataclass
class Tienda:
    productos: list[Producto] = field(default_factory=list)

    def agregar_producto(self, producto: Producto):
        self.productos.append(producto)
        logging.debug(f' {producto.nombre}fue agregado con exito. el precio es de {producto.precio} - cantodad: {producto.cantidad} unidades en stock')
    def realizar_compra(self, nombre_producto: str, cantidad: int):
        producto = next({p for p in self.productos if p.nombre == nombre_producto}, None)
        if producto:
            try:
                total = producto.comprar(cantidad)
                logging.info(f'compra realizada: {cantidad} unidades de {nombre_producto} por un total de ${total}')
                return total
            except ValueError as e:
                logging.error(f'error al efectual la compra: {e}')
            else:
                logging.warning(f'producto fuera de stock')
if __name__ =='main':
    tienda = Tienda()
    inventario_portatil = Producto(nombre = 'portatil',precio=100, cantidad=10)
    tienda.agregar_producto (inventario_portatil)
    tienda.realizar_compra('portatil',4)
        

