from django.db import models

# Create your models here.

class FileUpload(models.Model):
    file=models.FileField(blank=False,null=False)

class Major(models.Model):
    major_id = models.AutoField(primary_key=True)
    major_name = models.CharField(max_length=200, unique=True, default=None)

    def __str__(self):
        if self.major_name is None:
            self.major_name='N/A'
        return self.major_name

class School(models.Model):

    school_id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=100, unique=True)
    state_name = models.CharField(max_length=10, null=True)

    def __str__(self):
        if self.school_name is None:
            self.school_name='N/A'
        return self.school_name
    '''
    def name(self):
        return str(self.school_name)

    def schoolid(self):
        return self.school_id
    '''

class Approver(models.Model):
    approver_id = models.AutoField(primary_key=True)
    approver_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        if self.approver_name is None:
            self.approver_name='N/A'
        return self.approver_name
    '''
    def approverid(self):
        return self.approver_id
    '''  
class Major_requirement(models.Model):
    """
    table name is Major_requirement
    major_req_id is the Primarykey
    """
    major_req_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200, default=None,null=True)
    major_id = models.ForeignKey(Major, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('major_id', 'description')

    def __str__(self):
        if self.description is None:
            self.description='N/A'
        return self.description

    '''
    def major_req_id(self):
        return self.major_req_id
    '''
    
class TransferCourse(models.Model):
    transfer_course_id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE, null=True, default=None)
    subject_number = models.CharField(max_length=200,  blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)

    #class Meta:
      #  unique_together = ('school_id', 'subject_number','title',)

    def __str__(self):
        if self.title is None:
            self.title='N/A'
        return self.title
    '''
    def courseid(self):
        return self.transfer_course_id
    '''
class Transferevaluation(models.Model):
    transfer_eval_id = models.AutoField(primary_key=True)
    transfer_course_id = models.ForeignKey(TransferCourse, on_delete=models.CASCADE)
    major_req_id = models.ForeignKey(Major_requirement, on_delete=models.CASCADE)
    sem_year_taken = models.CharField(max_length=8, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)  # It must be in YYYY-MM-DD format
    approved_choice=(('Yes','yes'),('No','no'))
    approved_status = models.CharField(max_length=3, blank=True, null=True,choices=approved_choice)
    notes = models.CharField(max_length=150, blank=True, null=True)
    approver_id = models.ForeignKey(Approver, on_delete=models.CASCADE)

class CheckEvaluation(models.Model):
    """
    Purpose of this table is to have only one record at a time.
    """
    check_eval_id = models.AutoField(primary_key=True)
    approver_choices = (('Yes', 'Yes'), ('No', 'No'))
    major_name = models.CharField(max_length=30)
    school_name = models.CharField(max_length=30)
    #major_name = models.CharField(max_length=40)
    transfer_subject_number = models.CharField(max_length=30)
    transfer_course_title = models.CharField(max_length=30)
    unhm_equivalent = models.CharField(max_length=20)
    approver_name = models.CharField(max_length=20, blank=True, null=True)
    approved_status = models.CharField(max_length=5, choices=approver_choices, default=None)
    sem_or_year_taken = models.CharField(max_length=20, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)

class DropDown(models.Model):
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
