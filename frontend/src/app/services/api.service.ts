import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private readonly baseUrl = 'http://localhost:8000';

  constructor(private readonly http: HttpClient) { }

  getFunds(): Observable<any> {
    return this.http.get(`${this.baseUrl}/funds`);
  }

  subscribeToFund(fundId: string, amount: number, userBalance: number): Observable<any> {
    const body = { fund_id: fundId, amount: amount, user_balance: userBalance };
    return this.http.post(`${this.baseUrl}/funds/subscribe`, body);
  }

  cancelFundSubscription(fundId: string): Observable<any> {
    const body = { fund_id: fundId };
    return this.http.post(`${this.baseUrl}/funds/cancel`, body);
  }

  getTransactions(): Observable<any> {
    return this.http.get(`${this.baseUrl}/transactions`);
  }
}
