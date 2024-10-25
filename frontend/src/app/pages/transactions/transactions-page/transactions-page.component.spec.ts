import { ComponentFixture, TestBed } from '@angular/core/testing';
import { TransactionsPageComponent } from './transactions-page.component';
import { ApiService } from '../../../services/api.service';
import { of, throwError } from 'rxjs';
import { CommonModule } from '@angular/common';
import { TransactionItemComponent } from '../../../components/transaction-item/transaction-item.component';

describe('TransactionsPageComponent', () => {
  let component: TransactionsPageComponent;
  let fixture: ComponentFixture<TransactionsPageComponent>;
  let apiServiceSpy: jasmine.SpyObj<ApiService>;

  beforeEach(async () => {
    const apiSpy = jasmine.createSpyObj('ApiService', ['getFunds', 'getTransactions']);

    await TestBed.configureTestingModule({
      imports: [CommonModule, TransactionItemComponent, TransactionsPageComponent],
      providers: [{ provide: ApiService, useValue: apiSpy }]
    }).compileComponents();

    fixture = TestBed.createComponent(TransactionsPageComponent);
    component = fixture.componentInstance;
    apiServiceSpy = TestBed.inject(ApiService) as jasmine.SpyObj<ApiService>;

    fixture.detectChanges(); // Aplicar la detección de cambios inicial
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });

  describe('ngOnInit', () => {
    it('should load funds and transactions successfully', () => {
      const mockFunds = [
        { id: '1', name: 'Fund 1' },
        { id: '2', name: 'Fund 2' }
      ];
      const mockTransactions = [
        { id: 't1', fund_id: '1', amount: 100 },
        { id: 't2', fund_id: '3', amount: 200 }
      ];

      apiServiceSpy.getFunds.and.returnValue(of(mockFunds));
      apiServiceSpy.getTransactions.and.returnValue(of(mockTransactions));

      component.ngOnInit();

      expect(apiServiceSpy.getFunds).toHaveBeenCalled();
      expect(apiServiceSpy.getTransactions).toHaveBeenCalled();
      expect(component.funds).toEqual(mockFunds);
      expect(component.transactions.length).toEqual(2);
      expect(component.transactions[0].fund_name).toBe('Fund 1');
      expect(component.transactions[1].fund_name).toBe('Unknown Fund');
    });

    it('should handle error when fetching funds or transactions', () => {
      const mockError = { message: 'Error fetching data' };
      spyOn(console, 'error');

      apiServiceSpy.getFunds.and.returnValue(throwError(() => mockError));
      apiServiceSpy.getTransactions.and.returnValue(throwError(() => mockError));

      component.ngOnInit();

      expect(apiServiceSpy.getFunds).toHaveBeenCalled();
      expect(apiServiceSpy.getTransactions).toHaveBeenCalled();
      expect(console.error).toHaveBeenCalledWith('Error fetching data:', mockError);
    });
  });
});
