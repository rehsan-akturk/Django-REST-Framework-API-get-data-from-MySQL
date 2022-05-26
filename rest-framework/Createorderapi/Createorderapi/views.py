from .serialization import OrdersSerializer
from .models import  Orders
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
import  requests
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status



@api_view(['GET', 'POST', 'DELETE','PUT'])
def showorder(request):
    if request.method=='GET':
        results=Orders.objects.all()
        serialize=OrdersSerializer(results,many=True)
        return Response(serialize.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OrdersSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OrdersSerializer(Orders, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Orders.objects.all().delete()
        return JsonResponse({'message': '{} Tutorials were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)



def displaydata(request):
    callapi=requests.get('http://127.0.0.1:8000/api/orders')
    result=callapi.json()
    return  render(request,'index.html',{'Orders':result})