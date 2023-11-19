from Usuario import *

class Prestamo(Usuario):
    tasa_interes_mensual = 0.03

    def __init__(self, nombre="", correo="", contraseña="", cuenta=1000, prestamo=0):
        super().__init__(nombre, correo, contraseña, cuenta)
        self.prestamo = prestamo

    def solicitar_prestamo(self, cantidad, tiempo):
        interes_mensual = self.prestamo * self.tasa_interes_mensual
        cuota_mensual = self.prestamo / tiempo + interes_mensual
        self.prestamo -= cantidad

        if tiempo < 2 or cantidad <= 0:
            print("el plazo de pago debe superar lso dos meses y la cantidad del prestamo debe ser mayor que 0")
        else :
            self.prestamo += cantidad
            print(f"se ha añadido un prestamo por {cantidad} dolares a su cuenta y debera ser pagado en {tiempo} meses")





    def pagar_prestamo(self, cantidad, tiempo):
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




