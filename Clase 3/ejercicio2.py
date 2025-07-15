class Reserva:
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.fecha = fecha
    
reservas = [
    Reserva('juan','None'),
    Reserva('caro', '2025-01-29')         
            
    ]
for reserva in reservas:
    if not reserva.fecha:
        print(f'error: fecha no asignada para el cliente{reserva.cliente}')
        
