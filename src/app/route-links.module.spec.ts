import { RouteLinksModule } from './route-links.module';

describe('RouteLinksModule', () => {
  let routeLinksModule: RouteLinksModule;

  beforeEach(() => {
    routeLinksModule = new RouteLinksModule();
  });

  it('should create an instance', () => {
    expect(routeLinksModule).toBeTruthy();
  });
});
