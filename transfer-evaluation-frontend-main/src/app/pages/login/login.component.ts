import { AuthService } from 'src/app/components/services/auth.service';
import { Component, OnInit, OnDestroy } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ToastrService } from 'ngx-toastr';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit, OnDestroy {
  loginForm: FormGroup;
  incorrectForm = true;
  constructor(private authService: AuthService,
              private route: Router,
              private toastr: ToastrService
    ) {}

  ngOnInit() {
    this.loginForm = new FormGroup({
      username: new FormControl(null, Validators.required),
      password: new FormControl(null, Validators.required)
    });
    this.loginForm.valueChanges.subscribe(data => {
      this.incorrectForm = false;
    });
  }
  onSubmit() {
    if (this.loginForm.valid) {
      this.authService.login(this.loginForm.value).subscribe(res => {
        AuthService.isLogin = true;
        this.route.navigateByUrl('/dashboard');
        this.toastr.success('', 'Login Successfull!');
      }, error => {
        this.toastr.error('Either username or password is incorrect', 'Login Not Successful!'
        , {
          timeOut: 10000,
          positionClass: 'toast-top-right',
        });
      });
    }
  }
  ngOnDestroy() {
  }

}
