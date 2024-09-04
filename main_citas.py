from os import system, name
from cita import Cita

def main():
    try:
        while True:
            print('*************** MENU CITAS ********************')

            print('1 - Registrar nueva cita')
            print('2 - Buscar un cita por codigo')
            print('3 - Buscar un cita por mascota')
            print('4 - Buscar cita por fecha')
            print('5 - Buscar citas (TODAS)')
            print('6 - Actualizar cita')
            print('7 - Eliminar cita')
            print('8 - Salir')

            print('*************** MENU CITAS ********************')
            
            while True:
                try:
                    opcion = int(input('Seleccione una opción: '))
                    if opcion in [1, 2, 3, 4, 5, 6, 7, 8]:
                        break
                    else:
                        print('Opción no válida. Intente de nuevo.')
                except ValueError:
                    print('Opción no válida. Ingrese un número.')

            if opcion == 8:
                print('Gracias por usar nuestra app...')
                break
            
            elif opcion == 1:
                system('cls' if name == 'nt' else 'clear')
                print('1 - Registrar nueva cita')
                cita = Cita()
                cita.registrar_cita()
            
            elif opcion == 2:
                system('cls' if name == 'nt' else 'clear')
                print('2 - Buscar un cita por codigo')
                codigo = int(input('Código de la cita a buscar: '))
                cita  = Cita()
                cita.consultar_cita_por_codigo(codigo)

            elif opcion == 3:
                system('cls' if name == 'nt' else 'clear')
                print('3 - Buscar un cita por mascota')
                codigo_mascota = int(input('Codigo de la mascota: '))
                cita = Cita()
                cita.consultar_cita_por_mascota(codigo_mascota)

            elif opcion == 4:
                system('cls' if name == 'nt' else 'clear')
                print('4 - Buscar cita por fecha')
                fecha = str(input('Fecha de la cita: '))
                cita = Cita()
                cita.consultar_cita_por_fecha(fecha)

            elif opcion == 5:
                system('cls' if name == 'nt' else 'clear')
                print('5 - Buscar citas (TODAS)')
                cita = Cita()
                cita.consultar_citas()
            
            elif opcion == 6:
                system('cls' if name == 'nt' else 'clear')
                print('6. Actualizar cita')
                codigo = int(input('Código de la cita a actualizar: '))
                cita = Cita()
                cita.actualizar_cita(codigo)

            elif opcion == 7:
                system('cls' if name == 'nt' else 'clear')
                print('7. Eliminar cita')
                codigo = int(input('Código de la cita a eliminar: '))
                cita = Cita()
                cita.eliminar_cita(codigo)

    except KeyboardInterrupt:
        print('\nEl usuario ha cancelado la ejecución.')
    except Exception as error:
        print(f'Ha ocurrido un error no codificado: {error}')
    finally:
        print('Fin del programa.')

if __name__ == "__main__":
    main()
