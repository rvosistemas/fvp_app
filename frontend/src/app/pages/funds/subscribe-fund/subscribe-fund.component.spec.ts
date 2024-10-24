import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SubscribeFundComponent } from './subscribe-fund.component';

describe('SubscribeFundComponent', () => {
  let component: SubscribeFundComponent;
  let fixture: ComponentFixture<SubscribeFundComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SubscribeFundComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SubscribeFundComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
