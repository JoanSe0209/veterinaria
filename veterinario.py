from usuario import Usuario

class Veterinario(Usuario):
    def __init__(self, id_usuario, nombre, apellido, ciudad, direccion, telefono, email, contrasena, especialidad, horario):
        super().__init__(id_usuario, nombre, apellido, ciudad, direccion, telefono, email, contrasena)
        self.__especialidad = especialidad
        self.__horario = horario


    def iniciar_sesion(self):
        print(f"Veterinario {self.get_nombre()} {self.get_apellido()} ha iniciado sesión.")


    def ver_calendario(self):
        print(f"Mostrando calendario para el veterinario {self.get_nombre()}.")


    def actualizar_disponibilidad(self, nuevo_horario):
        self.__horario = nuevo_horario
        print(f"Disponibilidad actualizada a {self.__horario} para el veterinario {self.get_nombre()}.")


    def registrar(self):
        print(f"Registrando al veterinario {self.get_nombre()} en la base de datos.")


    def get_especialidad(self):
        return self.__especialidad


    def set_especialidad(self, especialidad):
        self.__especialidad = especialidad


    def get_horario(self):
        return self.__horario


    def set_horario(self, horario):
        self.__horario = horario
