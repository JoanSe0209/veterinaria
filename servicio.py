from conexion10 import BaseDatos
import re

class Servicio:
    def __init__(
            self,
            codigo: int = None,
            nombre: str = None,
            descripcion: str = None,
            precio: float = None):
        self._codigo = codigo
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio

#GET Y SET 

    def get_codigo(self):
        return self._codigo
    

    def set_codigo(self):
        while True:
            try:
                codigo = int(input('Escriba el codigo del servicio -> '))
                if (1 <= codigo <= 1000000000):
                    self._codigo = codigo
                    break
                else:
                    print('El número debe estar entre 1 y 1000000000')
            except ValueError:
                print('El código debe ser un número.')
            except KeyboardInterrupt:
                print('El usuario ha cancelado la entrada de datos.')
                continue
        
    
    def get_nombre(self):
        return self._nombre
    

    def set_nombre(self):
        while True:
            try:
                nombre = input('Escriba el nombre del servicio -> ')
                if 3 < len(nombre) <= 255:
                    self._nombre = nombre
                    break
                else:
                    print('Intentalo de nuevo...')
            except ValueError:
                print('Solo se admite texto')
                continue

    
    def get_descripcion(self):
        return self._descripcion
    

    def set_descripcion(self):
        descripcion = input('Ingrese la descripción del servicio -> ')
        self._descripcion = descripcion
    

    def get_precio(self):
        return self._precio
    

    def set_precio(self):
        while True:
            try:
                precio = float(input('Ingrese el precio del servicio -> '))
                if (20000 <= precio <= 15000000):
                    self._precio = precio
                    break 
                else:
                    print('El precio salio del rango permitido, intetalo de nuevo')
            except ValueError:
                print('El precio debe ser en numeros')
            except KeyboardInterrupt:
                print('El usuario ha cancelado el proceso')
            continue

    def capturar_datos_servicio(self):
        self.set_codigo()
        self.set_nombre()
        self.set_descripcion()
        self.set_precio()

    
    def registrar_servicio(self):
        self.capturar_datos_servicio()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('InsertarServicio', [
                    self.get_codigo(),
                    self.get_nombre(),
                    self.get_descripcion(),
                    self.get_precio()
                ])
                conexion.commit()
                print('Servicio registrado correctamente...')
            except Exception as e:
                print(f'Error al registrar el servicio: {e}')
                conexion.rollback()
                BaseDatos.desconectar()

    
    def consultar_servicio_por_codigo(self, codigo=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('BuscarServicioPorCodigo', [codigo])
                for busqueda in cursor_servicio.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        print('----RESULTADO----')
                        print(resultado)
                        print('\n')
                        return True
                    else:
                        print('Servicio no encontrado...')
                        return False
            except Exception as e:
                print(f'Error al buscar el servicio: {e}')
            finally:
                if conexion:
                    cursor_servicio.close()
                    BaseDatos.desconectar()

    
    def consultar_servicio_por_nombre(self, nombre=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('BuscarServicioPorNombre', [nombre])
                for busqueda in cursor_servicio.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        print('----RESULTADO----')
                        print(resultado)
                        print('\n')
                        return True
                    else:
                        print('Servicio no encontrado...')
                        return False
            except Exception as e:
                print(f'Error al buscar el servicio: {e}')
            finally:
                if conexion:
                    cursor_servicio.close()
                    BaseDatos.desconectar()

    
    def colsultar_todos_los_servicios(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_producto = conexion.cursor()
                cursor_producto.callproc('BuscarServicios')  
                resultados = cursor_producto.stored_results()  
                productos = [] 
                for resultado in resultados:
                    productos.extend(resultado.fetchall()) 
                if productos:
                    print('----RESULTADOS----')
                    for producto in productos:
                        print(producto)
                    print('\n')
                    return productos
                else:
                    print('No se encontraron productos')
                    return None
            except Exception as e:
                print(f'Error al consultar los productos: {e}')
            finally:
                if conexion:
                    cursor_producto.close()
                    BaseDatos.desconectar()

    
    def actualizar_servicio(self, codigo):
        conexion = BaseDatos.conectar()
        if self.consultar_servicio_por_codigo(codigo):
            try:
                print('Escriba los nuevos datos del servicio: ')
                self.set_nombre()
                self.set_descripcion()
                self.set_precio()
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('ActualizarServicio', [codigo,
                    self.get_nombre(),
                    self.get_descripcion(),
                    self.get_precio(),
                    ])
                conexion.commit()
                print('Servicio actualizado correctamente.')
            except Exception as error:
                print(f'Error al actualizar el servicio: {error}')
            finally:
                if conexion:
                    cursor_servicio.close()
                    BaseDatos.desconectar
        else:
            print('Servicio no encontrado...')

    
    def eliminar_servicio(self, codigo):
        conexion = BaseDatos.conectar()
        if self.consultar_servicio_por_codigo(codigo):
            try:
                cursor_servicio = conexion.cursor()
                cursor_servicio.callproc('EliminarServicio', [codigo])
                conexion.commit()
                print('Servicio eliminado')
            except Exception as e:
                print(f'Error al eliminar el servicio: {e}')
                conexion.rollback()
            finally:
                if conexion:
                    cursor_servicio.close()
                    BaseDatos.desconectar()
        else:
            print('Servicio no encontrado')