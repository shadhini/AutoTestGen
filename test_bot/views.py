from django.shortcuts import render
from django.http import JsonResponse
from dotenv import load_dotenv
import openai
import os


# Create your views here.

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

openai.api_key = OPENAI_API_KEY

messages = [
    {"role": "system",
     "content": "You are an AI specialized in General-Purpose Testing Engine capable of generating  a structured test "
                "model, such as a UML diagram based on given textual requirements or user stories, generating test "
                "cases, test scripts, and test data automatically based on that test model, simulating user "
                "interactions with the software system, executing the generated tests and validating the results and "
                "analyzing the test logs and system outputs to identify any deviations or defects."},
    {}
]


def get_openai_completion_response(prompt):
    print("Get completion")
    print(prompt)
    messages[1] = {"role": "user", "content": prompt}
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    reply = chat.choices[0].message.content
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

        # Step 4: Test Case Generation
        test_cases = generate_test_cases(test_model)
        data["test_cases"] = test_cases

        # # Step 5: Test Script Generation
        # test_scripts = generate_test_scripts(test_cases)
        #
        # # Step 6: Test Data Generation
        # test_data = generate_test_data(test_cases)
        #
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
    processed_data = input_text
    return processed_data


# Step 3: Test Model Generation
def generate_test_model(processed_data):
    # generate a test model using the processed data
    test_model_query = "Generate a test model for the following textual requirement/user stories \n" + processed_data
    test_model = get_openai_completion_response(test_model_query)

    return test_model


# Step 4: Test Case Generation
def generate_test_cases(test_model):
    # Implement code to generate test cases based on the test model
    test_cases_query = "Generate test cases based on the test model given below \n" + test_model
    test_cases = get_openai_completion_response(test_cases_query)

    return test_cases


# Step 5: Test Script Generation
def generate_test_scripts(test_cases):
    # Implement code to generate test scripts based on the test cases
    test_scripts = ...

    return test_scripts


# Step 6: Test Data Generation
def generate_test_data(test_cases):
    # Implement code to generate test data for the test cases
    test_data = ...

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

