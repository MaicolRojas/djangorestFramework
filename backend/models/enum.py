from enum import Enum

class Perfil(Enum):
    
    AD = "ADMINISTRADOR"
    VEN = "VENDEDOR"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)
    
class Estado(Enum):
    
    AC = "ACTIVADO"
    DES = "DESACTIVADO"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)
    
class Pago(Enum):
    
    EF = "EFECTVO"
    OT = "OTRO METODO DE PAGO"

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)