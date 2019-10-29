from app.model.modelImport import *

class Planificacion(db.Model):
    __tablename__ ='planificacion'
    cod = db.Column('cod_planificacion', Integer, primary_key = True, index = True)
    fchPlanificacion = db.Column('fch_planificacion', DateTime, default = datetime.datetime.now, index = True)
    comentarioPlanificacion = db.Column('comentario_planificacion', Text, nullable = True)
    codTipoPlanificacion = db.Column('fk_cod_tipo_planificacion',Integer,ForeignKey('tipo_planificacion.cod'),index = True)
    codEstadoPlanificacion = db.Column('fk_cod_estado_planificacion',Integer,ForeignKey('estado_planificacion.cod'),index = True)
    codFinca = db.Column('fk_cod_finca',Integer,ForeignKey('finca.codFinca'),index = True)
    codGrupoPlanificacion = db.Column('fk_cod_grupo_planificacion',Integer,ForeignKey('grupo_planificacion.cod'),index = True)
    #Relationships
    tipoPlanificacion = relationship('TipoPlanificacion',uselist = False)
    estadoPlanificacion = relationship('EstadoPlanificacion', uselist = False)
    grupoCuadroList = relationship('GrupoCuadro', uselist = True)
