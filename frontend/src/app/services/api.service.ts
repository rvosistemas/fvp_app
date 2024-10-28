import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  // private readonly baseUrl = 'http://localhost:8000';
  private readonly baseUrl = 'http://ec2-44-204-78-240.compute-1.amazonaws.com:8000';

  constructor(private readonly http: HttpClient) { }

  getFunds(): Observable<any> {
    return this.http.get(`${this.baseUrl}/funds`);
  }

  subscribeToFund(fundId: string, amount: number, userBalance: number): Observable<any> {
    const body = { fund_id: fundId, amount: amount, user_balance: userBalance };
    return this.http.post(`${this.baseUrl}/funds/subscribe`, body);
  }

  getActiveSubscriptions(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/transactions/active`);
  }

  cancelFundSubscription(fundId: string): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/funds/cancel`, { fund_id: fundId });
  }

  getTransactions(): Observable<any> {
    return this.http.get(`${this.baseUrl}/transactions`);
  }
}
