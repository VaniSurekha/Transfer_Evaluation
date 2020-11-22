from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from .DataImport import *
from rest_framework import generics
from rest_framework import mixins
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.pagination import LimitOffsetPagination


# Create your views here.
class RegisterUserView(APIView):
    """ 
    Creates the user. 
    """
    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUserView(APIView):
    def post(self, request, format=None):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    def get(self, request, format=None):
        logout(request)
        return Response({"success": 'request'}, status=status.HTTP_200_OK)

class DistinctMajorView(generics.ListAPIView):
    queryset=Major.objects.values('major_name').order_by('major_name').distinct()
    serializer_class = DistinctMajorSerializer

class DistinctSchoolView(generics.ListAPIView):
    queryset=School.objects.values('school_name').order_by('school_name').distinct()
    serializer_class = DistinctSchoolSerializer

class DistinctStateView(generics.ListAPIView):
    queryset=School.objects.values('state_name').order_by('state_name').distinct()
    serializer_class = DistinctStateSerializer

class DistinctSchoolwrtStateView(generics.RetrieveAPIView):
    queryset=School.objects.all()

    def get_object(self,state_name):
        if state_name.lower() !='all':
            queryset= School.objects.filter(state_name=state_name).values('school_name').distinct()
        else:
            queryset= School.objects.values('school_name').distinct()
        return queryset

    def get(self,request,state_name):
        queryset=self.get_object(state_name)
        serializer=DistinctSchoolSerializer(queryset,many=True)
        return Response(serializer.data)

class TrasferEvaluationDisplayView(generics.RetrieveAPIView):
    queryset=Transferevaluation.objects.all()
    #pagination_class=LimitOffsetPagination
    
    def get_object(self,state_name,school_name,major_name):
        if school_name.lower()!='all' and major_name.lower()!='all':
            majorid=Major.objects.filter(major_name=major_name).values_list('major_id',flat=True).first()
            major_req_id=Major_requirement.objects.filter(major_id_id=majorid).values_list('major_req_id',flat=True)

            if state_name.lower()!='all':
                schoolid=School.objects.filter(state_name=state_name,school_name=school_name).values_list('school_id',flat=True).first()
            else:
                schoolid=School.objects.filter(school_name=school_name).values_list('school_id',flat=True).first()

            transfer_course_id=TransferCourse.objects.filter(school_id_id=schoolid).values_list('transfer_course_id',flat=True)

            queryset=Transferevaluation.objects.filter(major_req_id__in=major_req_id,transfer_course_id__in=transfer_course_id)
        
        elif school_name.lower()!='all' and major_name.lower()=='all':

            if state_name.lower()!='all':
                schoolid=School.objects.filter(state_name=state_name,school_name=school_name).values_list('school_id',flat=True).first()
            else:
                schoolid=School.objects.filter(school_name=school_name).values_list('school_id',flat=True).first()

            transfer_course_id=TransferCourse.objects.filter(school_id_id=schoolid).values_list('transfer_course_id',flat=True)

            queryset=Transferevaluation.objects.filter(transfer_course_id__in=transfer_course_id)
 
        elif school_name.lower()=='all' and major_name.lower()!='all':
            
            majorid=Major.objects.filter(major_name=major_name).values_list('major_id',flat=True).first()
            major_req_id=Major_requirement.objects.filter(major_id_id=majorid).values_list('major_req_id',flat=True)
            
            if state_name.lower()!='all':
                schoolid=School.objects.filter(state_name=state_name).values_list('school_id',flat=True)

                transfer_course_id=TransferCourse.objects.filter(school_id_id__in=schoolid).values_list('transfer_course_id',flat=True)

                queryset=Transferevaluation.objects.filter(major_req_id__in=major_req_id,transfer_course_id__in=transfer_course_id)
            else:
                queryset=Transferevaluation.objects.filter(major_req_id__in=major_req_id)

        else:            
            if state_name.lower()!='all':
                schoolid=School.objects.filter(state_name=state_name).values_list('school_id',flat=True)

                transfer_course_id=TransferCourse.objects.filter(school_id_id__in=schoolid).values_list('transfer_course_id',flat=True)

                queryset=Transferevaluation.objects.filter(transfer_course_id__in=transfer_course_id)
            else:
                queryset=Transferevaluation.objects.all()
        return queryset

    def get(self,request,state_name=None,school_name=None,major_name=None):
        qs=self.get_object(state_name,school_name,major_name)
        serializer=TransferevaluationSerializer(qs,many=True)
        return Response(serializer.data)

class ApproverAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class=ApproverSerializer
    queryset=Approver.objects.all()
    lookup_field='pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, pk=None):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)
    
    def delete(self, request, pk=None):
        return self.destroy(request, pk)

class MajorAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class=MajorSerializer
    queryset=Major.objects.all()
    lookup_field='pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, pk=None):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)
    
    def delete(self, request, pk=None):
        return self.destroy(request, pk)

class SchoolAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class=SchoolSerializer
    queryset=School.objects.all()
    lookup_field='pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, pk=None):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)
    
    def delete(self, request, pk=None):
        return self.destroy(request, pk)

class MajorRequirementAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class=MajorRequirementSerializer
    queryset=Major_requirement.objects.all()
    lookup_field='pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, pk=None):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)
    
    def delete(self, request, pk=None):
        return self.destroy(request, pk)

class TransferCourseAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class=TransferCourseSerializer
    queryset=TransferCourse.objects.all()
    lookup_field='pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, pk=None):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)
    
    def delete(self, request, pk=None):
        return self.destroy(request, pk)

class TransferEvaluationAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class=TransferevaluationSerializer
    queryset=Transferevaluation.objects.all()
    lookup_field='pk'

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, pk=None):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)
    
    def delete(self, request, pk=None):
        return self.destroy(request, pk)

class CheckTransferEvaluationView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    serializer_class=CheckEvaluationSerializer
    queryset=CheckEvaluation.objects.all()
    lookup_field='pk'
    
    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request, pk=None):
        return self.create(request)

    def put(self, request, pk=None):
        return self.update(request, pk)
    
    def delete(self, request, pk=None):
        return self.destroy(request, pk)

class PostCheckTransferEvaluationView(APIView):
    
    def post(self, request,check_eval_id,*args, **kwargs):
            
        check = CheckEvaluation.objects.get(check_eval_id = check_eval_id)
        schools = School.objects.filter(school_name=check.school_name)
        major = Major.objects.filter(major_name=check.major_name)
        approver = Approver.objects.filter(approver_name=check.approver_name)

            # Addition of new school and its course from form
        if len(schools) == 0:
            School(school_name=check.school_name, state_name='None').save()
            # CheckEvaluation(school_name=check.school_name).save()
            school = School.objects.get(school_name=check.school_name)
            TransferCourse(school_id=school, subject_number=check.transfer_subject_number, title=check.transfer_course_title).save()
        else:
            # Addition of new courses if school exists in School model
            course = TransferCourse.objects.filter(school_id__in = schools).filter(subject_number=check.transfer_subject_number)
            if len(course) == 0:
                school = School.objects.get(school_name=check.school_name)
                TransferCourse(school_id=school, subject_number=check.transfer_subject_number, title=check.transfer_course_title).save()

            #Adding new majors and its major_requirements to its models
        if len(major) == 0:
            Major(major_name=check.major_name).save()
            new_major = Major.objects.get(major_name=check.major_name)
            Major_requirement(description=check.unhm_equivalent, major_id=new_major).save()
        else:
            # addition of new major_requirement if the major already exists in the Major model
            major = Major_requirement.objects.filter(major_id__in=major).filter(description=check.unhm_equivalent)
            if len(major) == 0:
                new_major = Major.objects.get(major_name=check.major_name)
                Major_requirement(description=check.unhm_equivalent, major_id=new_major).save()

            # addition of new approver
        if len(approver) == 0:
            Approver(approver_name = check.approver_name).save()

        school = School.objects.filter(school_name=check.school_name)
        transfer_course = TransferCourse.objects.filter(school_id__in = school).filter(subject_number = check.transfer_subject_number)

        major = Major.objects.filter(major_name = check.major_name)
        major_req = Major_requirement.objects.filter(major_id__in = major).filter(description=check.unhm_equivalent)

        transfer_eval = Transferevaluation.objects.filter(major_req_id__in = major_req).filter(transfer_course_id__in = transfer_course)
        if len(transfer_eval) == 0:
            for each_transfer_course in transfer_course:
                transfer_course = each_transfer_course
                print(transfer_course)

            transfer_course.title = check.transfer_course_title

            for new_major_req in major_req:
                major_req = new_major_req
                print(major_req)

            Transferevaluation(transfer_course_id=transfer_course,major_req_id=major_req,sem_year_taken=check.sem_or_year_taken,expiration_date=check.expiration_date,approved_status=check.approved_status,approver_id=Approver.objects.get(approver_name=check.approver_name)).save()

            object_list = Transferevaluation.objects.all()   
        return Response(status=status.HTTP_200_OK)
      
class FileUploadView(APIView):
    parser_classes=(MultiPartParser,FormParser,)
    
    def post(self, request, *args, **kwargs):
        file_serializer = FileUploadSerializer(data=request.data)
        file=request.FILES['file']
        import_data(file)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RemoveFileUploadView(APIView):
    
    def post(self, request, *args, **kwargs):
        Major.objects.all().delete()
        School.objects.all().delete()
        TransferCourse.objects.all().delete()
        Major_requirement.objects.all().delete()
        Transferevaluation.objects.all().delete()
        Approver.objects.all().delete()
        return Response(status=status.HTTP_200_OK)

        
    
