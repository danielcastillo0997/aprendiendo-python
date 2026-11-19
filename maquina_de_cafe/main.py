
# ============================================================
# MÁQUINA DE CAFÉ - PROGRAMA PRINCIPAL
# Archivo: main.py
# ============================================================

# Importamos nuestras funciones.

from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import registrar_pedido, mostrar_historial, contar_pedidos


# ============================================================
# FUNCIÓN PRINCIPAL
# ============================================================

def main():

    while True:

        # Mostrar el menú principal.
        mostrar_menu()

        # Solicitar una opción.
        opcion = input("Selecciona una opción: ")

        # ----------------------------------------------------
        # OPCIÓN 1 - PEDIR CAFÉ
        # ----------------------------------------------------

        if opcion == "1":

            cafe = pedir_cafe()

            # Solo registramos si la selección es válida.
            if cafe is not None:

                registrar_pedido(cafe)

        # ----------------------------------------------------
        # OPCIÓN 2 - VER HISTORIAL
        # ----------------------------------------------------

        elif opcion == "2":

            mostrar_historial()

        # ----------------------------------------------------
        # OPCIÓN 3 - SALIR
        # ----------------------------------------------------

        elif opcion == "3":

            print("\nGracias por utilizar nuestra máquina de café.")

            print("Total de pedidos:", contar_pedidos())

            break

        # ----------------------------------------------------
        # OPCIÓN INVÁLIDA
        # ----------------------------------------------------

        else:

            print("Opción inválida. Intenta nuevamente.")


# ============================================================
# EJECUTAR EL PROGRAMA
# ============================================================

if __name__ == "__main__":
    main()


# APUNTES:
#
# from historial import ...
# Importa funciones creadas en otro módulo.
#
# cafe = pedir_cafe()
# Guarda el café seleccionado.
#
# if cafe is not None:
# Comprueba que el usuario eligió un café válido.
#
# registrar_pedido(cafe)
# Guarda el pedido en la lista.
#
# mostrar_historial()
# Imprime los pedidos registrados.
#
# break:
# Termina el bucle while.
