from Usuario import CrearUsuario
from ListaUsuarios import ListaUsuarios
from ListaGrupoAhorro import ListaGrupoAhorro
from GrupoAhorro import CrearGrupo


class Menu:

    def menuPrincipal(self):
        lista_usuarios = ListaUsuarios()
        lista_grupo = ListaGrupoAhorro()
        creador_usuario = CrearUsuario()
        grupo_ahorros = CrearGrupo()

        while True:
            print(25*"")
            print("1. Crear un nuevo usuario")
            print("2. Crear un grupo de ahorro")
            print("3. Pedir un prestamo para el grupo de ahorro")
            print("4. Impirmir lista de todos los usuarios de EAFITBank")
            print("5. Impirmir lista de todos los grupos de ahorro de EAFITBank")
            print("6. Salir de EAFITBank")
            print(25*"")

            opcion = input("Seleccione una opción: ")
            print(25*"")

            if opcion == "1":
                creador_usuario.crear_usuario(lista_usuarios)
            elif opcion == "2":
                grupo_ahorros.crear_grupo(lista_usuarios, lista_grupo)
            elif opcion == "3":
                pass
            elif opcion == "4":
                lista_usuarios.imprimir_usuarios()
            elif opcion == "5":
                lista_grupo.imprimir_usuarios()
            elif opcion == "6":
                print("Se ha cerrado EAFITBank")
                break
            else:
                print("Opción incorrecta, ingrese de nuevo un valor")

if __name__ == "__main__":
    menu = Menu()
    menu.menuPrincipal()
