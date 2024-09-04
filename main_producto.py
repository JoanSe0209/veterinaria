from os import system, name
from producto import Producto

def main():
    try:
        while True:
            print('*************** MENU PRODUCTOS ********************')

            print('1 - Registrar nuevo producto')
            print('2 - Buscar un producto por ID')
            print('3 - Buscar un producto por nombre')
            print('4 - Buscar productos (TODOS)')
            print('5 - Actualizar producto')
            print('6 - Eliminar un producto')
            print('7 - Salir del sistema')

            print('*************** MENU PRODUCTOS ********************')
            
            while True:
                try:
                    opcion = int(input('Seleccione una opción: '))
                    if opcion in [1, 2, 3, 4, 5, 6, 7]:
                        break
                    else:
                        print('Opción no válida. Intente de nuevo.')
                except ValueError:
                    print('Opción no válida. Ingrese un número.')

            if opcion == 7:
                print('Gracias por usar nuestra app...')
                break
            
            elif opcion == 1:
                system('cls' if name == 'nt' else 'clear')
                print('1 - Registrar nuevo producto')
                producto = Producto()
                producto.registrar_producto()
            
            elif opcion == 2:
                system('cls' if name == 'nt' else 'clear')
                print('2 - Buscar un producto por ID')
                codigo = int(input('Código del producto a buscar: '))
                producto = Producto()
                producto.consultar_producto_por_codigo(codigo)

            elif opcion == 3:
                system('cls' if name == 'nt' else 'clear')
                print('3 - Buscar un producto por nombre')
                nombre = str(input('Nombre del producto a buscar: '))
                producto = Producto()
                producto.consultar_producto_por_nombre(nombre)

            elif opcion == 4:
                system('cls' if name == 'nt' else 'clear')
                print('4 - Buscar productos (TODOS)')
                producto = Producto()
                producto.consultar_productos()

            elif opcion == 5:
                system('cls' if name == 'nt' else 'clear')
                print('5 - Actualizar producto')
                codigo = int(input('Código del producto para actualizar: '))
                producto = Producto()
                producto.actualizar_producto(codigo)
            
            elif opcion == 6:
                system('cls' if name == 'nt' else 'clear')
                print('6. Eliminar un producto')
                codigo = int(input('Código del producto a eliminar: '))
                producto = Producto()
                producto.eliminar_producto(codigo)

    except KeyboardInterrupt:
        print('\nEl usuario ha cancelado la ejecución.')
    except Exception as error:
        print(f'Ha ocurrido un error no codificado: {error}')
    finally:
        print('Fin del programa.')

if __name__ == "__main__":
    main()
