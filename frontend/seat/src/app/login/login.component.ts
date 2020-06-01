import { Component, OnInit } from '@angular/core';
import { NgForm,FormGroup} from '@angular/forms'
import {NgModule} from '@angular/core'
import { Router,ActivatedRoute} from '@angular/router';
import {LoginService} from '../login.service'

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(
    private router: Router, 
    private route: ActivatedRoute,
    private loginService:LoginService) { }
  email=""
  password=""
  ngOnInit() {
  }

  submitData(){
    const loginForm=new FormData();
    loginForm.append("email",this.email);
    loginForm.append("password",this.password);

    this.loginService.changeLoginStatus(loginForm)

    

  }

}
