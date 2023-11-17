class Usuario:
    def __init__(self, nombre="", correo="", contraseña="", cuenta=1000):
        self.datos_personales = (nombre, correo, contraseña)
        self.cuenta = cuenta

    def obtener_datos_personales(self):
        return self.datos_personales

    def obtener_cuenta(self):
        return self.cuenta
    
    def establecer_cuenta(self, nuevo_saldo):
        self.cuenta = nuevo_saldo

class Cliente(Usuario):
    def __init__(self, nombre="", correo="", contraseña=""):
        super().__init__(nombre, correo, contraseña)


class CrearUsuario:
    def SignUp(self):
        nombre = input("Ingrese un nombre de usuario: ")
        correo = input("Ingrese un correo electrónico: ")
        contraseña = self.solicitar_contraseña()
        return nombre, correo, contraseña
                
    def solicitar_contraseña(self):
        while True:
            grupo_contraseña = input("Ingrese una contraseña: ")
            grupo_vefcontraseña = input("Ingrese una contraseña(verificación): ")

            if grupo_contraseña == grupo_vefcontraseña:
                return grupo_contraseña
            else:
                print("La verificación de la contraseña no coincide. Vuelva a intentar.")
                print(25 * "")

    def crear_usuario(self, lista_usuarios):
        datos_usuario = self.SignUp()
        if datos_usuario:
            nombre, correo, contraseña = datos_usuario
            cliente = Cliente(nombre=nombre, correo=correo, contraseña=contraseña)
            lista_usuarios.agregar_usuario(cliente)

