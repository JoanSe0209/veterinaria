from usuario import Usuario

class Administrador(Usuario):
    def __init__(self, id_usuario, nombre, apellido, ciudad, direccion, telefono, email, contrasena, cargo, fecha_ingreso):
        super().__init__(id_usuario, nombre, apellido, ciudad, direccion, telefono, email, contrasena)
        self.__cargo = cargo
        self.__fecha_ingreso = fecha_ingreso

    def iniciar_sesion(self):
        print(f"Administrador {self.get_nombre()} {self.get_apellido()} ha iniciado sesión.")


    def get_cargo(self):
        return self.__cargo


    def set_cargo(self, cargo):
        self.__cargo = cargo


    def get_fecha_ingreso(self):
        return self.__fecha_ingreso


    def set_fecha_ingreso(self, fecha_ingreso):
        self.__fecha_ingreso = fecha_ingreso
