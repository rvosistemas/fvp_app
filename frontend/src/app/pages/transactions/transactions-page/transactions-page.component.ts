import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../services/api.service';
import { CommonModule } from '@angular/common';
import { TransactionItemComponent } from '../../../components/transaction-item/transaction-item.component';
import { forkJoin } from 'rxjs';

@Component({
  selector: 'app-transactions-page',
  standalone: true,
  imports: [CommonModule, TransactionItemComponent],
  templateUrl: './transactions-page.component.html',
})
export class TransactionsPageComponent implements OnInit {

  funds: any[] = [];
  transactions: any[] = [];

  constructor(private readonly apiService: ApiService) { }

  ngOnInit(): void {

    forkJoin({
      funds: this.apiService.getFunds(),
      transactions: this.apiService.getTransactions()
    }).subscribe({
      next: (result) => {
        this.funds = result.funds;
        this.transactions = result.transactions.map((transaction: { fund_id: any; }) => {
          const fund = this.funds.find(f => f.id === transaction.fund_id);
          return {
            ...transaction,
            fund_name: fund ? fund.name : 'Unknown Fund',
          };
        });
      },
      error: (error) => {
        console.error('Error fetching data:', error);
      }
    });
  }
}
