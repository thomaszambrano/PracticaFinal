from Usuario import *

class Prestamo(Usuario):
    def __init__(self, nombre="", correo="", contraseña="", cuenta=1000, prestamo=0):
        super().__init__(nombre, correo, contraseña, cuenta)
        self.prestamo = prestamo

    def solicitar_prestamo(self, cantidad):
        if cantidad <= 0:
            print("La cantidad del préstamo debe ser mayor que cero.")
        else:
            self.prestamo += cantidad
            print(f"Se ha añadido un préstamo de {cantidad} a su cuenta.")

    def pagar_prestamo(self, cantidad):
        if self.prestamo == 0:
            print("No tienes ningún préstamo pendiente.")
        elif cantidad > self.prestamo:
            print("La cantidad de pago no puede ser mayor que la cantidad del préstamo.")
        else:
            self.prestamo -= cantidad
            print(f"Has pagado {cantidad} de tu préstamo. Tu saldo de préstamo restante es {self.prestamo}.")

    def verificar_estado_prestamo(self):
        if self.prestamo > 0:
            print(f"Tienes un préstamo pendiente de {self.prestamo}.")
        else:
            print("No tienes ningún préstamo pendiente.")
