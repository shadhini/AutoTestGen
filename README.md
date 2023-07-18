# AutoTestGen

>>> Prototype Implementation of General-Purpose Testing Engine

This prototype utilize ChatGPT to automate the test model creation, test generation, test execution, and result analysis stages.

- The prototype testing engine feature a user interface to input textual requirements or user stories. 
- `[not implemented yet]` The LLM would process the input and generate a structured test model, such as a UML diagram. 
- `[not implemented yet]` Based on the test model, the LLM would generate test cases, test scripts, and test data automatically.
- `[not implemented yet]` The testing engine would then simulate user interactions with the software system, utilizing the LLM to execute the generated tests and validate the results. 
- `[not implemented yet]` The LLM would also analyze the test logs and system outputs to identify any deviations or defects


## Start the development server

##### Option 1
Start the development server on the internal IP at port 8000 (the default port)
- should be called from the root directory where `manage.py` resides
```shell
python manage.py runserver
```
```text
Starting development server at http://127.0.0.1:8000/
```
##### Option 2
If you want to change the server’s port, pass it as a command-line argument 
```shell
python manage.py runserver 8080
```







