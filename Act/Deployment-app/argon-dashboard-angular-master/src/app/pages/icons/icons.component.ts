import { Component } from '@angular/core';
import { NgForm } from '@angular/forms';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-icons',
  templateUrl: './icons.component.html',
  styleUrls: ['./icons.component.scss']
})
export class IconsComponent {
  selectedFile: File | null = null;
  analysisType: string = '';
  selectedFileName: string = 'Choose file...';
  selectedApi: string = 'maha'; // Default selection
  isLoading: boolean = false;
  result: string | null = null;
  error: string | null = null;

  API_URLS = {
    maha: 'http://102.156.37.13:8000/api/drawing/maha/',
    achref: 'http://102.156.37.13:8000/api/drawing/achref/',
    idriss: 'http://102.156.37.13:8000/api/math/idriss/',
    heni: 'http://197.17.78.190:8001/predict',
  };

  constructor(private http: HttpClient) { }

  onFileSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    if (input.files?.length) {
      this.selectedFile = input.files[0];
      this.selectedFileName = this.selectedFile.name;
    }
  }

  onSubmit(form: NgForm): void {
  if (form.valid) {
    this.isLoading = true;
    this.error = null;
    this.result = null;

    const apiUrl = this.API_URLS[this.selectedApi as keyof typeof this.API_URLS];

    if (this.selectedApi === "idriss") {
      // Text-based request
      const payload = {
        prompt: this.analysisType.trim() || "return the correctness and the math creativity and the reason behind the reasoning"
      };

      this.http.post(apiUrl, payload, {
        headers: { "Content-Type": "application/json" }
      }).subscribe({
        next: (response: any) => {
          console.log('API Response:', response);
          this.handleSuccess(response);
        },
        error: (err: HttpErrorResponse) => {
          console.error('API Error:', err);
          this.handleError(err);
        },
        complete: () => this.isLoading = false
      });

    } else if (this.selectedApi === "heni" && this.selectedFile) {
      // File-based request for Heni API
      const formData = new FormData();
      formData.append('file', this.selectedFile, this.selectedFile.name);

      this.http.post(apiUrl, formData).subscribe({
        next: (response: any) => {
          console.log('API Response:', response);
          this.handleSuccess(response);
        },
        error: (err: HttpErrorResponse) => {
          console.error('API Error:', err);
          this.handleError(err);
        },
        complete: () => this.isLoading = false
      });

    } else if (this.selectedFile) {
      // File-based request for other APIs
      const formData = new FormData();
      formData.append('image', this.selectedFile, this.selectedFile.name);
      formData.append('analysisType', this.analysisType);

      this.http.post(apiUrl, formData).subscribe({
        next: (response: any) => {
          console.log('API Response:', response);
          this.handleSuccess(response);
        },
        error: (err: HttpErrorResponse) => {
          console.error('API Error:', err);
          this.handleError(err);
        },
        complete: () => this.isLoading = false
      });
    } else {
      this.error = 'Please select a file before submitting.';
      this.isLoading = false;
    }
  }
}
  
private handleSuccess(response: any): void {
  switch (this.selectedApi) {
    case 'maha':
      this.result = response?.result || 'Unexpected response format from Maha API';
      break;

    case 'achref':
      this.result = response?.prediction
        ? `Prediction: ${response.prediction}\nConfidence: ${response.confidence}%\nInterpretation: ${response.interpretation}`
        : 'Unexpected response format from Achref API';
      break;

    case 'idriss':
      this.result = response?.response || 'Unexpected response format from Idriss API';
      break;

    case 'heni':
  if (this.selectedFile) {
    const formData = new FormData();
    formData.append('file', this.selectedFile, this.selectedFile.name);

    const apiUrl = this.API_URLS.heni;

    this.http.post(apiUrl, formData, {
      headers: { "X-API-Key": "ekteb_benmoussa" }
    }).subscribe({
      next: (response: any) => {
        if (response?.output) {
          this.result = `📐 LaTeX Output: ${response.output}`;
        } else {
          this.error = 'Unexpected response format from Heni API';
        }
      },
      error: (err: HttpErrorResponse) => {
        console.error('Heni API Error:', err);
        this.handleError(err);
      },
      complete: () => this.isLoading = false
    });
  } else {
    this.error = 'No file selected';
  }
  break;

    default:
      this.error = 'Unknown API selected';
  }
}
  private handleError(err: HttpErrorResponse): void {
    if (err.error instanceof ErrorEvent) {
      this.error = `Client error: ${err.error.message}`;
    } else if (err.error) {
      const serverMessage = typeof err.error === 'string' ? err.error : JSON.stringify(err.error);
      this.error = `Server error: ${serverMessage}`;
    } else {
      this.error = `Server error: ${err.status} ${err.statusText}`;
    }
  }

  private resetForm(): void {
    this.selectedFile = null;
    this.selectedFileName = 'Choose file...';
    this.analysisType = '';
    this.result = null;
    this.error = null;
  }
}
