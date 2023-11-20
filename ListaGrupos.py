class ListaGrupos:
    def __init__(self):
        self.lista_grupos = []

    def agregar_grupo(self, usuario):
        self.lista_grupos.append(usuario)

    def eliminar_grupo(self):
        pass

    def imprimir_grupos(self):
        print("Lista de todos los grupos registrados en EAFITBank: ")
        print(25*"")
        for grupo in self.lista_grupos:
            datos_personales = grupo.obtener_datos_personales_grupo()
            datos_grupo = grupo.obtener_datos_grupo_ahorro()
            print(f"Nombres de los usuarios del grupo: {datos_personales[0]}")
            print(f"Correo: {datos_personales[1]}")
            print(f"Nombre del grupo: {datos_grupo[0]}")
            print(f"Cuenta del grupo: {datos_grupo[1]}")
            print(f"Prestamo del grupo: {datos_grupo[2]} y plazo que tienen {datos_grupo[3]} meses")
            print(25 * "-")
