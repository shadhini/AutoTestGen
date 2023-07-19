import os

import openai
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from dotenv import load_dotenv

# Create your views here.

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY


@ensure_csrf_cookie
def index_view(request):
    if request.method == 'POST':
        print("request received")
        data = {}
        return JsonResponse(data)

    return render(request, 'index_view.html')
