import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../services/api.service';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';
import { FundItemComponent } from '../../../components/fund-item/fund-item.component';

@Component({
  selector: 'app-funds-page',
  standalone: true,
  imports: [CommonModule, FundItemComponent, RouterLink],
  templateUrl: './funds-page.component.html',
})
export class FundsPageComponent implements OnInit {
  funds: any[] = [];

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

}
