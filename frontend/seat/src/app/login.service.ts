import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class LoginService {
  constructor(private httpClient:HttpClient) { }

  getDocumentsUrl="http://127.0.0.1:5000/documents"
  loginUrl="http://127.0.0.1:5000/login"


  changeLoginStatus(loginForm){
     return this.httpClient.post(this.loginUrl,loginForm)
    
  }

  getDocuments(){
    return this.httpClient.get(this.getDocumentsUrl)

  }
}
