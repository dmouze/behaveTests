from behave import given, when, then, step
import requests
import json

base_url = "https://reqres.in/api"
login_endpoint = "/login"
headers = {
    'Content-Type': 'application/json'
}


@given("I am on the login page in Super APP")
def step_impl(context):
    context.url = base_url + login_endpoint


@when('I log in with email "{email}" and password "{password}"')
def step_impl(context, email, password):
    payload = json.dumps({
        "email": email,
        "password": password
    })
    response = requests.post(context.url, headers=headers, data=payload)
    context.response = response


@then("The login is successful")
def step_impl(context):
    assert context.response.status_code == 200, f"Login failed with status code {context.response.status_code}"
    response_json = context.response.json()
    assert "token" in response_json, "Token not found in response"
