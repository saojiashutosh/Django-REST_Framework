import io
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.renderers import JSONRenderer
from .myserializer import EmployeeSerializer
from .models import Employee
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    serializer = EmployeeSerializer(Employee.objects.all(),many = True)
    print(serializer.data, type(serializer.data))
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')

def getemp(request,pk):
    serializer = EmployeeSerializer(Employee.objects.get(id=pk))
    print(serializer.data, type(serializer.data))
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type = 'application/json')

@csrf_exempt
def create_data(request):
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        parsed_data = JSONParser().parse(stream)
        serialize = EmployeeSerializer(data=parsed_data)
        if serialize.is_valid():
            serialize.save()
            resp = {'message': 'Data saved Successfully !!!!'}
            json_data = JSONRenderer().render(resp)
            return HttpResponse(json_data, content_type='application/json')
        print(serialize.errors)
        json_data = JSONRenderer().render(serialize.errors)
        return HttpResponse(json_data, content_type='application/json')
    elif request.method == 'PUT':
        data = request.body
        stream = io.BytesIO(data)
        parsed_data = JSONParser().parse(stream)
        id = parsed_data.get('id')  # Get 'id' from parsed data
        empobj = Employee.objects.get(id=id)
        serialize = EmployeeSerializer(empobj, data=parsed_data, partial=True)
        if serialize.is_valid():
            serialize.save()
            resp = {'message': 'Data updated Successfully !!!!'}
            json_data = JSONRenderer().render(resp)
            return HttpResponse(json_data, content_type='application/json')
        print(serialize.errors)
        json_data = JSONRenderer().render(serialize.errors)
        return HttpResponse(json_data, content_type='application/json')
    
    else:
        # Return a response for unsupported HTTP methods
        resp = {'error': 'Method not allowed'}
        json_data = JSONRenderer().render(resp)
        return HttpResponse(json_data, content_type='application/json', status=405)
