# USO DE BREAKPOINT (PUNTO DE INTERRUPCION) SIMPLES
class  Empleado:
    def __init__(self, nombre, ventas):
        self.nombre = nombre
        self.ventas = ventas
    
    def calculo_comision(self):
        if self.ventas > 5000:
            print(f'*******empleado: {self.nombre}. ventas: {self.ventas}. comision del 10%')
            return self.ventas * 0.10
        print(f'------empleado: {self.nombre}. ventas: {self.ventas}. comision del 5%')
        return self.ventas * 0.05

empleados = [
    Empleado('Ana', 6000),
    Empleado('Eduard', 3000)
]
for emp in empleados:
    print(f'Empleado: {emp.nombre}. comision: {emp.calculo_comision()}')
