import { Injectable } from '@angular/core';
import { Tournaments } from '../data/tournamentsData';

@Injectable({
  providedIn: 'root'
})
export class TournamentManagerService {

  tournaments: Object[] = Tournaments;

  constructor() { }

  getAllTournaments(): Object[]{
    return this.tournaments;
  }

  getTournamentById(id): Object{
    return this.tournaments.find(tournament => tournament["unique id"] == id);
  }
}
