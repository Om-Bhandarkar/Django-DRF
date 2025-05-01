from students.models import Student
from api.serializers import StudentSerializer,EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404

# function based view
@api_view(['GET','POST'])
def studentsView(request):

    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    
@api_view(['GET','PUT','DELETE'])
def studentDetailView(request,id):
    try: 
        student = Student.objects.get(id = id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# Class Based View
class Employees(APIView):
    # Get All Details 
    def get(self,request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    # Add Employee
    def post(self,request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class EmployeeDetail(APIView):

    def get_object(self,id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist :
            raise Http404
    # Get Single Employee
    def get(self,request,id):
        employee = self.get_object(id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    #Update Employee Details
    def put(self,request,id):
        employee = self.get_object(id)
        serializer = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # Delete Employee 
    def delete(self,request,id):
        employee = self.get_object(id)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



