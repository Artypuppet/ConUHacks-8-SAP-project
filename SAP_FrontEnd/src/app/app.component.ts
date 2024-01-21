import { Component } from '@angular/core'
import { NbSidebarService, NbMenuItem, NbMenuService } from '@nebular/theme'
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  title = 'SAP_FrontEnd'
  items: NbMenuItem[] = [
    {
      title: 'Home',
      icon: 'home-outline',
      link: '/',
    },
    {
      title: 'DashBoard',
      icon: 'browser-outline',
      link: '/dashboard',
    },
    {
      title: 'Calendar View',
      icon: 'calendar-outline',
    },
  ]
  constructor(private sidebarService: NbSidebarService) {}
  toggle() {
    this.sidebarService.toggle(true)
    return false
  }
}