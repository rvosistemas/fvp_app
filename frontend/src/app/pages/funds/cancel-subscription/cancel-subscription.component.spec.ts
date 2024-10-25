import { ComponentFixture, TestBed } from '@angular/core/testing';
import { ApiService } from '../../../services/api.service';
import { CancelSubscriptionComponent } from './cancel-subscription.component';
import { of, throwError } from 'rxjs';
import Swal from 'sweetalert2';

describe('CancelSubscriptionComponent', () => {
  let component: CancelSubscriptionComponent;
  let fixture: ComponentFixture<CancelSubscriptionComponent>;
  let apiServiceSpy: jasmine.SpyObj<ApiService>;

  beforeEach(async () => {
    const spy = jasmine.createSpyObj('ApiService', ['getFunds', 'getActiveSubscriptions', 'cancelFundSubscription']);

    await TestBed.configureTestingModule({
      imports: [CancelSubscriptionComponent],
      providers: [
        { provide: ApiService, useValue: spy },
      ],
    }).compileComponents();

    fixture = TestBed.createComponent(CancelSubscriptionComponent);
    component = fixture.componentInstance;
    apiServiceSpy = TestBed.inject(ApiService) as jasmine.SpyObj<ApiService>;
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });

  describe('ngOnInit', () => {
    it('should load funds and active subscriptions successfully', () => {
      const mockFunds = [
        { id: '1', name: 'Fund 1' },
        { id: '2', name: 'Fund 2' }
      ];
      const mockSubscriptions = [
        { fund_id: '1' },
        { fund_id: '2' }
      ];

      apiServiceSpy.getFunds.and.returnValue(of(mockFunds));
      apiServiceSpy.getActiveSubscriptions.and.returnValue(of(mockSubscriptions));

      component.ngOnInit();

      expect(apiServiceSpy.getFunds).toHaveBeenCalled();
      expect(apiServiceSpy.getActiveSubscriptions).toHaveBeenCalled();
      expect(component.funds).toEqual(mockFunds);
      expect(component.activeSubscriptions).toEqual([
        { fund_id: '1', fund_name: 'Fund 1' },
        { fund_id: '2', fund_name: 'Fund 2' }
      ]);
    });

    it('should handle error during data fetching', () => {
      const mockError = { message: 'Error fetching data' };
      apiServiceSpy.getFunds.and.returnValue(throwError(() => mockError));
      apiServiceSpy.getActiveSubscriptions.and.returnValue(of([]));

      spyOn(console, 'error');

      component.ngOnInit();

      expect(console.error).toHaveBeenCalledWith('Error fetching data:', mockError);
    });
  });

  describe('cancel', () => {
    beforeEach(() => {
      component.selectedFundId = '1';
      component.funds = [{ id: '1', name: 'Fund 1' }];
      component.activeSubscriptions = [{ fund_id: '1', fund_name: 'Fund 1' }];
    });

    it('should cancel a subscription successfully', () => {
      const mockResponse = { success: true };

      apiServiceSpy.cancelFundSubscription.and.returnValue(of(mockResponse));

      spyOn(Swal, 'fire');

      component.cancel();

      expect(apiServiceSpy.cancelFundSubscription).toHaveBeenCalledWith('1');
      expect(Swal.fire).toHaveBeenCalledWith({
        title: 'Success!',
        text: 'Subscription to fund Fund 1 canceled successfully!',
        icon: 'success',
        confirmButtonText: 'OK',
      } as any);
      expect(component.activeSubscriptions.length).toBe(0);
    });

    it('should handle error during subscription cancellation', () => {
      const mockError = { message: 'Cancellation failed' };

      apiServiceSpy.cancelFundSubscription.and.returnValue(throwError(() => mockError));

      spyOn(Swal, 'fire');

      component.cancel();

      expect(apiServiceSpy.cancelFundSubscription).toHaveBeenCalledWith('1');
      expect(Swal.fire).toHaveBeenCalledWith({
        title: 'Error!',
        text: 'Cancellation failed: ' + mockError.message,
        icon: 'error',
        confirmButtonText: 'OK',
      } as any);
    });

    it('should not cancel a subscription if no fund is selected', () => {
      component.selectedFundId = '';  // Simular que no hay un fondo seleccionado
      spyOn(Swal, 'fire');

      component.cancel();

      expect(apiServiceSpy.cancelFundSubscription).not.toHaveBeenCalled();
      expect(Swal.fire).not.toHaveBeenCalled();
    });
  });

  describe('getFundName', () => {
    it('should return fund name if fund is found', () => {
      component.funds = [{ id: '1', name: 'Fund 1' }];
      const fundName = component.getFundName('1');
      expect(fundName).toBe('Fund 1');
    });

    it('should return "Unknown Fund" if fund is not found', () => {
      component.funds = [{ id: '1', name: 'Fund 1' }];
      const fundName = component.getFundName('non-existent-id');
      expect(fundName).toBe('Unknown Fund');
    });
  });
});
