from app.extensions import db
from app.model.hlmodel import ActividadDetalle, ActivDetalleParam, Parametro

def selectActivDetalle(): 
    objetos = ActividadDetalle.query.filter(ActividadDetalle.isEliminado==False)
    return  objetos 

def selectActivDetalleCod(codActivDetalle):
    objeto = ActividadDetalle.query.filter(ActividadDetalle.codActivDetalle == codActivDetalle).first()
    return objeto

def selectActivDetalleParm(codActivDetalle,codParam):
    activDetalle = ActividadDetalle.query.filter(ActividadDetalle.codActivDetalle==codActivDetalle).first()
    parametro = Parametro.query.filter(Parametro.cod == codParam).first()

    activDetalleParam = ActivDetalleParam.query.filter(ActivDetalleParam.param==parametro).filter(ActivDetalleParam.activDetalle==activDetalle).first()
 
    return activDetalleParam