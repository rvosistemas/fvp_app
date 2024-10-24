import { Routes } from '@angular/router';
import { FundsPageComponent } from './pages/funds/funds-page/funds-page.component';
import { TransactionsPageComponent } from './pages/transactions/transactions-page/transactions-page.component';
import { HomeComponent } from './pages/home/home.component';
import { SubscribeFundComponent } from './pages/funds/subscribe-fund/subscribe-fund.component';
import { CancelSubscriptionComponent } from './pages/funds/cancel-subscription/cancel-subscription.component';

export const routes: Routes = [
  {
    path: '',
    component: HomeComponent,
    children: [
      {
        path: 'funds',
        component: FundsPageComponent,
      },
      {
        path: 'subscribe',
        component: SubscribeFundComponent,
      },
      {
        path: 'cancel',
        component: CancelSubscriptionComponent,
      },
      {
        path: 'transactions',
        component: TransactionsPageComponent,
      }
    ]
  },
  {
    path: '**',
    redirectTo: ''
  }
];
