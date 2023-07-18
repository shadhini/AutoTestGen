from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.


def code_quality_checker_view(request):
    if request.method == 'POST':
        print("request received")
        data = {}
        return JsonResponse(data)
    return render(request, 'code_quality_checker.html')
