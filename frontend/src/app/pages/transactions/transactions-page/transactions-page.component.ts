import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../services/api.service';
import { CommonModule } from '@angular/common';
import { TransactionItemComponent } from '../../../components/transaction-item/transaction-item.component';

@Component({
  selector: 'app-transactions-page',
  standalone: true,
  imports: [CommonModule, TransactionItemComponent],
  templateUrl: './transactions-page.component.html',
})
export class TransactionsPageComponent implements OnInit {
  transactions: any[] = [];

  constructor(private readonly apiService: ApiService) { }

  ngOnInit(): void {
    this.apiService.getTransactions().subscribe({
      next: (data: any[]) => {
        this.transactions = data;
      },
      error: (error) => {
        console.error('Error fetching transactions:', error);
      }
    });
  }
}
