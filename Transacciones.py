from Seguridad import Seguridad
seguridad = Seguridad()
class Transacciones:

    def ingresar_dinero(self, lista_usuarios):
        usuario = seguridad.Login(lista_usuarios)
        if usuario is not None:
            cuenta = usuario.obtener_cuenta()
            valor = input("Ingrese el monto que desea ingreasar a su cuenta de ahorros: ")
            cuenta += valor
            print("Recarga exitosa")
        else: 
            print("El usuario no se ha encontrado, intente de nuevo")

    def ingresar_dinero_grupo(self, lista_grupos):
        grupo = seguridad.Login(lista_grupos)
        if grupo is not None:
            valor = input("Ingrese el monto que desea ingreasar a su cuenta de grupo de ahorros: ")
            grupo[2] += valor
            print("Recarga exitosa")
        else: 
            print("El grupo no se ha encontrado, intente de nuevo")


    def sacar_dinero(self, lista_usuarios):
        usuario = seguridad.Login(lista_usuarios)
        if usuario is not None:
            cuenta = usuario.obtener_cuenta()
            valor = input("Ingrese el monto que desea sacar de su cuenta de ahorros: ")
            if cuenta > 0 and cuenta >= valor:
                cuenta = cuenta - valor
                print("Recarga exitosa")
            else:
                print("No hay plata en su cuenta de ahorros")
        else: 
            print("El usuario no se ha encontrado, intente de nuevo")

    def sacar_dinero_grupo(self, lista_grupos):
        grupo = seguridad.Login(lista_grupos)
        if grupo is not None:
            valor = input("Ingrese el monto que desea sacar de su cuenta de grupo de ahorros: ")
            if grupo[1] > 0 and grupo[1] >= valor:
                grupo[1] = grupo[1] - valor
                print("Recarga exitosa")
            else:
                print("No hay plata en su cuenta de grupo de ahorros")
        else: 
            print("El grupo no se ha encontrado, intente de nuevo")

    def pagar_deudas_grupo(self, lista_grupos):
        grupo = seguridad.Login_grupos(lista_grupos)
        if grupo is not None:

            if grupo[2] < 0:
                print("No hay deuda que pagar")

            print(f"Deuda de su grupo de ahorro {grupo[2]} y meses a los que tiene la deuda: {grupo[3]}")
            meses = int(input("Ingrese el numero de meses que desea pagar: "))
            total_a_pagar, valor_a_pagar = self.calcular_deuda_total(grupo, meses)

            if grupo[1] >= total_a_pagar:
                print(f"Su deuda a pagar es {total_a_pagar} y su cuenta de ahorros tiene {grupo[1]} por lo que su cuenta de ahorros quedaría: {grupo[1] - total_a_pagar}")
                print(25*"")
                opcion = input("¿Desea continuar? (S/N)")
                print(25*"")
                if opcion == "S":
                    print("Deuda saldada")
                    grupo[1] = grupo[1] - total_a_pagar
                    grupo[2] = grupo[2] - valor_a_pagar
                    grupo[3] = grupo[3] - meses
            else:
                print("No hay plata en su cuenta de grupo de ahorros")
        else: 
            print("El grupo no se ha encontrado, intente de nuevo")

    def movimientos(self, lista_usuarios):
        pass

    def movimientos_grupo(self, lista_grupos):
        grupo = seguridad.Login(lista_grupos)
        if grupo is not None:
            print(f"Todos los movimientos del grupo {grupo[0]}:")
            for movimientos in grupo[4]:
                print(movimientos)
        else: 
            print("El grupo no se ha encontrado, intente de nuevo")

    def calcular_deuda_total(self, grupo, meses):
        deuda_actual = grupo[2]
        if deuda_actual > 0:
            valor_por_mes = deuda_actual / grupo[3]
            valor_a_pagar = valor_por_mes * meses
            intereses = valor_a_pagar * (3 / 100) * meses
            total_a_pagar = valor_a_pagar + intereses
            return total_a_pagar, valor_a_pagar