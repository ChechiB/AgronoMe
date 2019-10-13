import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class SeguridadService {

  constructor(private http: HttpClient) {
    console.log("SeguridadService up and running");
  }

  /**
  * @param tipoNomenclador string
  * @return Observable<Object>
  *  
  * Devuelve todos los nomencladores creados del tipo enviado por parámetro
  */
  getListaNomencladores(tipoNomenclador: string): Observable<String> {
    return this.http.get<String>(`http://localhost:9001/api/configuracion/nomenclador/${tipoNomenclador}`);
  }

  /**
  * @param tipoNomenclador string
  * @param isActiv boolean
  * @return Observable<Object>
  *  
  * Devuelve todos los nomencladores activos creados del tipo enviado por parámetro
  */
  getListaNomencladoresConFiltro(tipoNomenclador: string, isActiv: boolean): Observable<String> {
    let filtroJson = {
      "filtros":
      {
        "isActiv": isActiv
      }
    }

    return this.http.post<String>(`http://localhost:9001/api/configuracion/nomenclador/${tipoNomenclador}`, filtroJson);
  }

  /**
  * @param form form
  *  
  * Devuelve todos los nomencladores activos creados del tipo enviado por parámetro
  */
  postUsuario(json: any): Observable<String> {

    return this.http.post<String>(`http://localhost:9001/api/users`, json);
  }

  /**
  * @return List Observable<Object>
  *  
  * Devuelve todos los usuarios
  */
  getUsuarios(): Observable<String> {

    return this.http.get<String>(`http://localhost:9001/api/users`);
  }

  /**
  * @param cod string
  * @return Observable<Object>
  *  
  * Devuelve los datos de un usuario segun su cod
  */
  getUsuario(cod: string): Observable<String> {

    return this.http.get<String>(`http://localhost:9001/api/users/${cod}`);
  }

  /**
  * @param cod string
  *  
  * Actualiza los datos de un usuario
  */
  putUsuario(cod:string,json: any): Observable<String> {

    return this.http.put<String>(`http://localhost:9001/api/users//${cod}`, json);
  }
}
