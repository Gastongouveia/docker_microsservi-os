from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def mult(request):
    if request.method == 'GET':
        response = Response()
        print(request)
        op1 = request.GET.get('op1')
        op2 = request.GET.get('op2')
        resultado = float(op1) * float(op2)

    return Response({'resultado': resultado})