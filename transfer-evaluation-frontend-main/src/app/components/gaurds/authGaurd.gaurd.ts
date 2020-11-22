import { AuthService } from 'src/app/components/services/auth.service';
import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthGaurd implements CanActivate {
  constructor(private authService: AuthService,
    private router: Router) {
  }

  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
    console.log(AuthService.isLogin)
    if (AuthService.isLogin) {
      return true;
    } else {
      this.router.navigateByUrl('/login');
    }
  }
}
