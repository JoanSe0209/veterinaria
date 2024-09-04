from os import system, name
from historialmedico import HistorialMedico

def main():
    try:
        while True:
            print('*************** MENU HISTORIALES MÉDICOS ********************')

            print('1 - Registrar historial médico')
            print('2 - Buscar un historial médico por codigo')
            print('3 - Buscar un historial médico por codigo de mascota')
            print('4 - Actualizar historial médico')
            print('5 - Eliminar un historial médico')
            print('6 - Salir del sistema')

            print('*************** MENU HISTORIALES MÉDICOS ********************')
            
            while True:
                try:
                    opcion = int(input('Seleccione una opción: '))
                    if opcion in [1, 2, 3, 4, 5, 6]:
                        break
                    else:
                        print('Opción no válida. Intente de nuevo.')
                except ValueError:
                    print('Opción no válida. Ingrese un número.')

            if opcion == 6:
                print('Gracias por usar nuestra app...')
                break
            
            elif opcion == 1:
                system('cls' if name == 'nt' else 'clear')
                print('1 - Registrar historial médico')
                historial = HistorialMedico()
                historial.registrar_historial_medico()
            
            elif opcion == 2:
                system('cls' if name == 'nt' else 'clear')
                print('2 - Buscar un historial médico por codigo')
                codigo = int(input('Código del producto a buscar: '))
                historial = HistorialMedico()
                historial.consultar_historial_por_codigo(codigo)

            elif opcion == 3:
                system('cls' if name == 'nt' else 'clear')
                print('3 - Buscar un historial médico por codigo de mascota')
                codigo_mascota = int(input('codigo de mascota: '))
                historial = HistorialMedico()
                historial.consultar_historial_por_mascota(codigo_mascota)

            elif opcion == 4:
                system('cls' if name == 'nt' else 'clear')
                print('4 - Actualizar historial médico')
                codigo_mascota = int(input('codigo de mascota: '))
                historial = HistorialMedico()
                historial.actualizar_historial_por_mascota(codigo_mascota)

            elif opcion == 5:
                system('cls' if name == 'nt' else 'clear')
                print('5 - Eliminar un historial médico')
                codigo = int(input('Código del historial a eliminar: '))
                historial = HistorialMedico()
                historial.eliminar_historial(codigo)
            
    except KeyboardInterrupt:
        print('\nEl usuario ha cancelado la ejecución.')
    except Exception as error:
        print(f'Ha ocurrido un error no codificado: {error}')
    finally:
        print('Fin del programa.')

if __name__ == "__main__":
    main()
