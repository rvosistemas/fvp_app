import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-fund-item',
  standalone: true,
  imports: [],
  templateUrl: './fund-item.component.html',
  styleUrl: './fund-item.component.css'
})
export class FundItemComponent {
  @Input() fund: any;
}
