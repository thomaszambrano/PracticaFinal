class ListaGrupoAhorro:
    def __init__(self):
        self.lista_grupo_ahorro = []

    def agregar_grupo(self, usuarios):
        self.lista_grupo_ahorro.append(usuarios)

    def imprimir_usuarios(self):
        print("Lista de todos los grupos registrados en EAFITBank: ")
        for grupo in self.lista_grupo_ahorro:
            datos_personales = grupo.obtener_datos_personales()
            cuenta = grupo.obtener_cuenta()
            print(f"Nombre: {datos_personales[0]}")
            print(f"Correo: {datos_personales[1]}")
            print(f"Saldo de la cuenta: {cuenta}")
            print(25 * "-")