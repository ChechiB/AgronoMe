import { Component, OnInit } from '@angular/core';
import { ActividadService } from '../../services/actividad/actividad.service';


@Component({
  selector: 'app-actividad-page',
  templateUrl: './actividad-page.component.html'
})
export class ActividadPageComponent implements OnInit {

  constructor( private _actividadService: ActividadService ){}


  ngOnInit() {
  }

}
