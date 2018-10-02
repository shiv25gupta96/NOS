import { Injectable } from '@angular/core';
import { Accounts } from '../data/tournamentsData';

@Injectable({
  providedIn: 'root'
})
export class TournamentManagerService {

  tournaments: Object[] = Accounts;

  constructor() { }

  getAllTournaments(): Object[]{
    return this.tournaments;
  }

  getTournamentById(id): Object{
    return this.tournaments.find(tournament => tournament["unique id"] == id);
  }
}
