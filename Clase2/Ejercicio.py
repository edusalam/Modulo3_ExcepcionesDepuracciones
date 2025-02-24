#implementar un sistema de monitoreo para facturacion, va atener manejo de exepciones por consola .log
import logging
from dataclasses import dataclass
#utilizamos el mismo manejador
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='ejercicio2.log',
    filemode='a'
    )
#crear un nuevo manejador handler para gestionar mensajes de gestion por .log y por consola

