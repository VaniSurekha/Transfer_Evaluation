import { Router } from '@angular/router';
import { AuthService } from 'src/app/components/services/auth.service';
import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormControl, FormGroup, FormGroupName, ValidationErrors, Validators } from '@angular/forms';
import { ToastrService } from 'ngx-toastr';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  signupForm: FormGroup;
  signupFormError = false;
  incorrectForm = false;
  constructor(private authService: AuthService,
              private route: Router,
              private toastr: ToastrService
              ) { }

  ngOnInit() {
    this.signupForm = new FormGroup({
      username: new FormControl(null, Validators.required),
      email: new FormControl(null, [Validators.required, Validators.email]),
      passwords: new FormGroup({
        password: new FormControl(null, Validators.required),
        conf_pass: new FormControl(null, [Validators.required])
      }, {validators: this.checkPasswords})

    });
    this.signupForm.valueChanges.subscribe(() => {
      this.incorrectForm = false;
    });
  }
  onSubmit() {
    if (this.signupForm.valid) {
      const register_data = {
        'username': this.signupForm.get('username').value,
        'email': this.signupForm.get('email').value,
        'password': this.signupForm.get('passwords').get('password').value,
        'conf_pass': this.signupForm.get('passwords').get('conf_pass').value
      };
      this.authService.register(register_data).subscribe(res => {
        this.toastr.success('Please Login!', 'Registration Successfull!',{
          timeOut: 10000,
          positionClass: 'toast-top-right',
        });
        this.route.navigate(['login']);
      }, error => {
        this.toastr.error('Either username or email already in use!', 'Registration Not Successfull!', {
          timeOut: 10000,
          positionClass: 'toast-top-right',
        });
      });
    } else {
      this.incorrectForm = true;
    }
  }

  checkPasswords(group: FormGroup) { // here we have the 'passwords' group
    const pass = group.get('password').value;
    const confirmPass = group.get('conf_pass').value;

    return pass === confirmPass ? null : { 'notSame': true };
  }

}
