class estudiante:
    def __init__(self,nombre,apellido,correo,cedula,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.cedula = cedula
        self.telefono = telefono 

    def ObtenerInformacion(self):
        return f'MI nombre es {self.nombre}  {self.apellido} con cedula {self.cedula} mi numero telefonico es {self.telefono} y mi correo es {self.correo}, soy estudiante de UNITECNAR.'