import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../services/api.service';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-cancel-subscription',
  standalone: true,
  imports: [CommonModule, RouterLink, FormsModule],
  templateUrl: './cancel-subscription.component.html',
})
export class CancelSubscriptionComponent implements OnInit {
  funds: any[] = [];
  selectedFundId!: string;

  constructor(private readonly apiService: ApiService) { }

  ngOnInit(): void {
    this.apiService.getFunds().subscribe({
      next: (data: any[]) => {
        this.funds = data;
      },
      error: (error) => {
        console.error('Error fetching funds:', error);
      }
    });
  }

  cancel() {
    if (this.selectedFundId) {
      this.apiService.cancelFundSubscription(this.selectedFundId).subscribe({
        next: (response) => {
          console.log('Cancellation successful:', response);
          alert(`Subscription to fund ${this.selectedFundId} canceled successfully!`);
        },
        error: (error) => {
          console.error('Error canceling subscription:', error);
          alert('Cancellation failed: ' + error.message);
        }
      });
    }
  }
}
