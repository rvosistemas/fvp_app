import { provideHttpClient, HttpClient } from '@angular/common/http';
import { TestBed } from '@angular/core/testing';
import { ApiService } from './api.service';
import { of } from 'rxjs';

describe('ApiService', () => {
  let service: ApiService;
  let httpSpy: jasmine.SpyObj<HttpClient>;

  beforeEach(() => {
    const spy = jasmine.createSpyObj('HttpClient', ['get', 'post']);

    TestBed.configureTestingModule({
      providers: [
        ApiService,
        provideHttpClient(),
        { provide: HttpClient, useValue: spy }
      ]
    });

    service = TestBed.inject(ApiService);
    httpSpy = TestBed.inject(HttpClient) as jasmine.SpyObj<HttpClient>;
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });

  it('should retrieve funds from API via GET', () => {
    const mockFunds = [
      { id: '1', name: 'Fund 1', amount: 100 },
      { id: '2', name: 'Fund 2', amount: 200 }
    ];

    httpSpy.get.and.returnValue(of(mockFunds));

    service.getFunds().subscribe(funds => {
      expect(funds).toEqual(mockFunds);
    });

    expect(httpSpy.get.calls.count()).toEqual(1);
    expect(httpSpy.get.calls.mostRecent().args[0]).toBe('http://localhost:8000/funds');
  });

  it('should subscribe to a fund via POST', () => {
    const mockResponse = { success: true };
    const fundId = '1';
    const amount = 500;
    const userBalance = 1000;

    httpSpy.post.and.returnValue(of(mockResponse));

    service.subscribeToFund(fundId, amount, userBalance).subscribe(response => {
      expect(response).toEqual(mockResponse);
    });

    expect(httpSpy.post.calls.count()).withContext('one call').toEqual(1);
    expect(httpSpy.post.calls.mostRecent().args[0]).toBe('http://localhost:8000/funds/subscribe');
  });

  it('should retrieve active subscriptions via GET', () => {
    const mockSubscriptions = [
      { id: 'sub1', fund_id: '1', amount: 100 },
      { id: 'sub2', fund_id: '2', amount: 200 }
    ];

    httpSpy.get.and.returnValue(of(mockSubscriptions));

    service.getActiveSubscriptions().subscribe(subscriptions => {
      expect(subscriptions).toEqual(mockSubscriptions);
    });

    expect(httpSpy.get.calls.count()).withContext('one call').toEqual(1);
    expect(httpSpy.get.calls.mostRecent().args[0]).toBe('http://localhost:8000/transactions/active');
  });

  it('should cancel a fund subscription via POST', () => {
    const mockResponse = { success: true };
    const fundId = '1';

    httpSpy.post.and.returnValue(of(mockResponse));

    service.cancelFundSubscription(fundId).subscribe(response => {
      expect(response).toEqual(mockResponse);
    });

    expect(httpSpy.post.calls.count()).withContext('one call').toEqual(1);
    expect(httpSpy.post.calls.mostRecent().args[0]).toBe('http://localhost:8000/funds/cancel');
  });

  it('should retrieve transactions via GET', () => {
    const mockTransactions = [
      { id: 'trans1', amount: 100, type: 'deposit' },
      { id: 'trans2', amount: 200, type: 'withdraw' }
    ];

    httpSpy.get.and.returnValue(of(mockTransactions));

    service.getTransactions().subscribe(transactions => {
      expect(transactions).toEqual(mockTransactions);
    });

    expect(httpSpy.get.calls.count()).withContext('one call').toEqual(1);
    expect(httpSpy.get.calls.mostRecent().args[0]).toBe('http://localhost:8000/transactions');
  });
});
