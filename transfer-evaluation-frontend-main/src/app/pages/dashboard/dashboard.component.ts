import { Major } from '../../../model/common.model';
import { FormControl, FormGroup } from '@angular/forms';
import { DataService } from './../../components/services/data_service.service';
import { AfterViewInit, Component, OnInit, ViewChild } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import {MatPaginator} from '@angular/material/paginator';
import { Observable, of } from 'rxjs';
import {filter, map, startWith} from 'rxjs/operators';



@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit, AfterViewInit {

  public datasets: any;
  public data: any;
  dataSource = new MatTableDataSource([]);
  searchForm: FormGroup;
  majorField = new FormControl('All');
  filteredMajor: Observable<string[]>;
  schoolField = new FormControl('All');
  filteredSchool: Observable<string[]>;
  stateField = new FormControl('All');
  filteredState: Observable<string[]>;
  majorOptions = ['All'];
  schoolOptions = ['All'];
  stateOptions = ['All'];

  displayedColumns = ['id', 'approved_status', 'transfer_course_id', 'subject_number', 'title', 'school_id', 'school_name', 'school_state', 'major_req_id', 'major_description', 'major_id', 'major_name', 'approver_id', 'approver_name'];
  @ViewChild(MatPaginator) paginator: MatPaginator;

  constructor(private dataService: DataService) {}
  ngOnInit() {
    this.searchForm = new FormGroup({
      'majorField': this.majorField,
      'schoolField': this.schoolField,
      'stateField': this.stateField
    });

    this.dataService.get_distinctmajor().subscribe(data => {
      data.map(i => this.majorOptions.push(i['major_name']));
      this.filteredMajor = this.majorField.valueChanges.pipe(
      startWith(''),
      map(value => typeof value === 'string' ? value : value.name),
      map(value => value ? this._filter(value, this.majorOptions) : this.majorOptions.slice())
    );
    });
    this.dataService.get_distinctschool().subscribe(data => {
      data.map(i => this.schoolOptions.push(i['school_name']));
      this.filteredSchool = this.schoolField.valueChanges.pipe(
        startWith(''),
        map(value => value ? this._filter(value, this.schoolOptions): this.schoolOptions.slice())
      );
    });
    this.dataService.get_distinct_state().subscribe(data => {
      data.map(i => this.stateOptions.push(i['state_name']));
      this.filteredState = this.stateField.valueChanges.pipe(
        startWith(''),
        map(value => value ? this._filter(value, this.stateOptions): this.stateOptions.slice())
      );
    });
    this.dataService.get_table_data().subscribe(data => {
        this.dataSource = new MatTableDataSource(data);
        setTimeout(() => this.dataSource.paginator = this.paginator);
    });


  }
  ngAfterViewInit() {
    this.dataSource.paginator = this.paginator;
  }

  inputControl(event, options, field) {
    setTimeout(() => {
        let isValueTrue = options.filter(myAlias => {
              return myAlias.includes(event.target.value);
            });
        if (isValueTrue.length === 0) {
            field.setValue('All');
        }
    }, 300);
  }

  search_tables() {
    if (this.searchForm.dirty) {
      this.dataService.get_transferevaluationmaindisplay(this.stateField.value, this.schoolField.value, this.majorField.value).subscribe(data =>{
        this.dataSource = new MatTableDataSource(data);
        setTimeout(() => this.dataSource.paginator = this.paginator);
        this.searchForm.markAsPristine();
      })
    }
  }

  public updateOptions() {
  }

   private _filter(value: string, options): string[] {
    const filterValue = value.toLowerCase();
    return options.filter(option => option.toLowerCase().indexOf(filterValue) === 0);
  }

}
