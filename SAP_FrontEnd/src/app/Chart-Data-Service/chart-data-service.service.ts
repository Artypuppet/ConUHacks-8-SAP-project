import { Injectable } from '@angular/core'
import { HttpClient } from '@angular/common/http'
import { Subject } from 'rxjs'
@Injectable({
    providedIn: 'root',
})
export class ChartDataServiceService {
    private _barChartData: any
    private _finalMetricsData: any
    public mySubject: Subject<any> = new Subject<any>();
    private url: string = "http://127.0.0.1:5000/files"
    constructor() {
        this._barChartData = null
        this._finalMetricsData = null
    }
    set barChartData(data: any) {
        this._barChartData = data;
        console.log("In bar chart setter");
        console.log(data);
        this.mySubject.next({ barChartData: this.barCharData });
    }
    set finalMetricsData(data: any) {
        this._finalMetricsData = data;
        console.log(data);
        console.log("In final metrics setter")
        this.mySubject.next({ finalMetricsData: this._finalMetricsData });
    }

    get barCharData() {
        return this._barChartData;
    }
    get finalMetricsData() {
        return this._finalMetricsData;
    }

}
