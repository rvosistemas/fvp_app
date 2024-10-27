import { ComponentFixture, TestBed } from '@angular/core/testing';
import { TransactionItemComponent } from './transaction-item.component';

describe('TransactionItemComponent', () => {
  let component: TransactionItemComponent;
  let fixture: ComponentFixture<TransactionItemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TransactionItemComponent]
    }).compileComponents();

    fixture = TestBed.createComponent(TransactionItemComponent);
    component = fixture.componentInstance;
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should display transaction data correctly', () => {
    const mockTransaction = {
      type: 'Deposit',
      amount: 200,
      date: '2024-10-25'
    };

    component.transaction = mockTransaction;

    fixture.detectChanges();

    expect(component.transaction).toEqual(mockTransaction);

    const compiled = fixture.nativeElement;
    expect(compiled.querySelector('li').textContent).toContain('Deposit');
    expect(compiled.querySelector('li').textContent).toContain('200');
    expect(compiled.querySelector('li').textContent).toContain('2024-10-25');
  });
});
