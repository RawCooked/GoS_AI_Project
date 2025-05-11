import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'https://jsonplaceholder.typicode.com'; // Free test API

  constructor(private http: HttpClient) { }

  // Get all posts
  getPosts(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/posts`);
  }

  // Get single post by ID
  getPostById(id: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/posts/${id}`);
  }

  // Get comments for a specific post
  getPostComments(postId: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/posts/${postId}/comments`);
  }

  // Search posts by user ID (query parameter example)
  getPostsByUser(userId: number): Observable<any[]> {
    const params = new HttpParams().set('userId', userId.toString());
    return this.http.get<any[]>(`${this.apiUrl}/posts`, { params });
  }

  // Get all users
  getUsers(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/users`);
  }

  // Get user albums
  getUserAlbums(userId: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/users/${userId}/albums`);
  }
}
