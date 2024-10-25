import { ComponentFixture, TestBed } from '@angular/core/testing';
import { SubscribeFundComponent } from './subscribe-fund.component';
import { ApiService } from '../../../services/api.service';
import { of, throwError } from 'rxjs';
import Swal from 'sweetalert2';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

describe('SubscribeFundComponent', () => {
  let component: SubscribeFundComponent;
  let fixture: ComponentFixture<SubscribeFundComponent>;
  let apiServiceSpy: jasmine.SpyObj<ApiService>;

  beforeEach(() => {
    const apiSpy = jasmine.createSpyObj('ApiService', ['getFunds', 'subscribeToFund']);

    // Simular valores de retorno para evitar undefined
    apiSpy.getFunds.and.returnValue(of([]));
    apiSpy.subscribeToFund.and.returnValue(of({ success: true }));

    TestBed.configureTestingModule({
      imports: [FormsModule, CommonModule, RouterLink, SubscribeFundComponent],
      providers: [{ provide: ApiService, useValue: apiSpy }]
    }).compileComponents();

    fixture = TestBed.createComponent(SubscribeFundComponent);
    component = fixture.componentInstance;
    apiServiceSpy = TestBed.inject(ApiService) as jasmine.SpyObj<ApiService>;

    fixture.detectChanges();
  });

  it('should create the component', () => {
    expect(component).toBeTruthy();
  });

  describe('ngOnInit', () => {
    it('should load funds successfully', () => {
      const mockFunds = [
        { id: '1', name: 'Fund 1', amount: 100 },
        { id: '2', name: 'Fund 2', amount: 200 }
      ];
      apiServiceSpy.getFunds.and.returnValue(of(mockFunds));

      component.ngOnInit();

      expect(apiServiceSpy.getFunds).toHaveBeenCalled();
      expect(component.funds).toEqual(mockFunds);
    });

    it('should handle error when fetching funds', () => {
      const mockError = { message: 'Error fetching funds' };
      spyOn(console, 'error');

      apiServiceSpy.getFunds.and.returnValue(throwError(() => mockError));

      component.ngOnInit();

      expect(apiServiceSpy.getFunds).toHaveBeenCalled();
      expect(console.error).toHaveBeenCalledWith('Error fetching funds:', mockError);
    });

    it('should set default user balance from localStorage or use default value', () => {
      const getItemSpy = spyOn(localStorage, 'getItem').and.callFake((key) => {
        return key === 'userBalance' ? null : '1000';

        component.ngOnInit();
        expect(component.userBalance).toBe(500000);

        getItemSpy.and.returnValue('1000');
        component.ngOnInit();
        expect(component.userBalance).toBe(1000);
      });


    });

    describe('subscribe', () => {
      beforeEach(() => {
        spyOn(Swal, 'fire');
        spyOn(localStorage, 'setItem');
      });

      it('should show validation errors when form is invalid', () => {
        component.selectedFundId = '';
        component.amount = 0;
        component.subscribe();
        expect(component.showValidationErrors).toBeTrue();
      });

      it('should subscribe to a fund successfully', () => {
        const mockResponse = { success: true };
        component.selectedFundId = '1';
        component.amount = 100;
        component.userBalance = 1000;

        apiServiceSpy.subscribeToFund.and.returnValue(of(mockResponse));

        component.subscribe();

        expect(apiServiceSpy.subscribeToFund).toHaveBeenCalledWith('1', 100, 1000);
        expect(component.userBalance).toBe(900);
        expect(localStorage.setItem).toHaveBeenCalledWith('userBalance', '900');
        expect(Swal.fire).toHaveBeenCalledWith({
          icon: 'success',
          title: 'Subscribed!',
          text: `Subscribed to fund 1 successfully!`,
        } as any);
      });

      it('should handle error when subscribing to a fund', () => {
        const mockError = { message: 'Subscription failed' };
        component.selectedFundId = '1';
        component.amount = 100;
        component.userBalance = 1000;

        apiServiceSpy.subscribeToFund.and.returnValue(throwError(() => mockError));

        component.subscribe();

        expect(Swal.fire).toHaveBeenCalledWith({
          icon: 'error',
          title: 'Subscription failed',
          text: `Subscription failed: ${mockError.message}`,
        } as any);
      });

      it('should display error message when response has an error', () => {
        const mockResponse = { error: 'Fund not available' };
        component.selectedFundId = '1';
        component.amount = 100;
        component.userBalance = 1000;

        apiServiceSpy.subscribeToFund.and.returnValue(of(mockResponse));

        component.subscribe();

        expect(Swal.fire).toHaveBeenCalledWith({
          icon: 'error',
          title: 'Subscription failed',
          text: 'Fund not available',
        } as any);
      });
    });
  });

});
