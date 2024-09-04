from conexion10 import BaseDatos
import datetime


class HistorialMedico:
    def __init__(self,
                 codigo: int = None,
                 codigo_mascota: int = None,
                 fecha: datetime.datetime = None,
                 descripcion: str = None,
                 tratamiento: str = None
                ):
        self._codigo = codigo
        self._codigo_mascota = codigo_mascota
        self._fecha = fecha
        self._descripcion = descripcion
        self._tratamiento = tratamiento


#GET Y SET

    def get_codigo(self):
        return self._codigo


    def set_codigo(self):
        while True:
            try:
                codigo = int(input('Ingrese el codigo del historial medico -> '))
                if (1 <= codigo <= 1000000000000):
                    self._codigo = codigo
                    break
                else:
                    print('El número debe estar entre 1 y 1000000000000')
            except ValueError:
                print('El codigo deber ser un numero')
            continue


    def get_codigo_mascota(self):
        return self._codigo_mascota
    
    
    def set_codigo_mascota(self):
        while True:
            try:
                codigo_mascota = int(input('Escriba el código de la mascota: '))
                if (1 <= codigo_mascota <= 1000000000):
                    self._codigo_mascota = codigo_mascota
                    break
                else:
                    print('El número debe estar entre 1 y 1000000000')
            except ValueError:
                print('El código debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')

    
    def get_fecha(self):
        return self._fecha
    

    def set_fecha(self):
        while True:
            try:
                fecha_str = input ('Ingrese la fecha de la cita DD/MM/YYYY -> ')
                fecha = datetime.datetime.strptime(fecha_str, '%d/%m/%Y')  
                self._fecha = fecha
                break
            except ValueError:
                print('La fecha debe estar en el formato DD/MM/YYYY')
            continue

    
    def get_descripcion(self):
        return self._descripcion
    

    def set_descripcion(self):
        descripcion = input('Ingrese la descripción del historial medico -> ')
        self._descripcion = descripcion
    

    def get_tratamiento(self):
        return self._tratamiento
    

    def set_tratamiento(self):
        tratamiento = input('Ingrese el tratamiento -> ')
        self._tratamiento = tratamiento


    def capturar_datos_historial(self):
        self.set_codigo()
        self.set_codigo_mascota()
        self.set_fecha()
        self.set_descripcion()
        self.set_tratamiento()

    
    def registrar_historial_medico(self):
        self.capturar_datos_historial()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()
                cursor_historial.callproc('InsertarHistorialMedico', [
                    self.get_codigo(),
                    self.get_codigo_mascota(),
                    self.get_fecha(),
                    self.get_descripcion(),
                    self.get_tratamiento()
                ])
                conexion.commit()
                print('Historial registrado correctamente...')
            except Exception as e:
                print(f'Error al registrar el historial medico: {e}')
                conexion.rollback()
            finally:
                cursor_historial.close
                BaseDatos.desconectar()


    def consultar_historial_por_codigo(self, codigo = None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()
                cursor_historial.callproc('BuscarHistorialPorCodigo', [codigo])
                for busqueda in cursor_historial.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        fecha_formateada = datetime.datetime.strptime(str(resultado[2]), '%Y-%m-%d').strftime('%d/%m/%Y')
                        descripcion = resultado[3]
                        tratamiento = resultado[4]
                        resultado = f'{resultado[0]}, {resultado[1]}, {fecha_formateada}, {descripcion}, {tratamiento}'
                        print(resultado)
                        return True
                    else:
                        print('Historial no encontrado.')
                        return False
            except Exception as e:
                print(f'Error al buscar el historial medico: {e}')

    
    def consultar_historial_por_mascota(self, codigo_mascota = None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_historial = conexion.cursor()
                cursor_historial.callproc('BuscarHistorialPorCodigo', [codigo_mascota])
                for busqueda in cursor_historial.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        fecha_formateada = datetime.datetime.strptime(str(resultado[2]), '%Y-%m-%d').strftime('%d/%m/%Y')
                        descripcion = resultado[3]
                        tratamiento = resultado[4]
                        resultado = f'{resultado[0]}, {resultado[1]}, {fecha_formateada}, {descripcion}, {tratamiento}'
                        print(resultado)
                        return True
                    else:
                        print('Historial no encontrado.')
                        return False
            except Exception as e:
                print(f'Error al buscar el historial medico: {e}')
    

    def actualizar_historial_por_mascota(self, codigo_mascota):
        conexion = BaseDatos.conectar()
        if self.consultar_historial_por_mascota(codigo_mascota):
            try:
                print('Escriba los nuevos datos del historial medico')
                self.set_codigo()
                self.set_codigo_mascota()
                self.set_fecha()
                self.set_descripcion()
                self.set_tratamiento()
                cursor_historial = conexion.cursor()
                cursor_historial.callproc('ActualizarHistorialPorMascota', [
                    self.get_codigo(),
                    self.get_codigo_mascota(),
                    self.get_fecha(),
                    self.get_descripcion(),
                    self.get_tratamiento()
                    ])
                conexion.commit()
                print('Historial medico actualizado correctamente')
            except Exception as error:
                print(f'Error al actualizar el historial_medico: {error}')
            finally:
                if conexion:
                    cursor_historial.close()
                    BaseDatos.desconectar()
        else:
            print('Historial no encontrado.')

    
    def eliminar_historial(self, codigo):
        conexion = BaseDatos.conectar()
        if self.consultar_historial_por_codigo(codigo):
            try:
                cursor_historial = conexion.cursor()
                cursor_historial.callproc('EliminarHistorial', [codigo])
                conexion.commit()
                print('Historial eliminado.')
            except Exception as e:
                print(f'Error al eliminar el historial medico: {e}')
                conexion.rollback()
            finally:
                if conexion:
                    cursor_historial.close()
                    BaseDatos.desconectar()
        else:
            print('Historial no encontrado...')