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

messages = []


@ensure_csrf_cookie
def code_quality_checker_view(request):
    if request.method == 'POST':
        print("request received")
        data = {}
        files = request.FILES.getlist('files[]', None)
        data['msg'] = '<span style="color: green;">File successfully uploaded</span>'

        initialize_openai_context()

        file_list = []
        for f in files:
            file_analysis = {}
            file_name = f.name
            file_analysis['file_name'] = file_name

            file_content = f.read()
            file_content_str = file_content.decode('utf-8')
            file_analysis['file_content'] = file_content_str

            file_analysis['openai_analysis'] = analyse_code(file_content_str)
            file_list.append(file_analysis)

        data['analysis'] = file_list
        return JsonResponse(data)

    return render(request, 'code_quality_checker.html')


def get_openai_code_completion_response(prompt):
    chat = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0
    )
    # get response
    reply = chat['choices'][0]['text'].strip()

    return reply


def get_openai_completion_response(prompt):
    messages.append({"role": "user", "content": prompt})
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(reply)
    return reply


def initialize_openai_context():
    # initialize messages
    global messages
    messages = [
        {"role": "system",
         "content": "You are an AI specialized in examining source code to identify potential issues, errors, "
                    "security vulnerabilities, and other coding best practices to ensure code quality, "
                    "maintainability, and security and you help to detect bugs, performance bottlenecks, "
                    "and adherence to coding standards."},
    ]


def analyse_code(file_content):
    code_query = "Please provide inline code quality comments/corrections for the following code \n" + file_content
    analysis = get_openai_completion_response(code_query)

    return analysis
