from Seguridad import Seguridad
seguridad = Seguridad()
class PrestamosGrupos:

    def prestar_dinero_grupo(self, lista_grupos):
        grupo = seguridad.Login_grupos(lista_grupos)
        if grupo is not None:
            prestamo = int(input("Ingrese el dinero que desea pedir prestado: "))
            plazo = int(input("Ingrese el tiempo que desea pedir prestado el dinero: "))
            if grupo[1] > prestamo + grupo[2] and plazo >= 2:
                print(f"El prestamo del dinero al grupo {grupo[0]} ha sido autorizado")
                grupo[1] += prestamo
                grupo[2] += prestamo
                grupo[3] += plazo

            else:
                print("El prestamo que se pide es mayor a la cantidad de dinero que tienen en la cuenta o el plazo es menor a dos meses")

        else:
            print("El grupo que ingresa no existe, vuelva a intentarlo de nuevo")

    def prestamo_otro_grupo(self):
        pass