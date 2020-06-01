import { Component } from '@angular/core';
import {LoginService} from "./login.service"
import { Observable } from 'rxjs';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'seat';
  login=false
  register=false
  hidehome=false
  loginCorrect:any

  constructor(private loginService:LoginService){}

  ngOnInit() {
  
  }



  registerfun(){
    this.register=true
    this.hidehome=true
  }
}
