import { Component } from '@angular/core'
import { CommonModule } from '@angular/common'
import {
  NbInputModule,
  NbCardModule,
  NbButtonModule,
  NbAlertModule,
  NbFormFieldModule,
  NbIconModule,
  NbListModule,
} from '@nebular/theme'
@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    CommonModule,
    NbInputModule,
    NbCardModule,
    NbButtonModule,
    NbAlertModule,
    NbFormFieldModule,
    NbIconModule,
    NbListModule,
  ],
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss'],
})
export class DashboardComponent {}
