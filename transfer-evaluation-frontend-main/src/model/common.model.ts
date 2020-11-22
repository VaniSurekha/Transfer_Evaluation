export interface Major {
  major_name: 'string';
}
export interface Schools {
  school_name: 'string';
}
export interface States {
  state_name: 'string';
}
export interface TransferCourses {
  transfer_course_id: number;
  subject_number: string;
  title: string;
  school_id: number;
}
export interface Approvers {
  approver_id: number;
  approver_name: string;
}
