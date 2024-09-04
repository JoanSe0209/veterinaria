from os import system, name
from servicio import Servicio

def main():
    try:
        while True:
            print('*************** MENU SERVICIOS ********************')

            print('1 - Registrar nuevo servicio')
            print('2 - Buscar un servicio por ID')
            print('3 - Buscar un servicio por nombre')
            print('4 - Buscar servicios (TODOS)')
            print('5 - Actualizar servicio')
            print('6 - Eliminar un servicio')
            print('7 - Salir del sistema')

            print('*************** MENU SERVICIOS ********************')
            
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
                print('1 - Registrar nuevo servicio')
                servicio = Servicio()
                servicio.registrar_servicio()
            
            elif opcion == 2:
                system('cls' if name == 'nt' else 'clear')
                print('2 - Buscar un producto por ID')
                codigo = int(input('Código del servicio a buscar: '))
                servicio = Servicio()
                servicio.consultar_servicio_por_codigo(codigo)

            elif opcion == 3:
                system('cls' if name == 'nt' else 'clear')
                print('3 - Buscar un servicio por nombre')
                nombre = str(input('Nombre del servicio a buscar: '))
                servicio = Servicio()
                servicio.consultar_servicio_por_nombre(nombre)

            elif opcion == 4:
                system('cls' if name == 'nt' else 'clear')
                print('4 - Buscar servicios (TODOS)')
                servicio = Servicio()
                servicio.colsultar_todos_los_servicios()

            elif opcion == 5:
                system('cls' if name == 'nt' else 'clear')
                print('5 - Actualizar servicio')
                codigo = int(input('Código del servicio para actualizar: '))
                servicio = Servicio()
                servicio.actualizar_servicio(codigo)
            
            elif opcion == 6:
                system('cls' if name == 'nt' else 'clear')
                print('6. Eliminar un servicio')
                codigo = int(input('Código del servicio a eliminar: '))
                servicio = Servicio()
                servicio.eliminar_servicio(codigo)

    except KeyboardInterrupt:
        print('\nEl usuario ha cancelado la ejecución.')
    except Exception as error:
        print(f'Ha ocurrido un error no codificado: {error}')
    finally:
        print('Fin del programa.')

if __name__ == "__main__":
    main()
