import { ToastrService } from 'ngx-toastr';
import { DataService } from './../../components/services/data_service.service';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-check-transfer-evaluation',
  templateUrl: './check-transfer-evaluation.component.html',
  styleUrls: ['./check-transfer-evaluation.component.css']
})
export class CheckTransferEvaluationComponent implements OnInit {

  transferEvaluationData;

  constructor(private dataService: DataService,
    private route: Router,
    private toastr: ToastrService) { }

  ngOnInit(): void {
    if (!this.dataService.transferTableData) {
      this.route.navigateByUrl('/addTables');
    }
    this.transferEvaluationData = this.dataService.transferTableData;
    console.log(this.transferEvaluationData);
  }

  onUpdate() {
    this.route.navigateByUrl('/addTables?update=true');
  }
  onAdd() {
    const data = {
      'major_name': this.transferEvaluationData.majorField,
      'school_name': this.transferEvaluationData.schoolField,
      'transfer_subject_number': this.transferEvaluationData.transferCourseSubject,
      'transfer_course_title': this.transferEvaluationData.transferCourseTitle,
      'unhm_equivalent': this.transferEvaluationData.unhm_equivalent,
      'approver_name': this.transferEvaluationData.approver_name,
      'approved_status': this.transferEvaluationData.approved_status,
      'sem_or_year_taken': this.transferEvaluationData.sem_year_taken,
      'expiration_data': this.transferEvaluationData.expiration_date
    }
    this.dataService.post_checktransferevaluation(data).subscribe(res => {
      this.toastr.success('Successfully Submited');
      this.route.navigateByUrl('/dashboard');
    }, err => {
      this.toastr.error('Please try again later', 'Data not added', {
          timeOut: 10000,
          positionClass: 'toast-top-right',
        });
      this.route.navigateByUrl('/dashboard');
    });
  }
  onCancel() {
    this.route.navigateByUrl('/addTables');
  }
}
