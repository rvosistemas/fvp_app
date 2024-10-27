import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../services/api.service';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { FormsModule } from '@angular/forms';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-subscribe-fund',
  standalone: true,
  imports: [CommonModule, RouterLink, FormsModule],
  templateUrl: './subscribe-fund.component.html',
})
export class SubscribeFundComponent implements OnInit {
  funds: any[] = [];
  selectedFundId!: string;
  amount: number = 0;
  userBalance: number = 0;
  showValidationErrors = false;

  constructor(private readonly apiService: ApiService) { }

  ngOnInit(): void {
    const savedBalance = localStorage.getItem('userBalance');
    this.userBalance = savedBalance ? parseFloat(savedBalance) : 500000;

    this.apiService.getFunds().subscribe({
      next: (data: any[]) => {
        this.funds = data;
      },
      error: (error) => {
        console.error('Error fetching funds:', error);
      }
    });
  }

  subscribe() {
    if (this.selectedFundId && this.amount > 0 && this.userBalance >= this.amount) {
      this.apiService.subscribeToFund(this.selectedFundId, this.amount, this.userBalance).subscribe({
        next: (response) => {
          if (response.error) {
            Swal.fire({
              icon: 'error',
              title: 'Subscription failed',
              text: response.error,
            });
          } else {
            this.userBalance -= this.amount;
            localStorage.setItem('userBalance', this.userBalance.toString());

            Swal.fire({
              icon: 'success',
              title: 'Subscribed!',
              text: `Subscribed to fund ${this.selectedFundId} successfully!`,
            });
          }
        },
        error: (error) => {
          console.error('Error subscribing to fund:', error);
          Swal.fire({
            icon: 'error',
            title: 'Subscription failed',
            text: `Subscription failed: ${error.message}`,
          });
        }
      });
    } else {
      this.showValidationErrors = true;
    }
  }


}
