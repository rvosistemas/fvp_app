import { ComponentFixture, TestBed } from '@angular/core/testing';
import { of, throwError } from 'rxjs';
import { ApiService } from '../../../services/api.service';
import { FundsPageComponent } from './funds-page.component';
import { FundItemComponent } from '../../../components/fund-item/fund-item.component';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

describe('FundsPageComponent', () => {
  let component: FundsPageComponent;
  let fixture: ComponentFixture<FundsPageComponent>;
  let apiServiceSpy: jasmine.SpyObj<ApiService>;

  beforeEach(async () => {
    const spy = jasmine.createSpyObj('ApiService', ['getFunds']);

    await TestBed.configureTestingModule({
      imports: [CommonModule, FundItemComponent, RouterLink, FundsPageComponent],
      providers: [
        { provide: ApiService, useValue: spy }
      ]
    }).compileComponents();

    fixture = TestBed.createComponent(FundsPageComponent);
    component = fixture.componentInstance;
    apiServiceSpy = TestBed.inject(ApiService) as jasmine.SpyObj<ApiService>;
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
  });
});
