import { environment } from './../../../environments/environment';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class AuthService {
  static isLogin = false;
  api_url: string = environment.API_url;
  constructor(private http: HttpClient,
              private route: Router) {
  }
  register(data) {
    const form_data = new FormData;
    for(let key in data) {
        form_data.append(key, data[key])
    }
    return this.http.post(this.api_url + '/register/', form_data);
  }
  login(data) {
    const form_data = new FormData;
    for(let key in data) {
        form_data.append(key, data[key])
    }
    return this.http.post(this.api_url + '/login/', form_data);
  }
  logout() {
    AuthService.isLogin = false;
    this.route.navigateByUrl('/login')
  }
}
