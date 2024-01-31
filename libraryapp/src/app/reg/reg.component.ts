import { Component } from '@angular/core';
import { ApicallService } from '../apicall.service';
@Component({
  selector: 'app-reg',
  templateUrl: './reg.component.html',
  styleUrls: ['./reg.component.css']
})
export class RegComponent {
  constructor(private regapi:ApicallService){}
  data={
    'username':'',
    'password':'',
    }

  onsubmit(){
    console.log(this.data);
    this.regapi.register(this.data).subscribe((res)=>
    {console.log(res);})
  }
}
