import { ComponentFixture, TestBed } from '@angular/core/testing';
import { FundItemComponent } from './fund-item.component';

describe('FundItemComponent', () => {
  let component: FundItemComponent;
  let fixture: ComponentFixture<FundItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FundItemComponent]
    })
      .compileComponents();

    fixture = TestBed.createComponent(FundItemComponent);
    component = fixture.componentInstance;
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should display the fund input correctly', () => {
    const mockFund = {
      name: 'Growth Fund',
      minimum_amount: 1000,
      category: 'Growth'
    };

    component.fund = mockFund;

    fixture.detectChanges();

    expect(component.fund).toEqual(mockFund);
  });
});
