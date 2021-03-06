import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ReportesService {

  constructor(private http: HttpClient) {
    console.log("ReportesService up and running");
  }

  /**
  * @param json json
  * @return Observable<string>
  *  
  * POST obtiene el dataset para realizar la grafica de barras de actividades
  */
  getReporteActividad(fechaDesde: any, fechaHasta: any, codLibroCampo: number): Observable<any> {
    let json = {
      fchDesde: String(fechaDesde.year + "-" + fechaDesde.month + "-" + fechaDesde.day + " 00:00"),
      fchHasta: String(fechaHasta.year + "-" + fechaHasta.month + "-" + fechaHasta.day + " 23:00"),
      codLibroCampo: codLibroCampo
    }
    return this.http.post<String>(`http://localhost:9001/api/reporte/actividadGfBar`, json);
  }

  /**
  * @param json json
  * @return Observable<string>
  *  
  * POST obtiene el dataset para realizar la grafica de torta de recomendaciones
  */
  getReporteRecomendacion(fechaDesde: any, fechaHasta: any, codLibroCampo: number): Observable<any> {
    let json = {
      fchDesde: String(fechaDesde.year + "-" + fechaDesde.month + "-" + fechaDesde.day + " 00:00"),
      fchHasta: String(fechaHasta.year + "-" + fechaHasta.month + "-" + fechaHasta.day + " 23:00"),
      codLibroCampo: codLibroCampo
    }
    return this.http.post<String>(`http://localhost:9001/api/reporte/recomendacionGfPie`, json);
  }

  /**
  * @param json json
  * @return Observable<string>
  *  
  * POST obtiene el dataset para realizar la grafica de barras de siembra
  */
  getReporteSiembra(fechaDesde: any, fechaHasta: any, codLibroCampo: number): Observable<any> {
    let json = {
      fchDesde: String(fechaDesde.year + "-" + fechaDesde.month + "-" + fechaDesde.day + " 00:00"),
      fchHasta: String(fechaHasta.year + "-" + fechaHasta.month + "-" + fechaHasta.day + " 23:00"),
      codActividad: 2,
      codParamComboDual: 50,
      codParamIndicador: 54,
      codOpcionOne: "plantin",
      codOpcionTwo: "semilla",
      codLibroCampo: codLibroCampo
    }
    return this.http.post<String>(`http://localhost:9001/api/reporte/actividadDualGfBar`, json);
  }

  /**
  * @param json json
  * @return Observable<string>
  *  
  * POST obtiene el dataset para realizar la grafica de barras de siembra
  */
  getReporteRiego(fechaDesde: any, fechaHasta: any, codLibroCampo: number): Observable<any> {
    let json = {
      fchDesde: String(fechaDesde.year + "-" + fechaDesde.month + "-" + fechaDesde.day + " 00:00"),
      fchHasta: String(fechaHasta.year + "-" + fechaHasta.month + "-" + fechaHasta.day + " 23:00"),
      codActividad: 1,
      codParamComboDual: 45,
      codParamIndicador: 48,
      codOpcionOne: "aspersion",
      codOpcionTwo: "goteo",
      codLibroCampo: codLibroCampo
    }
    return this.http.post<String>(`http://localhost:9001/api/reporte/actividadDualGfBar`, json);
  }

  /**
  * @param codFinca number 
  * @return Observable<string>
  *  
  * POST obtiene los libros de campo de la finca segun el codFinca enviado
  */
  getLibrosCampo(codFinca: number): Observable<any> {
    let json = {
      codFinca: codFinca
    }
    return this.http.post<string>(`http://localhost:9001/api/libroCampo`, json);
  }

}
