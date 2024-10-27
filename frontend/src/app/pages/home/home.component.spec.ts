import { ActivatedRoute, RouterModule } from '@angular/router';
import { of } from 'rxjs';
import { HomeComponent } from './home.component';
import { ComponentFixture, TestBed } from '@angular/core/testing';

describe('HomeComponent', () => {
  let component: HomeComponent;
  let fixture: ComponentFixture<HomeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [RouterModule, HomeComponent],
      providers: [
        {
          provide: ActivatedRoute,
          useValue: {
            params: of({})
          }
        }
      ]
    }).compileComponents();

    fixture = TestBed.createComponent(HomeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create the HomeComponent', () => {
    expect(component).toBeTruthy();
  });
});
