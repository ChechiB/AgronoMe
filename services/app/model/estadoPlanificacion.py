from app.model.modelImport import *

class EstadoPlanificacion(db.Model):
    __tablename__ = 'estado_planificacion'
    cod = db.Column('cod_estado_planificacion', Integer,primary_key = True,index = True)
    nombre = db.Column('nombre_estado_planificacion', String(80), nullable = False,  unique = True, index = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    nombreNomenclador = "estadoPlanificacion"  

    def __init__(self, nombre,isActiv):
        
        self.nombre = nombre
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        estadoPlanificacion = EstadoPlanificacion(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return estadoPlanificacion

    def to_json(self):
        return {
            'cod': self.cod,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }