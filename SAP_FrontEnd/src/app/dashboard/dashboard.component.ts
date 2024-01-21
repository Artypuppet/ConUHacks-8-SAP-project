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
import { ChartDataServiceService } from '../Chart-Data-Service/chart-data-service.service'
import { Chart } from 'chart.js'
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
export class DashboardComponent {
  title: string = 'Revenue per Car Type'
  barChartRevenue: any = []
  barChartLoss: any = []
  barChartRevApptNum: any = []
  barChartTurnAwayNum: any = []
  initialized: boolean = false
  constructor(private chartData: ChartDataServiceService) {}
  ngOnIt() {
    if (
      this.chartData.barCharData.length == 0 &&
      Object.keys(this.chartData.finalMetricsData).length == 0
    ) {
      let revenue = []
      let totalRevenueLoss = []
      let totalRevenueApptNum = []
      let totalTurnAwayNum = []
      let lables = [
        'Compact Cars',
        'Medium Cars',
        'Full-Size Cars',
        'Class 1 Trucks',
        'Class 2 Trucks',
      ]
      for (let i = 0; i < 5; i++) {
        revenue.push(parseInt(this.chartData.barCharData[i]['totalRevenue']))
        totalRevenueLoss.push(
          parseInt(this.chartData.barCharData[i]['totalRevenueLoss'])
        )
        totalRevenueApptNum.push(
          parseInt(this.chartData.barCharData[i]['totalAppointmentNum'])
        )
        totalTurnAwayNum.push(
          parseInt(this.chartData.barCharData[i]['totalAppointmentNum'])
        )
      }
      this.barChartRevenue = new Chart('Revenue', {
        type: 'bar',
        data: {
          labels: lables,
          datasets: [
            {
              label: '$Revenue',
              data: revenue,
              borderWidth: 1,
            },
          ],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      })
      this.barChartLoss = new Chart('Loss', {
        type: 'bar',
        data: {
          labels: lables,
          datasets: [
            {
              label: '$loss',
              data: totalRevenueLoss,
              borderWidth: 1,
            },
          ],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      })
      this.barChartRevApptNum = new Chart('TotalApptNum', {
        type: 'bar',
        data: {
          labels: lables,
          datasets: [
            {
              label: '# total Appointments',
              data: totalRevenueApptNum,
              borderWidth: 1,
            },
          ],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      })
      this.barChartTurnAwayNum = new Chart('NumOfTurnAway', {
        type: 'bar',
        data: {
          labels: lables,
          datasets: [
            {
              label: '#total Appointments turned Away',
              data: totalTurnAwayNum,
              borderWidth: 1,
            },
          ],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      })
    }
  }

  onClick() {
    this.checkDashboard()
  }
  checkDashboard() {
    if (
      this.chartData.barCharData == null &&
      this.chartData.finalMetricsData == null
    )
      return
    this.initialized = true
    let revenue = []
    let totalRevenueLoss = []
    let totalRevenueApptNum = []
    let totalTurnAwayNum = []
    let lables = [
      'Compact Cars',
      'Medium Cars',
      'Full-Size Cars',
      'Class 1 Trucks',
      'Class 2 Trucks',
    ]
    for (let i = 0; i < 5; i++) {
      revenue.push(parseInt(this.chartData.barCharData[i]['totalRevenue']))
      totalRevenueLoss.push(
        parseInt(this.chartData.barCharData[i]['totalRevenueLoss'])
      )
      totalRevenueApptNum.push(
        parseInt(this.chartData.barCharData[i]['totalAppointmentNum'])
      )
      totalTurnAwayNum.push(
        parseInt(this.chartData.barCharData[i]['totalAppointmentNum'])
      )
    }
    this.barChartRevenue = new Chart('Revenue', {
      type: 'bar',
      data: {
        labels: lables,
        datasets: [
          {
            label: '$Revenue',
            data: revenue,
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    })
    this.barChartLoss = new Chart('Loss', {
      type: 'bar',
      data: {
        labels: lables,
        datasets: [
          {
            label: '$loss',
            data: totalRevenueLoss,
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    })
    this.barChartRevApptNum = new Chart('TotalApptNum', {
      type: 'bar',
      data: {
        labels: lables,
        datasets: [
          {
            label: '# total Appointments',
            data: totalRevenueApptNum,
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    })
    this.barChartTurnAwayNum = new Chart('NumOfTurnAway', {
      type: 'bar',
      data: {
        labels: lables,
        datasets: [
          {
            label: '#total Appointments turned Away',
            data: totalTurnAwayNum,
            borderWidth: 1,
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    })
  }
}
