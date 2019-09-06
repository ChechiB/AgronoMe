from app.model.modelImport import *
from app.model.hlmodel import Parametro,Opcion

class ParametroOpcion(db.Model):
    __tablename__ = 'parametro_opcion'
    isActiv = db.Column('is_activ', Boolean, nullable = False)
    codParametro = db.Column('fk_cod_parametro',Integer,ForeignKey('parametro.cod_parametro'),index = True, primary_key = True)
    codOpcion = db.Column('fk_cod_opcion',Integer,ForeignKey('opcion.cod_opcion'),index = True,  primary_key = True)
    #Agregar relationship hacia parametro
    
    #PK compuesta
    #__table_args__ = (
    #    PrimaryKeyConstraint(codParametro, codOpcion),
    #    {},
    #)
    
    def __init__(self,isActiv,parametro,opcion):
        print("En constructor parametro opcion")
        self.isActiv = isActiv
        self.parametro = parametro
        self.opcion = opcion
        print(self.parametro)
        print(self.opcion)

    parametro = relationship(Parametro,backref = "parametroOpcion")
    print("Paramtro relationship")
    
    opcion = relationship(Opcion,backref = "parametroOpcion")
    print("Opcion relationship")

   

    @staticmethod
    #def from_json(json):
    #    parametroOpcion = ParametroOpcion(
    #        isActiv=json.get('isActiv')
    #       )
    #    print(parametroOpcion.isActiv)
    #    return parametroOpcion

    def to_json(self):
        return {
            'isActiv': self.isActiv
        }