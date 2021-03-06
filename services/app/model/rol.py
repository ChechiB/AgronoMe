from app.model.modelImport import *

class Rol(db.Model):
    __tablename__ = 'rol'
    cod = db.Column('cod_rol',  Integer,primary_key = True,index = True)
    nombre = db.Column('nombre_rol', String(80), nullable = False,  unique = True,index = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)

    nombreNomenclador = "rol"


    def __init__(self, nombre, isActiv):
        self.nombre = nombre
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        rol = Rol(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return rol

    def to_json(self):
        return {
            'cod': self.cod,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }
    
    def to_json_simple(self):
        return{
            'cod': self.cod,
            'nombre': self.nombre
        }