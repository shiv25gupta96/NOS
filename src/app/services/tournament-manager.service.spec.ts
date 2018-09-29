import { TestBed, inject } from '@angular/core/testing';

import { TournamentManagerService } from './tournament-manager.service';

describe('TournamentManagerService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [TournamentManagerService]
    });
  });

  it('should be created', inject([TournamentManagerService], (service: TournamentManagerService) => {
    expect(service).toBeTruthy();
  }));
});
