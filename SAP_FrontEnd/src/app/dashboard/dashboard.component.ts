import { Component, OnChanges, SimpleChanges } from '@angular/core'
import { CommonModule } from '@angular/common'
import { Chart, registerables } from 'chart.js'
Chart.register(...registerables);
import {
    NbInputModule,
    NbCardModule,
    NbButtonModule,
    NbAlertModule,
    NbFormFieldModule,
    NbIconModule,
    NbListModule,
    NbSpinnerModule
} from '@nebular/theme'
import { ChartDataServiceService } from '../Chart-Data-Service/chart-data-service.service'

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
        NbSpinnerModule
    ],

    templateUrl: './dashboard.component.html',
    styleUrls: ['./dashboard.component.scss'],
})
export class DashboardComponent {
    revenue: any = [];
    totalRevenueLoss: any = [];
    totalRevenueApptNum: any = [];
    totalTurnAwayNum: any = [];
    title: string = 'Revenue per Car Type'
    barChartRevenue: any = []
    barChartLoss: any = []
    barChartRevApptNum: any = []
    barChartTurnAwayNum: any = []
    loading: boolean = false

    constructor(public chartData: ChartDataServiceService) { }
    ngOnInit() {
        console.log("in ngOnIt")
        // let revenue = [240750, 235350, 238950, 425750, 1243900];
        // let totalRevenueLoss = [-66150, -65400, -66600, -69500, -103600];
        // let totalRevenueApptNum = [1605, 1569, 1593, 1703, 1777];
        // let totalTurnAwayNum = [441, 436, 444, 278, 148];
        this.chartData.mySubject.subscribe((data) => {
            if ("finalMetricsData" in data)
                this.createBarChart();
            else
                this.createFinalMetrics();
        });
        let lables = [
            'Compact Cars',
            'Medium Cars',
            'Full-Size Cars',
            'Class 1 Trucks',
            'Class 2 Trucks',
        ]

        this.barChartRevenue = new Chart('Revenue', {
            type: 'bar',
            data: {
                labels: lables,
                datasets: [
                    {
                        label: '$Revenue',
                        data: this.revenue,
                        backgroundColor: 'rgb(2, 227, 2)',
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
                        data: this.totalRevenueLoss,
                        backgroundColor: 'rgb(168, 64, 50)',
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
                        data: this.totalRevenueApptNum,
                        backgroundColor: 'rgb(2, 96, 227)',
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
                        data: this.totalTurnAwayNum,
                        backgroundColor: 'rgb(227, 2, 84)',
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
    createBarChart() {
        for (let i = 0; i < 5; i++) {
            this.revenue.push(parseInt(this.chartData.barCharData[i]['totalRevenue']))
            this.totalRevenueLoss.push(
                parseInt(this.chartData.barCharData[i]['totalRevenueLoss'])
            )
            this.totalRevenueApptNum.push(
                parseInt(this.chartData.barCharData[i]['totalAppointmentNum'])
            )
            this.totalTurnAwayNum.push(
                parseInt(this.chartData.barCharData[i]['totalAppointmentNum'])
            )
        }
        this.barChartRevenue.update();
        this.barChartLoss.update();
        this.barChartRevApptNum.update();
        this.barChartTurnAwayNum.update();
    }
    createFinalMetrics() {
        console.log("In final metrics");
    }
}
