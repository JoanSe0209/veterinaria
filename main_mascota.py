from os import system, name
from mascota import Mascota

def main():
    try:
        while True:
            print('*************** MENU MASCOTAS ********************')

            print('1 - Registrar nueva mascota')
            print('2 - Buscar una mascota por ID')
            print('3 - Buscar una mascota por nombre')
            print('4 - Buscar mascotas (TODAS)')
            print('5 - Actualizar mascota')
            print('6 - Eliminar una mascota')
            print('7 - Salir del sistema')

            print('*************** MENU MASCOTAS ********************')
            
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
                print('1. Registrar Mascota')
                mascota = Mascota()
                mascota.registrar_mascota()
            
            elif opcion == 2:
                system('cls' if name == 'nt' else 'clear')
                print('2. Buscar Mascota por ID')
                codigo_mascota = int(input('Código de la mascota a buscar: '))
                mascota = Mascota()
                mascota.buscar_mascota(codigo_mascota)

            elif opcion == 3:
                system('cls' if name == 'nt' else 'clear')
                print('3. Buscar Mascota por nombre')
                nombre = str(input('Nombre de la mascota a buscar: '))
                mascota = Mascota()
                mascota.buscar_mascota_por_nombre(nombre)

            elif opcion == 4:
                system('cls' if name == 'nt' else 'clear')
                print('4. Buscar todas las mascotas')
                mascota = Mascota()
                mascota.buscar_mascota_todas()

            elif opcion == 5:
                system('cls' if name == 'nt' else 'clear')
                print('5. Actualizar Mascota')
                codigo_mascota = int(input('Código de la mascota a actualizar: '))
                mascota = Mascota()
                mascota.actualizar_mascota(codigo_mascota)
            
            elif opcion == 6:
                system('cls' if name == 'nt' else 'clear')
                print('6. Eliminar Mascota')
                codigo_mascota = int(input('Código de la mascota a eliminar: '))
                mascota = Mascota()
                mascota.eliminar_mascota(codigo_mascota)

    except KeyboardInterrupt:
        print('\nEl usuario ha cancelado la ejecución.')
    except Exception as error:
        print(f'Ha ocurrido un error no codificado: {error}')
    finally:
        print('Fin del programa.')

if __name__ == "__main__":
    main()
