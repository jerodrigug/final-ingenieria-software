import { Component, OnInit } from '@angular/core';
import { NgForm,FormGroup} from '@angular/forms'
import {NgModule} from '@angular/core'
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  constructor(private httclient:HttpClient) { }

  nombre=""
  apellido=""
  idnumber=""
  email=""
  isAdmin:any
  nit=""
  contrasena=""

  uploadForm: FormGroup; 
  serverUrlCitizen="http://127.0.0.1:5000/register_user"
  serverUrlSchool="http://127.0.0.1:5000/register_driving_school"

  ngOnInit() {
  }

  submitData(){
    console.log(this.contrasena+" "+this.isAdmin)

    const registerSchoolForm=new FormData();
    registerSchoolForm.append("nit_driving_school",this.nit);
    registerSchoolForm.append("name",this.nombre);

    this.httclient.post(this.serverUrlSchool,registerSchoolForm).subscribe(
      (res)=> console.log(res),
      (err)=> console.log(err)
    )


    const registerUserForm = new FormData();
    registerUserForm.append("id_number",this.idnumber);
    registerUserForm.append("name",this.nombre);
    registerUserForm.append("last_name",this.apellido);
    registerUserForm.append("email",this.email);
    registerUserForm.append("password",this.contrasena);
    registerUserForm.append("is_admin",this.isAdmin);
    registerUserForm.append("nit_driving_school",this.idnumber);

    this.httclient.post(this.serverUrlCitizen,registerUserForm).subscribe(
      (res)=> console.log(res),
      (err)=> console.log(err)
    )

  }




}
