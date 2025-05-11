import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

type ApiKey =  'khalil' | 'azer' ;

@Component({
  selector: 'app-maps',
  templateUrl: './maps.component.html',
  styleUrls: ['./maps.component.scss']
})
export class MapsComponent {
  selectedFile: File | null = null;
  selectedFileName = 'Choose file...';
  selectedApi: ApiKey = 'khalil';
  isLoading = false;
  result: string | null = null;
  error: string | null = null;

  readonly API_URLS: Record<ApiKey,string> = {
    khalil: 'http://102.156.37.13:8000/api/audio/khalil/',
    azer: 'http://102.156.37.13:8000/api/audio/azer/',
  };

  constructor(private http: HttpClient) {}

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files?.length) {
      this.selectedFile = input.files[0];
      this.selectedFileName = this.selectedFile.name;
    }
  }

  onSubmit(form: NgForm): void {
    if (!form.valid || !this.selectedFile) return;

    this.isLoading = true;
    this.error = this.result = null;

    const formData = new FormData();
    // use 'audio' key for khalil, 'image' otherwise
    const key = this.selectedApi === 'khalil' ? 'audio' : 'image';
    formData.append(key, this.selectedFile, this.selectedFile.name);

    this.http.post(this.API_URLS[this.selectedApi], formData)
      .subscribe({
        next: res => {
          this.handleSuccess(res as any);
          this.isLoading = false;
        },
        error: (err: HttpErrorResponse) => {
          this.error = err.error?.message || `Server error: ${err.status}`;
          this.isLoading = false;
        }
      });
  }

  private handleSuccess(resp: any): void {
    switch (this.selectedApi) {
      case 'azer':
        this.result = resp.result;
        break;

      case 'khalil':
        this.result = [
          `Result: ${resp.result}`,
          `Confidence: ${resp.confidence}`,
          `Interpretation: ${resp.interpretation}`
        ].join('\n');
        break;
    }
  }
}
