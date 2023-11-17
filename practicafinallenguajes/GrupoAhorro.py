class GrupoAhorro:
    def __init__(self, nombres="", correo="", contraseña="", cuenta=6000):
        self.datos_personales = (nombres, correo, contraseña)
        self.cuenta = cuenta

    def obtener_datos_personales(self):
        return self.datos_personales

    def obtener_cuenta(self):
        return self.cuenta

    def establecer_cuenta(self, nuevo_saldo):
        self.cuenta = nuevo_saldo


class Clientes(GrupoAhorro):
    def __init__(self, nombres="", correo="", contraseña=""):
        super().__init__(nombres, correo, contraseña)


class CrearGrupo:
    def login_grupos(self, lista_usuarios):
        while True:
            print("1. Grupo de ahorro de 2 personas")
            print("2. Grupo de ahorro de 3 personas")
            print("3. Volver al menú principal")
            opcion = input("")
            while True:
                if opcion in ["1", "2"]:
                    num_personas = 2 if opcion == "1" else 3
                    nombres = []

                    for i in range(num_personas):
                        print(f"Ingrese la información del usuario {i + 1}:")
                        nombre = input("Ingrese un nombre de usuario: ")
                        contraseña = input("Ingrese la contraseña: ")

                        # Verificar si el usuario existe en la lista_usuarios
                        usuario_encontrado = False
                        for usuario in lista_usuarios:
                            if usuario.obtener_datos_personales()[0] == nombre and usuario.obtener_datos_personales()[2] == contraseña:
                                print("Usuario encontrado")
                                usuario_encontrado = True
                                break

                        if not usuario_encontrado:
                            print("Usuario no encontrado. Vuelva a intentar.")
                            return None

                        nombres.append(nombre)

                    grupo_correo = input("Ingrese el correo del usuario del grupo: ")
                    grupo_contraseña = self.solicitar_contraseña_grupo()
                    return nombres, grupo_correo, grupo_contraseña

                elif opcion == "3":
                    print("Volviendo al menú principal...")
                    break

                else:
                    print("Escoga una opción válida")

    def solicitar_contraseña_grupo(self):
        while True:
            grupo_contraseña = input("Ingrese la contraseña para el grupo de ahorros: ")
            grupo_vefcontraseña = input("Ingrese la contraseña para el grupo de ahorros (verificación): ")

            if grupo_contraseña == grupo_vefcontraseña:
                return grupo_contraseña
            else:
                print("La verificación de la contraseña no coincide. Vuelva a intentar.")
                print(25 * "")

    def crear_grupo(self, lista_usuarios, lista_grupos):
        datos_usuario = self.login_grupos(lista_usuarios.lista_usuarios)
        if datos_usuario:
            nombres, correo, contraseña = datos_usuario

            grupo = GrupoAhorro(nombres=nombres, correo=correo, contraseña=contraseña)

            lista_grupos.agregar_grupo(grupo)
