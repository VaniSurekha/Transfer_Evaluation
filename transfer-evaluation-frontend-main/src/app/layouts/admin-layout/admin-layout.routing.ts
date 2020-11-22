import { AddTablesComponent } from './../../pages/add-tables/add-tables.component';
import { AuthGaurd } from './../../components/gaurds/authGaurd.gaurd';
import { Routes } from '@angular/router';

import { DashboardComponent } from '../../pages/dashboard/dashboard.component';
import { CheckTransferEvaluationComponent } from '../../pages/check-transfer-evaluation/check-transfer-evaluation.component';

export const AdminLayoutRoutes: Routes = [
    // { path: 'dashboard', component: DashboardComponent, canActivate: [AuthGaurd] }
    { path: 'dashboard', component: DashboardComponent },
    { path: 'addTables', component: AddTablesComponent },
    { path: 'checktransferevaluation', component: CheckTransferEvaluationComponent}
];
