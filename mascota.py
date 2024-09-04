from conexion10 import BaseDatos
import re

class Mascota:
    def __init__(
            self,
            codigo: int = None,
            nombre: str = None,
            especie: str = None,
            raza: str = None,
            edad: float = None,
            peso: float = None,
            id_usuario: int = None,
            historial_medico=None
            ):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__especie = especie
        self.__raza = raza
        self.__edad = edad
        self.__peso = peso
        self.__id_usuario = id_usuario
        self.__historial_medico = historial_medico if historial_medico is not None else []

    # GET y SET

    def get_codigo(self):
        return self.__codigo
    
    def set_codigo(self):
        while True:
            try:
                codigo_mascota = int(input('Escriba el código de la mascota: '))
                if (1 <= codigo_mascota <= 1000000000):
                    self.__codigo = codigo_mascota
                    break
                else:
                    print('El número debe estar entre 1 y 1000000000')
            except ValueError:
                print('El código debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self):
        while True:
            try:
                nombre = input('Nombre de la mascota: ')
                if len(nombre) > 3:
                    self.__nombre = nombre
                    break
                else:
                    print('Nombre incorrecto. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue

    def get_especie(self):
        return self.__especie

    def set_especie(self):
        while True:
            try:
                especie = input('Especie de la mascota (gato, perro...): ')
                if 3 < len(especie) <= 50:
                    self.__especie = especie
                    break
                else:
                    print('Datos incorrectos. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue

    def get_raza(self):
        return self.__raza
    
    def set_raza(self):
        while True:
            try:
                raza = input('Raza de la mascota: ')
                if re.match(r'^[A-Za-z\s]{3,30}$', raza):
                    self.__raza = raza
                    break
                else:
                    print('Datos de raza incorrectos. Intente de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue

    def get_edad(self):
        return self.__edad
    
    def set_edad(self):
        while True:
            try:
                edad = float(input('Edad de la mascota (años): '))
                if 0 < edad <= 80.0:
                    self.__edad = edad
                    break
                else:
                    print('Edad no válida')
            except ValueError:
                print('Edad acepta solo números.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue                

    def get_peso(self):
        return self.__peso
    
    def set_peso(self):
        while True:
            try:
                peso = float(input('Peso en kg: '))
                if 0.1 < peso <= 1000.0:
                    self.__peso = peso
                    break
                else:
                    print('Peso no válido')
            except ValueError:
                print('El peso acepta solo números')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue                 

    def get_usuario(self):
        return self.__id_usuario
    
    def set_usuario(self):
        while True:
            try:
                id_usuario = int(input('Id usuario: '))
                if id_usuario > 0:
                    self.__id_usuario = id_usuario
                    break
                else:
                    print('Usuario no válido')
            except ValueError:
                print('Solo se admiten números')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
            continue    

    def get_historial(self):
        return self.__historial_medico
    
    def agregar_historial_medico(self, entrada: str):
        self.__historial_medico.append(entrada)

    def capturar_datos(self):
        self.set_codigo()
        self.set_nombre()
        self.set_especie()
        self.set_raza()
        self.set_edad()
        self.set_peso()
        self.set_usuario()


    def registrar_mascota(self):
        self.capturar_datos()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('InsertarMascota', [
                    self.get_codigo(),
                    self.get_nombre(),
                    self.get_especie(),
                    self.get_raza(),
                    self.get_edad(),
                    self.get_peso(),
                    self.get_usuario()
                ])
                conexion.commit()
                print('Mascota registrada correctamente...')
            except Exception as e:
                print(f'Error al registrar la mascota: {e}')
                conexion.rollback() 
            finally:
                cursor_mascota.close()
                BaseDatos.desconectar()


    def buscar_mascota_todas(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('ConsultarMascotas')
                for busqueda in cursor_mascota.stored_results():
                    resultado = busqueda.fetchall()
                    if resultado:
                        resultado_ordenado = sorted(resultado, key=lambda x: x[0])
                        print('Resultado:')
                        print('************************************************')
                        for fila in resultado_ordenado:
                            print(fila)
                        print('************************************************')
                        return True
                    else:
                        print('Mascota no encontrada.')
                        return False
            except Exception as e:
                print(f'Error al buscar la mascota: {e}')
            finally:
                if conexion:
                    cursor_mascota.close()
                    BaseDatos.desconectar()




    def buscar_mascota(self, codigo_mascota=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('ConsultarMascotaPorId', [codigo_mascota])
                for busqueda in cursor_mascota.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        print('Resultado:')
                        print('************************************************')
                        print(resultado)
                        print('************************************************')
                        return True
                    else:
                        print('Mascota no encontrada.')
                        return False
            except Exception as e:
                print(f'Error al buscar la mascota: {e}')
            finally:
                if conexion:
                    cursor_mascota.close()
                    BaseDatos.desconectar()

    
    def buscar_mascota_por_nombre(self, nombre=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('ConsultarMascotaPorNombre', [nombre])
                for busqueda in cursor_mascota.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        print('Resultado:')
                        print('************************************************')
                        print(resultado)
                        print('************************************************')
                        return True
                    else:
                        print('Mascota no encontrada.')
                        return False
            except Exception as e:
                print(f'Error al buscar la mascota: {e}')
            finally:
                if conexion:
                    cursor_mascota.close()
                    BaseDatos.desconectar()


    def actualizar_mascota(self, codigo_mascota):
        conexion = BaseDatos.conectar()
        if self.buscar_mascota(codigo_mascota):
            try:
                print('Escriba los nuevos datos de la mascota: ')
                self.set_nombre()
                self.set_especie()
                self.set_raza()
                self.set_edad()
                self.set_peso()
                
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('ActualizarMascota', [
                    codigo_mascota,
                    self.get_nombre(),
                    self.get_especie(),
                    self.get_raza(),
                    self.get_edad(),
                    self.get_peso(),
                ])
                conexion.commit()
                print('Mascota actualizada correctamente.')
            except Exception as error:
                print(f'Error al actualizar la mascota: {error}')
            finally:
                if conexion:
                    cursor_mascota.close()
                    BaseDatos.desconectar()
        else:
            print('Mascota no encontrada.')


    def eliminar_mascota(self, codigo_mascota):
        conexion = BaseDatos.conectar()
        if self.buscar_mascota(codigo_mascota):
            try:
                print("Iniciando la eliminación...")
                cursor_mascota = conexion.cursor()
                cursor_mascota.callproc('EliminarMascota', [codigo_mascota])
                conexion.commit()
                print('Mascota eliminada correctamente.')
            except Exception as e:
                print(f'Error al eliminar la mascota: {e}')
                conexion.rollback()
            finally:
                if conexion:
                    cursor_mascota.close()
                    BaseDatos.desconectar()
        else:
            print('Mascota no encontrada.')
