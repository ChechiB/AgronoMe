from app.repositorio.hlDb import saveEntidadSinCommit,Commit
from app.uses_cases.moduloConfiguracion.gestionarNomenclador import getNomencladoCod
from app.model.hlmodel import RecomendacionDetalle, RecomDetalleParam, Parametro
from app.repositorio.repositorioRegistrarActividad import selectActivDetalleCod
from app.repositorio.repositorioRegistrarRecomendacion import selectRecomenActiv, selectRecomCod
from app.api.helperApi.hlResponse import ResponseException, ResponseOk
from app.uses_cases.hlToDict import recomDetalleFullToDict, activDetalleToDict
def postRegistrarRecom(data,currentUser):
    try:
        codRecom = data.get('codRecomendacion')
        codActivDetalle = data.get('codActividadDetalle')
        obs = data.get('observacion')
        parametros = data.get('parametros')
        fch = data.get('fchRecomDetalle')
        
        recomendacion = getNomencladoCod('recomendacion',codRecom)
        activDetalle = selectActivDetalleCod(codActivDetalle)
        ##creacion del detalle recomendacion
        detalleRecom = RecomendacionDetalle(observacion = obs,fchRecomDetalle = fch)
        
        ##asociacion de recomendacion
        detalleRecom.recomendacion = recomendacion
        ##asociación de activ detalle 
        activDetalle.recomendacionDetalle = detalleRecom
        ##asociacion de usuario
        detalleRecom.usuario = currentUser

        for param in parametros:
            codParam = param.get('codParam')
            valor = param.get('valor')
            parametro = getNomencladoCod('parametro',codParam)

            recomDetalleParam = RecomDetalleParam(valor = valor )
            recomDetalleParam.param = parametro
            detalleRecom.paramList.append(recomDetalleParam)

        saveEntidadSinCommit(detalleRecom)  
        Commit()
        return ResponseOk()
    except Exception as e:
        return ResponseException(e)


def getRecomDetalle(codRecomDetalle):
    try:
        recomDetalle = selectRecomCod(codRecomDetalle)
        if not recomDetalle:
            raise Exception('N','No existe actividad detalle con código ' + str(codRecomDetalle))
        result = recomDetalleFullToDict(recomDetalle)
        return result
    except Exception as e:
        return ResponseException(e)

def recomendacionActividad(currentUser):
    ##sacar del usuario las fincas 
    actividadDetalleList = selectRecomenActiv() #pasarle el libro de campo
    dtoListActivSin = []
    dtoListActivRecom= []
    
    for actividadDetalle in actividadDetalleList:
        dtoAux=activDetalleToDict(actividadDetalle)

        dtoFinca = dict(codFinca=1,nombreFinca='3 Huert.JArcode')


        dtoAux['finca'] = dtoFinca

        codRecomDetalle = actividadDetalle.codRecomDetalle

        if actividadDetalle.codRecomDetalle == None:
            dtoListActivSin.append(dtoAux)
        else:   
            dtoAux['codRecomDetalle'] = codRecomDetalle
            dtoListActivRecom.append(dtoAux) 
    result= (dict(actvidadesArecomendar = dtoListActivSin, actividadesRecomendadas=dtoListActivRecom))
    return result




