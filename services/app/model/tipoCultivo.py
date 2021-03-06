from app.model.modelImport import *

class TipoCultivo(db.Model):
    __tablename__ = 'tipo_cultivo'
    cod = db.Column('cod_tipo_cultivo',Integer,primary_key = True,index = True)
    nombre = db.Column('nombre_tipo_cultivo', String(80), nullable = False, unique = True,index = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    nombreNomenclador = "tipoCultivo"

    def __init__(self, nombre, isActiv):
        self.nombre = nombre
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        tipoCultivo = TipoCultivo(
            nombre=json.get('nombre'),
            isActiv=json.get('isActiv')
            )
        return tipoCultivo

    def to_json(self):
        return {
            'cod': self.cod,
            'tipoNomenclador': self.nombreNomenclador,
            'nombre': self.nombre,
            'isActiv': self.isActiv
        }