import { Component } from '@angular/core'
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
} from '@nebular/theme'
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
  ],
  templateUrl: './Input-Page.component.html',
  styleUrls: ['./Input-Page.component.scss'],
})
export class InputPageComponent {
  form: any
  allFiles: Array<File> = []
  constructor(fb: FormBuilder, private http: HttpClient) {
    this.form = fb.group({
      file: ['', Validators.required],
    })
  }
  onFileClick(event: any) {
    let value = event.target.files[0]
    this.allFiles.push(value)
  }
  uploadFile(index: number) {
    console.log(this.allFiles[index])
    if (this.allFiles[index]) {
      const formData = new FormData()
      formData.append('file', this.allFiles[index], this.allFiles[index].name)
      const post = this.http.post('http://127.0.0.1:5000/files', formData, {
        responseType: 'text',
      })
      post.subscribe()
    }
  }
  removeFile(index: number) {
    this.allFiles.splice(index)
  }
  onSubmit() {}
}
