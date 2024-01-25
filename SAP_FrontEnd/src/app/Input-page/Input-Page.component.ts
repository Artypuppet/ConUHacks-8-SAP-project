import { Component, Input, Output, EventEmitter } from '@angular/core'
import { CommonModule } from '@angular/common'
import {
    FormsModule,
    ReactiveFormsModule,
    FormGroup,
    FormControl,
    Validators,
    FormArray,
    FormBuilder,
} from '@angular/forms'
import {
    NbInputModule,
    NbCardModule,
    NbButtonModule,
    NbAlertModule,
    NbFormFieldModule,
    NbIconModule,
    NbListModule,
    NbSpinnerModule,
} from '@nebular/theme'
import { DashboardComponent } from '../dashboard/dashboard.component'
import { ChartDataServiceService } from '../Chart-Data-Service/chart-data-service.service'
import { RouterLink } from '@angular/router'
import { HttpClient } from '@angular/common/http'
@Component({
    selector: 'input-page',
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
        FormsModule,
        ReactiveFormsModule,
        RouterLink,
        NbSpinnerModule,
    ],
    templateUrl: './Input-Page.component.html',
    styleUrls: ['./Input-Page.component.scss'],
})
export class InputPageComponent {
    form: any
    allFiles: Array<File> = []
    @Input() loading: boolean = false
    @Output() loadingChange = new EventEmitter<Boolean>();
    constructor(
        fb: FormBuilder,
        private http: HttpClient,
        private chartDataService: ChartDataServiceService
    ) {
        this.form = fb.group({
            file: ['', Validators.required],
        })
        chartDataService = new ChartDataServiceService()
    }
    onFileClick(event: any) {
        let value = event.target.files[0]
        this.allFiles.push(value)
    }
    async uploadFile(index: number) {
        if (this.allFiles[index]) {

            const formData = new FormData()
            formData.append('file', this.allFiles[index], this.allFiles[index].name)
            this.removeFile(index)

            this.loading = false;
            this.loadingChange.emit(this.loading);
            const response = await this.http
                .post('http://127.0.0.1:5000/files', formData, {
                    responseType: 'text',
                })
                .toPromise()

            let data = JSON.parse(response!)
            for (let dataKey in data) {
                data[dataKey] = JSON.parse(data[dataKey]);
            }
            this.chartDataService.barChartData = data.graphData
            this.chartDataService.finalMetricsData = data.finalMetrics
            console.log(this.chartDataService)
        }
    }
    removeFile(index: number) {
        this.allFiles.splice(index)
    }
    onSubmit() { }
}
