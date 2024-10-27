import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../services/api.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';
import { forkJoin } from 'rxjs';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-cancel-subscription',
  standalone: true,
  imports: [CommonModule, RouterLink, FormsModule],
  templateUrl: './cancel-subscription.component.html',
})
export class CancelSubscriptionComponent implements OnInit {
  funds: any[] = [];
  activeSubscriptions: any[] = [];
  selectedFundId!: string;

  constructor(private readonly apiService: ApiService) { }

  ngOnInit(): void {
    forkJoin({
      funds: this.apiService.getFunds(),
      subscriptions: this.apiService.getActiveSubscriptions()
    }).subscribe({
      next: (result) => {
        this.funds = result.funds;
        this.activeSubscriptions = result.subscriptions.map((subscription: { fund_id: any; }) => {
          const fund = this.funds.find(f => f.id === subscription.fund_id);
          return {
            ...subscription,
            fund_name: fund ? fund.name : 'Unknown Fund',
          };
        });
      },
      error: (error) => {
        console.error('Error fetching data:', error);
      }
    });
  }

  cancel() {
    if (this.selectedFundId) {
      this.apiService.cancelFundSubscription(this.selectedFundId).subscribe({
        next: (response) => {
          console.log('Subscription canceled:', response);
          Swal.fire({
            title: 'Success!',
            text: `Subscription to fund ${this.getFundName(this.selectedFundId)} canceled successfully!`,
            icon: 'success',
            confirmButtonText: 'OK'
          });

          this.activeSubscriptions = this.activeSubscriptions.filter(fund => fund.fund_id !== this.selectedFundId);
        },
        error: (error) => {
          console.error('Error canceling subscription:', error);
          Swal.fire({
            title: 'Error!',
            text: 'Cancellation failed: ' + error.message,
            icon: 'error',
            confirmButtonText: 'OK'
          });
        }
      });
    }
  }

  getFundName(fundId: string): string {
    const fund = this.funds.find(f => f.id === fundId);
    return fund ? fund.name : 'Unknown Fund';
  }
}
