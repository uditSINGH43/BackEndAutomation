import requests
from behave import *

from payLoad import *
from utilities.configurations import *
from utilities.resources import *


@given('the book details which needs to be added to Library')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload("mangtsgdt","4567")


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad, headers=context.headers, )


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.bookId = response_json['ID']
    print(context.bookId)
    assert response_json['Msg'] == "successfully added"



@given ('the book details with {isbn} and {aisle}')
def step_impl(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    context.payLoad = addBookPayload(isbn, aisle)


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.Session()
    token = getPassword()  # make sure this returns your token, not password
    context.se.get(ApiResources.githubRepo, headers={"Authorization": f"token {token}"})



@when('i hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo, headers={"Authorization": "token " + getPassword()})


@then('status code of response should be {statusCode:d}')
def step_impl(context,statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode


