import { Component, OnInit } from '@angular/core';
import {LoginService} from "../login.service"
import { Observable } from 'rxjs';
@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  title = 'seat';
  login=false
  register=false
  hidehome=false
  loginData:any

  email=""
  password=""

  loginCorrect=false
  upload=false

  documentMetadata:any

  constructor(private loginService:LoginService){}

  ngOnInit() {
  
  }

  loginfun(){
    this.login=true
    this.hidehome=true

  }

  registerfun(){
    this.register=true
    this.hidehome=true
  }

  submitLoginData(){
    const loginForm=new FormData();
    loginForm.append("email",this.email);
    loginForm.append("password",this.password);

    this.loginService.changeLoginStatus(loginForm).subscribe(
      (res)=> {
        this.loginData=res
        this.loginCorrect=true
        this.login=false
        this.upload=true
        this.loginService.getDocuments().subscribe(

          (res)=> {
            console.log(res)
            this.documentMetadata=res
          },
          (err)=> console.log(err)

        )

      },
      (err)=>console.log(err)
    )

  }

}
