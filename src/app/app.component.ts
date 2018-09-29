import { Component } from '@angular/core';
import { Title } from '@angular/platform-browser';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'NOS';

  public constructor(private titleService: Title){}

  ngOnInit(){
    this.titleService.setTitle('NOS');
  }
}
