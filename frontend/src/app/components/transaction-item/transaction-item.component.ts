import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-transaction-item',
  standalone: true,
  template: `
    <li>{{ transaction.type }} - {{ transaction.amount }} - {{ transaction.date }}</li>
  `,
})
export class TransactionItemComponent {
  @Input() transaction: any;
}
