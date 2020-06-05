import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class LoginService {
  constructor(private httpClient:HttpClient) { }

  getDocumentsUrl="http://ec2-100-26-223-58.compute-1.amazonaws.com/documents"
  loginUrl="http://ec2-100-26-223-58.compute-1.amazonaws.com//login"
  uploadDocUrl="http://ec2-100-26-223-58.compute-1.amazonaws.com//upload_unauthenticated_document"
  verificarDocumentoUrl="http://ec2-100-26-223-58.compute-1.amazonaws.com//authenticate_document"

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
