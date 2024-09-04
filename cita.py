from conexion10 import BaseDatos
import re
import datetime, time

class Cita:
    def __init__(self,
                codigo: int = None,
                fecha: datetime.datetime = None,
                hora: datetime.datetime = None,
                estado: str = None,
                id_servicio: int = None,
                id_veterinario: int = None,
                codigo_mascota: int = None
                ):
            self._codigo = codigo
            self._fecha = fecha
            self._hora = hora
            self._estado = estado
            self._id_servicio = id_servicio
            self._id_veterinario = id_veterinario
            self._codigo_mascota = codigo_mascota

#GET Y SET

    def get_codigo(self):
        return self._codigo


    def set_codigo(self):
         while True:
            try:
                codigo = int(input('Ingrese el codigo de la cita -> '))
                if (1 <= codigo <= 10000000000):
                    self._codigo = codigo
                    break
                else:
                    print('El número debe estar entre 1 y 10000000000')
            except ValueError:
                print('El codigo debe ser un numero')
            continue
    

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

    
    def get_hora(self):
        return self._hora
    

    def set_hora(self):
        while True:
            try:
                hora_str = input('Ingrese la hora de la cita (formato HH:MM) -> ')
                hora = datetime.datetime.strptime(hora_str, '%H:%M').time()
                self._hora = hora
                break
            except ValueError:
                print('La hora debe tener el formato HH:MM y ser válida.')
            continue

    
    def get_estado(self):
        return self._estado
    

    def set_estado(self):
        while True:
            estado = str(input('Ingrese el estado de la cita (PENDIENTE, CONFIRMARDA, CANCELADA, COMPLETADA'))
            if estado in ['PENDIENTE', 'CONFIRMARDA', 'CANCELADA', 'COMPLETADA']:
                self._estado = estado
                break
            else:
                print('El estado debe ser PENDIENTE, CONFIRMARDA, CANCELADA, COMPLETADA')

    
    def get_id_servicio(self):
        return self._id_servicio
    

    def set_id_servicio(self):
         while True:
            try:
                id_servicio = int(input('Ingrese el codigo del servicio -> '))
                if (1 <= id_servicio<= 10000000000):
                    self._id_servicio = id_servicio
                    break
                else:
                    print('El número debe estar entre 1 y 10000000000')
            except ValueError:
                print('El codigo debe ser un numero')
            continue
        
    
    def get_id_veterinario(self):
        return self._id_veterinario
    

    def set_id_veterinario(self):
         while True:
            try:
                id_veterinario = int(input('Ingrese el ID del veterinario -> '))
                if (1 <= id_veterinario <= 10000000000):
                    self._id_veterinario = id_veterinario
                    break
                else:
                    print('El número debe estar entre 1 y 10000000000')
            except ValueError:
                print('El ID debe ser un numero')
            continue
    

    def get_codigo_mascota(self):
        return self._codigo_mascota
    

    def set_codigo_mascota(self):
         while True:
            try:
                codigo_mascota = int(input('Ingrese el codigo de la mascota -> '))
                if (1 <= codigo_mascota <= 10000000000):
                    self._codigo_mascota = codigo_mascota
                    break
                else:
                    print('El número debe estar entre 1 y 10000000000')
            except ValueError:
                print('El codigo de la mascota debe ser un numero')
            continue


    def capturar_datos_cita(self):
        self.set_codigo()
        self.set_fecha()
        self.set_hora()
        self.set_estado()
        self.set_id_servicio()
        self.set_id_veterinario()
        self.set_codigo_mascota()

    
    def registrar_cita(self):
        self.capturar_datos_cita()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('InsertarCita', [
                    self.get_codigo(),
                    self.get_fecha(),
                    self.get_hora(),
                    self.get_estado(),
                    self.get_id_servicio(),
                    self.get_id_veterinario(),
                    self.get_codigo_mascota()
                ])
                conexion.commit()
                print('Cita registrada correctamente...')
            except Exception as e:
                print(f'Error al registrar la cita: {e}')
                conexion.rollback()
            finally:
                cursor_cita.close()
                BaseDatos.desconectar()


    def consultar_cita_por_codigo(self, codigo=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('BuscarCitaPorCodigo', [codigo])
                for busqueda in cursor_cita.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        fecha_formateada = datetime.datetime.strptime(str(resultado[1]), '%Y-%m-%d').strftime('%d/%m/%Y')
                        hora_formateada = datetime.datetime.strptime(str(resultado[2]), '%H:%M:%S').strftime('%H:%M')
                        estado = resultado[3]
                        id_servicio = resultado[4]
                        id_veterinario = resultado[5]
                        codigo_mascota = resultado[6]
                        resultado = f'{resultado[0]}, {fecha_formateada}, {hora_formateada}, {estado}, {id_servicio}, {id_veterinario}, {codigo_mascota}'
                        print(resultado)
                        return True
                    else:
                        print('Cita no encontrada.')
                        return False
            except Exception as e:
                print(f'Error al buscar la cita: {e}')
   


    def consultar_cita_por_mascota(self, codigo_mascota = None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('BuscarCitaPorMascota', [codigo_mascota])
                for busqueda in cursor_cita.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        fecha_formateada = datetime.datetime.strptime(str(resultado[1]), '%Y-%m-%d').strftime('%d/%m/%Y')
                        hora_formateada = datetime.datetime.strptime(str(resultado[2]), '%H:%M:%S').strftime('%H:%M')
                        estado = resultado[3]
                        id_servicio = resultado[4]
                        id_veterinario = resultado[5]
                        codigo_mascota = resultado[6]
                        resultado = f'{resultado[0]}, {fecha_formateada}, {hora_formateada}, {estado}, {id_servicio}, {id_veterinario}, {codigo_mascota}'
                        print(resultado)
                        return True
                    else:
                        print('Cita no encontrada.')
                        return False
            except Exception as e:
                print(f'Error al buscar la cita: {e}')


    def consultar_cita_por_fecha(self, fecha = None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('BuscarCitaPorFecha', [fecha])
                for busqueda in cursor_cita.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        fecha_formateada = datetime.datetime.strptime(str(resultado[1]), '%Y-%m-%d').strftime('%d/%m/%Y')
                        hora_formateada = datetime.datetime.strptime(str(resultado[2]), '%H:%M:%S').strftime('%H:%M')
                        estado = resultado[3]
                        id_servicio = resultado[4]
                        id_veterinario = resultado[5]
                        codigo_mascota = resultado[6]
                        resultado = f'{resultado[0]}, {fecha_formateada}, {hora_formateada}, {estado}, {id_servicio}, {id_veterinario}, {codigo_mascota}'
                        print(resultado)
                        return True
                    else:
                        print('Cita no encontrada.')
                        return False
            except Exception as e:
                print(f'Error al buscar la cita: {e}')

    
    def consultar_citas(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('BuscarCitas')
                resultados = cursor_cita.stored_results()
                citas = []
                for resultado in resultados:
                    citas.extend(resultado.fetchall()) 
                if citas:
                    for cita in citas:
                        fecha_formateada = datetime.datetime.strptime(str(cita[1]), '%Y-%m-%d').strftime('%d/%m/%Y')
                        hora_formateada = datetime.datetime.strptime(str(cita[2]), '%H:%M:%S').strftime('%H:%M')
                        estado = cita[3]
                        id_servicio = cita[4]
                        id_veterinario = cita[5]
                        codigo_mascota = cita[6]
                        cita_linea = f'{cita[0]}, {fecha_formateada}, {hora_formateada}, {estado}, {id_servicio}, {id_veterinario}, {codigo_mascota}'
                        print(cita_linea)
                    return citas
                else:
                    print('No se encontraron citas.')
                    return None
            except Exception as e:
                print(f'Error al consultar las citas: {e}')
            finally:
                if conexion:
                    cursor_cita.close()
                    BaseDatos.desconectar()

    def actualizar_cita(self, codigo):
        conexion = BaseDatos.conectar()
        if self.consultar_cita_por_codigo(codigo):
            try:
                print('Esciba los nuevos datos de la cita')
                self.set_fecha()
                self.set_hora()
                self.set_estado()
                self.set_id_servicio()
                self.set_id_veterinario()
                self.set_codigo_mascota()
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('ActualizarCita', [
                    codigo,
                    self.get_fecha(),
                    self.get_hora(),
                    self.get_estado(),
                    self.get_id_servicio(),
                    self.get_id_veterinario(),
                    self.get_codigo_mascota()
                ])
                conexion.commit()
                print('Cita actualizada correctamente')
            except Exception as error:
                print(f'Error al actualizar la cita: {error}')
            finally:
                if conexion:
                    cursor_cita.close()
                    BaseDatos.desconectar()
        else:
            print('Cita no encontrada.')


    def eliminar_cita(self, codigo):
        conexion = BaseDatos.conectar()
        if self.consultar_cita_por_codigo(codigo):
            try:
                cursor_cita = conexion.cursor()
                cursor_cita.callproc('EliminarCita', [codigo])
                conexion.commit()
                print('Cita eliminada')
            except Exception as e:
                print(f'Error al eliminar la cita: {e}')
                conexion.rollback()
            finally:
                if conexion:
                    cursor_cita.close()
                    BaseDatos.desconectar()        
        else:
            print('Cita no encontrada')    

        