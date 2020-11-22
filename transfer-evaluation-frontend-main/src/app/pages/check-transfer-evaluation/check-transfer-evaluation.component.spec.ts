import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CheckTransferEvaluationComponent } from './check-transfer-evaluation.component';

describe('CheckTransferEvaluationComponent', () => {
  let component: CheckTransferEvaluationComponent;
  let fixture: ComponentFixture<CheckTransferEvaluationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CheckTransferEvaluationComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(CheckTransferEvaluationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
