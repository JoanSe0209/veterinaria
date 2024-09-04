from conexion10 import BaseDatos
import re

class Producto:
    def __init__(
            self,
            codigo: int = None,
            nombre: str = None,
            descripcion: str = None,
            precio: float = None,
            stock: int = None
            ):
        self._codigo = codigo
        self._nombre = nombre
        self._descripcion = descripcion
        self._precio = precio
        self._stock = stock


#GET Y SET

    def get_codigo(self):
        return self._codigo
    

    def set_codigo(self):
        while True:
            try:
                codigo = int(input('Ingrese el codigo del producto -> '))
                if (1 <= codigo <= 10000000000):
                    self._codigo = codigo
                    break
                else:
                    print('El número debe estar entre 1 y 10000000000')
            except ValueError:
                print('El codigo debe ser un numero')
                continue


    def get_nombre(self):
        return self._nombre
    

    def set_nombre(self):
        while True:
            try:
                nombre = input('Ingrese el nombre del producto -> ')
                if len(nombre) > 1:
                    self._nombre = nombre
                    break
                else:
                    print('Nombre incorrecto, intentalo de nuevo')
            except KeyboardInterrupt:
                print('El usuario ha interrumpido la entrada de datos')
                continue

    
    def get_descripcion(self):
        return self._descripcion
    

    def set_descripcion(self):
        descripcion = input('Ingrese la descripción del producto -> ')
        self._descripcion = descripcion

    
    def get_precio(self):
        return self._precio
    

    def set_precio(self):
        while True:
            try:
                precio = float(input('Ingrese el precio del producto -> '))
                if (1 <= precio <= 2500000):
                    self._precio = precio
                    break 
                else:
                    print('El precio salio del rango permitido, intetalo de nuevo')
            except ValueError:
                print('El precio debe ser en numeros')
            except KeyboardInterrupt:
                print('El usuario ha cancelado el proceso')
            continue

    
    def get_stock(self):
        return self._stock
    

    def set_stock(self):
        stock = int(input('Ingrese el stock existente -> '))
        self._stock = stock 


    def capturar_datos_producto(self):
        self.set_codigo()
        self.set_nombre()
        self.set_descripcion()
        self.set_precio()
        self.set_stock()

    
    def registrar_producto(self):
        self.capturar_datos_producto()
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_producto = conexion.cursor()
                cursor_producto.callproc('InsertarProducto', [
                    self.get_codigo(),
                    self.get_nombre(),
                    self.get_descripcion(),
                    self.get_precio(),
                    self.get_stock()
                ])
                conexion.commit()
                print('Producto registrado correctamente...')
            except Exception as e:
                print(f'Error al registrar el producto: {e}')
                conexion.rollback()
            finally:
                cursor_producto.close()
                BaseDatos.desconectar()


    def consultar_producto_por_codigo(self, codigo=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_producto = conexion.cursor()
                cursor_producto.callproc('BuscarProductoPorCodigo', [codigo])
                for busqueda in cursor_producto.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        print('----RESULTADO----')
                        print(resultado)
                        print('\n')
                        return True
                    else:
                        print('Producto no encontrado')
                        return False
            except Exception as e:
                print(f'Error al buscar la mascota: {e}')
            finally:
                if conexion:
                    cursor_producto.close()
                    BaseDatos.desconectar()


    def consultar_productos(self):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_producto = conexion.cursor()
                cursor_producto.callproc('BuscarProductos')  
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


    def consultar_producto_por_nombre(self, nombre=None):
        conexion = BaseDatos.conectar()
        if conexion:
            try:
                cursor_producto = conexion.cursor()
                cursor_producto.callproc('BuscarProductoPorNombre', [nombre])
                for busqueda in cursor_producto.stored_results():
                    resultado = busqueda.fetchone()
                    if resultado:
                        print('----RESULTADO----')
                        print(resultado)
                        print('\n')
                        return True
                    else:
                        print('Producto no encontrado')
                        return False
            except Exception as e:
                print(f'Error al buscar la mascota: {e}')
            finally:
                if conexion:
                    cursor_producto.close()
                    BaseDatos.desconectar()


    def actualizar_producto(self, codigo):
        conexion = BaseDatos.conectar()
        if self.consultar_producto_por_codigo(codigo):
            try:
                print('Escriba los nuevos datos del producto: ')
                self.set_nombre()
                self.set_descripcion()
                self.set_precio()
                self.set_stock()
                cursor_producto = conexion.cursor()
                cursor_producto.callproc('ActualizarProducto', [
                    codigo,
                    self.get_nombre(),
                    self.get_descripcion(),
                    self.get_precio(),
                    self.get_stock(),
                ])
                conexion.commit()
                print('Producto actualizado correctamente.')
            except Exception as error:
                print(f'Error al actualizar el producto: {error}')
            finally:
                if conexion:
                    cursor_producto.close()
                    BaseDatos.desconectar()
        else:
            print('Producto no encontrada.')



    def eliminar_producto(self, codigo):
        conexion = BaseDatos.conectar()
        if self.consultar_producto_por_codigo(codigo):
            try:
                cursor_producto = conexion.cursor()
                cursor_producto.callproc('EliminarProducto', [codigo])
                conexion.commit()
                print('Producto eliminado')
            except Exception as e:
                print(f'Error al eliminar el producto: {e} ')
                conexion.rollback()
            finally:
                if conexion:
                    cursor_producto.close()
                    BaseDatos.desconectar()
        else:
            print('Producto no encontrado')


