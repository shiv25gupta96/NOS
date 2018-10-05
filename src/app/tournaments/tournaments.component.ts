import { Component, OnInit } from '@angular/core';
import { TournamentManagerService } from '../services/tournament-manager.service';
import { Title } from '@angular/platform-browser';
// import { NgbModule } from '@ng-bootstrap/ng-bootstrap';

// import * as tourn from '../data/tournament.json';

@Component({
  selector: 'app-tournaments',
  templateUrl: './tournaments.component.html',
  styleUrls: ['./tournaments.component.scss']
})
export class TournamentsComponent implements OnInit {

  // Accounts: Object[] = tourn;
  tournaments: Object[];
  constructor(public tourManager: TournamentManagerService, private titleService: Title) { }

  ngOnInit() {
    this.titleService.setTitle("Tournaments");
    this.getTournaments();
  }

  getTournaments(){
    this.tournaments = this.tourManager.getAllTournaments();
    console.log(this.tournaments);
  }

}
