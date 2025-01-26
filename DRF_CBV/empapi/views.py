from rest_framework.response import Response
from .myserializer import EmployeeSerializer
from .models import Employee
from rest_framework.decorators import api_view
from rest_framework import status


@api_view(['GET','POST'])
def getcreate(request):
    if request.method == 'GET':
        serializer = EmployeeSerializer(Employee.objects.all(),many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serialize = EmployeeSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def getputdelete(request,pk): 

    try:
        snippet = Employee.objects.get(id=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = EmployeeSerializer(snippet)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = EmployeeSerializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

