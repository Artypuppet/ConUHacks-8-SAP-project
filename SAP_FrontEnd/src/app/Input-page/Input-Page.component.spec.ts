import { ComponentFixture, TestBed } from '@angular/core/testing';
import { InputPageComponent } from './Input-Page.component';

describe('InputPageComponent', () => {
  let component: InputPageComponent;
  let fixture: ComponentFixture<InputPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ InputPageComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InputPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
