from django.urls import path,re_path
from .views import *

urlpatterns = [
    #signup
    path('register/',RegisterUserView.as_view()),
    #login
    path('login/',LoginUserView.as_view()),
    #logout
    path('logout/',LogoutView.as_view()),

    #import file data and remove the data from database
    path('uploadfile/',FileUploadView.as_view(), name='file-upload'),
    path('removeuploadedfile/',RemoveFileUploadView.as_view(), name='removeuploadedfile'),

    #MajorDropdown
    path('distinctmajor/',DistinctMajorView.as_view()),
    #SchoolDropdown
    path('distinctschool/',DistinctSchoolView.as_view()),
    #StateDropdown
    path('distinctstate/',DistinctStateView.as_view()),
    #schoolDropdownwrtStateSelection
    path('distinctschoolwrtstate/<slug:state_name>/',DistinctSchoolwrtStateView.as_view()),

    #DisplayTransferEvaluationOnHome
    re_path(r'transferevaluationmaindisplay/(?P<state_name>[\w|\W]+)/(?P<school_name>[\w|\W]+)/(?P<major_name>[\w|\W]+)/',TrasferEvaluationDisplayView.as_view()),

    #Create,View,detailView,Update and Delete Approvers
    path('approvers/',ApproverAPIView.as_view(), name='ListOrCreateApprover'),
    path('approvers/<int:pk>/',ApproverAPIView.as_view(), name='ModifyOrDeleteApprover'),

    #Create,View,detailView,Update and Delete Major
    path('majors/',MajorAPIView.as_view(), name='ListOrCreateMajor'),
    path('majors/<int:pk>/',MajorAPIView.as_view(), name='ModifyOrDeleteMajor'),

    #Create,View,detailView,Update and Delete School
    path('schools/',SchoolAPIView.as_view(), name='ListOrCreateSchool'),
    path('schools/<int:pk>/',SchoolAPIView.as_view(), name='ModifyOrDeleteSchool'),

    #Create,View,detailView,Update and Delete MajorRequirement
    path('majorrequirement/',MajorRequirementAPIView.as_view(), name='ListOrCreateMajorReq'),
    path('majorrequirement/<int:pk>/',MajorRequirementAPIView.as_view(), name='ModifyOrDeleteMajorReq'),

    #Create,View,detailView,Update and Delete TransferCourse
    path('transfercourse/',TransferCourseAPIView.as_view(), name='ListOrCreatetransfercourse'),
    path('transfercourse/<int:pk>/',TransferCourseAPIView.as_view(), name='ModifyOrDeletetransfercourse'),

    #Create,View,detailView,Update and Delete TransferEvaluation
    path('transferevaluation/',TransferEvaluationAPIView.as_view(), name='ListOrCreatetransferevaluation'),
    path('transferevaluation/<int:pk>/',TransferEvaluationAPIView.as_view(), name='ModifyOrDeletetransferevaluation'),

    #Add/modify/delete TransferEvaluation by checking existing records in TransferEvaluation
    path('checktransferevaluation/',CheckTransferEvaluationView.as_view(), name='ListOrCreatechecktransferevaluation'),
    path('checktransferevaluation/<int:pk>/',CheckTransferEvaluationView.as_view(), name='ModifyOrDeletetransferevaluation'),

    #validation page after adding Transfer evaluation details
    path('postchecktransferevaluation/<int:check_eval_id>/',PostCheckTransferEvaluationView.as_view(), name='postchecktransferevaluation'),
]

