import { Injectable } from '@angular/core'

@Injectable({
  providedIn: 'root',
})
export class ChartDataServiceService {
  public barCharData: any
  public finalMetricsData: any
  constructor() {
    this.barCharData = null
    this.finalMetricsData = null
  }
  barChar(data: any) {
    this.barCharData = data
  }
  finalMetrics(data: any) {
    this.finalMetricsData = data
  }
}
