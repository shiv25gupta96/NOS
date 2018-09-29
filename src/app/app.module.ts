//=========   MODULES   =======
import { BrowserModule } from '@angular/platform-browser';
import { NgModule, NO_ERRORS_SCHEMA } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MDBBootstrapModule } from 'angular-bootstrap-md';
import { FormsModule } from '@angular/forms';
import { RouteLinksModule } from './route-links.module';

//---------COMPONENTS =======
import { AppComponent } from './app.component';
import { HomepageComponent } from './homepage/homepage.component';
import { TournamentsComponent } from './tournaments/tournaments.component';

//==============    SERVICES
import { TournamentManagerService } from './services/tournament-manager.service';
import { Title } from '@angular/platform-browser';

@NgModule({
  declarations: [
    AppComponent,
    HomepageComponent,
    TournamentsComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MDBBootstrapModule.forRoot(),
    FormsModule,
    RouteLinksModule,
  ],
  providers: [Title, TournamentManagerService],
  bootstrap: [AppComponent],
  schemas: [ NO_ERRORS_SCHEMA ]
})
export class AppModule { }
