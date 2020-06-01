import { NgModule } from '@angular/core';
import { Routes, RouterModule} from '@angular/router';
import {UploadDocComponent} from "./upload-doc/upload-doc.component"
const routes: Routes = [
  {path:'upload', component:UploadDocComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
