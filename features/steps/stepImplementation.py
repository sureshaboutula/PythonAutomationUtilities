from lib2to3.fixes.fix_input import context

from behave import *
import requests
import json
import mysql.connector

import utilities
from payload import *
from requests import session
from utilities.configurations import *
from utilities.resources import *


@given('the Book details which needs to be added to the Library')
def step_Implementation(context):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.json = addBookPayload2("behavetest6", "43569")
    context.headers = {"Content-Type": "application/json"}

@when('we execute the AddBook PostAPI method')
def step_Implementation(context):
    context.addBook_response = requests.post(url=context.url, json=context.json, headers=context.headers)


@then('book is successfully added')
def step_Implementation(context):
    print(context.addBook_response.json())
    response_json = context.addBook_response.json()
    print(type(response_json))
    context.bookId = response_json['ID']
    print(context.bookId)
    assert response_json['Msg'] == 'successfully added'

@given('the Book details with {isbn} and {aisle}')
def step_Implementation(context, isbn, aisle):
    context.url = getConfig()['API']['endpoint'] + ApiResources.addBook
    context.json = addBookPayload2(isbn, aisle)
    context.headers = {"Content-Type": "application/json"}


@given('I have github auth credentials')
def step_impl(context):
    context.se = requests.session()
    context.se.auth = ("sureshaboutula", getPassword())
    #context.url = "https://api.github.com/user/repos"


@when('I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then('status code of response should be {statusCode:d}')
def step_impl(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode

