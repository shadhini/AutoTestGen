from django.http import JsonResponse
from django.shortcuts import render
from dotenv import load_dotenv
import openai
import os
import subprocess

from AutoTestGen.settings import BASE_DIR, MEDIA_ROOT

# Create your views here.

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY

messages = []


def get_openai_completion_response(prompt):
    print("Get completion")
    print(prompt)
    messages.append({"role": "user", "content": prompt})
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    reply = chat.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    # query = openai.Completion.create(
    #     engine="gpt-3.5-turbo-16k",
    #     prompt=prompt,
    #     max_tokens=1024,
    #     n=1,
    #     stop=None,
    #     temperature=0.5,
    # )
    #
    # response = query.choices[0].text
    print(reply)
    return reply


def get_openai_image_response(prompt):
    print("Get image")
    print(prompt)
    query = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024",
    )
    response = query.data[0].url
    print(response)
    return response


def testbot_view(request):
    if request.method == 'POST':
        print("request received")
        data = {}

        # Step 1: User Interface
        input_text = get_user_input(request)

        # Step 2: Input Processing
        processed_data = process_input(input_text)

        # Step 3: Test Model Generation
        test_model = generate_test_model(processed_data)
        data["test_model"] = test_model

        generate_uml_test_model()

        # Step 4: Test Case Generation
        test_cases = generate_test_cases(test_model)
        data["test_cases"] = test_cases

        # Step 5: Test Script Generation
        test_scripts = generate_test_scripts(test_cases)
        data["test_scripts"] = test_scripts

        # Step 6: Test Data Generation
        test_data = generate_test_data(test_cases)
        data["test_data"] = test_data

        # # Step 7: Test Execution
        # test_results = execute_test_scripts(test_scripts, test_data)
        #
        # # Step 8: Result Validation
        # validate_results(test_results)
        #
        # # Step 9: Test Log Analysis
        # analyze_test_logs(test_results.logs)
        #
        # # Step 10: Defect Identification
        # identified_defects = identify_defects(test_results.system_outputs, test_results.logs)
        #
        # # Step 11: Reporting and Documentation
        # generate_reports(test_results, identified_defects)
        #
        # prompt = request.POST.get('prompt')
        # response = get_openai_completion_response(prompt)
        return JsonResponse(data)
    return render(request, 'testbot.html')


# Step 1: User Interface
def get_user_input(request):
    input_text = request.POST.get('prompt')
    return input_text


# Step 2: Input Processing
def process_input(input_text):
    # initialize messages
    global messages
    messages = [
        {"role": "system",
         "content": "You are an AI specialized in General-Purpose Testing Engine capable of generating  a structured "
                    "test model, such as a UML diagram based on given textual requirements or user stories, "
                    "generating test cases, test scripts, and test data automatically based on that test model, "
                    "simulating user interactions with the software system, executing the generated tests and "
                    "validating the results and analyzing the test logs and system outputs to identify any deviations "
                    "or defects."},
    ]
    # process input
    processed_data = input_text
    return processed_data


# Step 3: Test Model Generation
def generate_test_model(processed_data):
    # generate a test model using the processed data
    test_model_query = "Generate a test model for the following textual requirement/user stories \n" + processed_data
    test_model = get_openai_completion_response(test_model_query)

    return test_model


def generate_uml_test_model():
    # generate a test model using the processed data
    plantuml_test_model_query = "Generate a test model for the above textual requirement/user stories in PlantUML " \
                                "format. Please respond with only the PlantUML file. Don't add any natural text " \
                                "to the response."
    plantuml_test_model = get_openai_completion_response(plantuml_test_model_query)

    file_path = os.path.join(MEDIA_ROOT, 'diagrams', 'diagram.puml')
    jar_path = os.path.join(BASE_DIR, 'lib', 'plantuml-1.2023.10.jar')

    with open(file_path, 'w') as file:
        file.write(plantuml_test_model)

    try:
        # Generate the image using PlantUML command-line tool
        subprocess.run(['java', '-jar', jar_path, file_path], check=True)
    except:
        pass


# Step 4: Test Case Generation
def generate_test_cases(test_model):
    # generate test cases based on the test model
    # test_cases_query = "Generate test cases based on the test model given below \n" + test_model
    test_cases_query = "Generate test cases based on the test model generated above."
    test_cases = get_openai_completion_response(test_cases_query)

    return test_cases


# Step 5: Test Script Generation
def generate_test_scripts(test_cases):
    # generate test scripts based on the test cases
    # test_scripts_query = "Generate test scripts in python based on the test cases given below \n" + test_cases
    test_scripts_query = "Generate test scripts in python based on the test cases generated above."
    test_scripts = get_openai_completion_response(test_scripts_query)

    return test_scripts


# Step 6: Test Data Generation
def generate_test_data(test_cases):
    # generate test data for the test cases
    # test_data_query = "Generate test data for the test cases given below \n" + test_cases
    test_data_query = "Generate test data for the test cases generated above. "
    test_data = get_openai_completion_response(test_data_query)

    return test_data


# Step 7: Test Execution
def execute_test_scripts(test_scripts, test_data):
    # Implement code to execute the test scripts using the test data
    # Simulate user interactions with the software system
    # Utilize the LLM for test execution
    ...


# Step 8: Result Validation
def validate_results(test_results):
    # Implement code to validate the test results
    # Compare actual outputs with expected outcomes
    # Flag any deviations or defects
    ...


# Step 9: Test Log Analysis
def analyze_test_logs(test_logs):
    # Implement code to analyze the test logs
    # Identify errors, failures, or exceptions
    ...


# Step 10: Defect Identification
def identify_defects(system_outputs, test_logs):
    # Implement code to analyze system outputs and test logs
    # Identify potential defects or unexpected behavior
    ...


# Step 11: Reporting and Documentation
def generate_reports(test_results, identified_defects):
    # Implement code to generate reports on the test results
    # Include identified defects or issues
    ...
