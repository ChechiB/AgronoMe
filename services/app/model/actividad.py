from app.model.modelImport import *

class Actividad(db.Model):
    __tablename__ = 'actividad'
    codActividad = db.Column('cod_actividad',Integer,primary_key = True,index = True)
    nombreActividad = db.Column('nombre_actividad', String(32), nullable = False, unique = True)
    isActiv = db.Column('is_activ', Boolean, nullable = False)

    #Relaciones OneToMany lado Many
    actividadParametro = relationship("ActividadParametro")


    def __init__(self, nombreActividad, isActiv):
        self.nombreActividad = nombreActividad
        self.isActiv = isActiv

    @staticmethod
    def from_json(json):
        actividad = Actividad(
            nombreActividad=json.get('nombreActividad'),
            isActiv=json.get('isActiv')
            )
        return actividad

    def to_json(self):
        return {
            'codActividad': self.codActividad,
            'nombreActividad': self.nombreActividad,
            'isActiv': self.isActiv
        }