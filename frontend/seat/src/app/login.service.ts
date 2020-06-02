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
  uploadDocUrl="http://127.0.0.1:5000/upload_unauthenticated_document"
  verificarDocumentoUrl="http://127.0.0.1:5000/authenticate_document"

  changeLoginStatus(loginForm){
     return this.httpClient.post(this.loginUrl,loginForm)
    
  }

  getDocuments(){
    return this.httpClient.get(this.getDocumentsUrl)

  }

  uploadDoc(uploadForm){
    return this.httpClient.post(this.uploadDocUrl,uploadForm)

  }
  verificarDocumento(verifyForm){
    return this.httpClient.post(this.verificarDocumentoUrl,verifyForm)

  }
}
