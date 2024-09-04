from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, id_usuario, nombre, apellido, ciudad, direccion, telefono, email, contrasena):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__ciudad = ciudad
        self.__direccion = direccion
        self.__telefono = telefono
        self.__email = email
        self.__contrasena = contrasena

    @abstractmethod
    def iniciar_sesion(self):
        pass


    def get_id_usuario(self):
        return self.__id_usuario


    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario


    def get_nombre(self):
        return self.__nombre


    def set_nombre(self, nombre):
        self.__nombre = nombre


    def get_apellido(self):
        return self.__apellido


    def set_apellido(self, apellido):
        self.__apellido = apellido


    def get_ciudad(self):
        return self.__ciudad


    def set_ciudad(self, ciudad):
        self.__ciudad = ciudad


    def get_direccion(self):
        return self.__direccion


    def set_direccion(self, direccion):
        self.__direccion = direccion


    def get_telefono(self):
        return self.__telefono


    def set_telefono(self, telefono):
        self.__telefono = telefono


    def get_email(self):
        return self.__email


    def set_email(self, email):
        self.__email = email


    def get_contrasena(self):
        return self.__contrasena


    def set_contrasena(self, contrasena):
        self.__contrasena = contrasena
