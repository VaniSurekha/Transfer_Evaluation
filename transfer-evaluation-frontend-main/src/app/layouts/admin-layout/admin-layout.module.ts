import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { ClipboardModule } from 'ngx-clipboard';

import { AdminLayoutRoutes } from './admin-layout.routing';
import { DashboardComponent } from '../../pages/dashboard/dashboard.component';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
// import { ToastrModule } from 'ngx-toastr';
import { MatTableModule } from '@angular/material/table';
import { MatSortModule } from '@angular/material/sort';
import { MatPaginatorModule } from '@angular/material/paginator';
import {MatAutocompleteModule} from '@angular/material/autocomplete';
import {MatInputModule} from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { AddTablesComponent } from '../../pages/add-tables/add-tables.component';
import { AuthGaurd } from './../../components/gaurds/authGaurd.gaurd';
import { DataService } from './../../components/services/data_service.service';
import { CheckTransferEvaluationComponent } from '../../pages/check-transfer-evaluation/check-transfer-evaluation.component';



@NgModule({
  imports: [
    CommonModule,
    RouterModule.forChild(AdminLayoutRoutes),
    ReactiveFormsModule,
    HttpClientModule,
    NgbModule,
    ClipboardModule,
    MatTableModule,
    MatSortModule,
    MatPaginatorModule,
    MatAutocompleteModule,
    MatFormFieldModule,
    MatInputModule,
  ],
  declarations: [
    DashboardComponent,
    AddTablesComponent,
    CheckTransferEvaluationComponent
  ],
  providers: [DataService]
})

export class AdminLayoutModule {}
