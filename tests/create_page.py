#
# create_page.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# Edificio Union № 1376 Av. General Inofuentes esquina Calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

from assertpy.assertpy import assert_that
import json
from http import HTTPStatus
from helpers.crud import CrudPage
from utils.print_helpers import pretty_print
from tests.get_token import test_get_token
from helpers.config import status_code,json_response,dict_response
from helpers.config import AUTHORIZATION
from helpers.config import schema

# Happy path
def test_create_post():
    payload = json.dumps({
      "title": "Validate status response!",
      "status": "publish",
      "content": "test for validate the status response"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)


def test_validate_valid_token():
    test_get_token()
    payload = json.dumps({
        "title": "Valid token!",
        "status": "publish",
        "content": "test with a valid token"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)


def test_valid_title():
    test_get_token()
    title = "Valid title"
    payload = json.dumps({
        "title": title,
        "status": "publish",
        "content": "Test for validate title"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    response_title = response_content['title']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(response_content['title']).is_not_empty()
    assert_that(response_title['raw']).is_equal_to(title)


def test_valid_content():
    test_get_token()
    content = "test for validate the content"
    payload = json.dumps({
        "title": "Validate the content",
        "status": "publish",
        "content": content
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    resp_content = response_content['content']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(response_content['content']).is_not_empty()
    assert_that(resp_content['raw']).is_equal_to(content)


def test_valid_content2():
    test_get_token()
    payload = json.dumps({
        "title": "Valid content!!!",
        "status": "publish",
        "content": "Correct content"
    })
    responses = CrudPage().post(payload)
    print("-----------------------")
    print(responses[json_response])
    print("-----------------------")
    pretty_print(responses[dict_response])
    print("-----------------------")
    print(responses[status_code])
    print("-----------------CONTENT------------------")
    response_content = responses[dict_response]
    print(response_content['content'])
    print("-----------------CONTENT------------------")
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(response_content['content']).is_not_empty()


def test_valid_status_publish():
    test_get_token()
    status = "publish"
    payload = json.dumps({
        "title": "Status publish!",
        "status": status,
        "content": "test for validate the publish status"
    })
    responses = CrudPage().post(payload)
    #print(responses[json_response])
    response_content = responses[dict_response]
    #pretty_print(response_content['status'])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(response_content['status']).is_equal_to(status)


def test_valid_status_draft():
    test_get_token()
    status = "draft"
    payload = json.dumps({
        "title": "Status draft",
        "status": status,
        "content": "test for validate the draft status"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(response_content['status']).is_equal_to(status)


def test_valid_status_private():
    test_get_token()
    status = "private"
    payload = json.dumps({
        "title": "status private",
        "status": status,
        "content": "Test for validate the private status"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(response_content['status']).is_equal_to(status)


def test_validate_schema():
    print(schema)
    pretty_print(schema)
    try:
        json.loads(schema)
    except ValueError as error:
        return False
    return True


# Negative tests
def test_valid_no_title():
    test_get_token()
    payload = json.dumps({
        "title": "",
        "status": "publish",
        "content": "Test for validate no title"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    dic_title = response_content['title']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(dic_title['raw']).is_equal_to('')


def test_valid_void_title():
    test_get_token()
    payload = json.dumps({
        "title": "  ",
        "status": "publish",
        "content": "Test for validate void title"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    dic_title = response_content['title']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(dic_title['raw']).is_equal_to('')


def test_valid_null_title():
    test_get_token()
    payload = json.dumps({
        "status": "publish",
        "content": "Test for validate null title"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    dic_title = response_content['title']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(dic_title['raw']).is_equal_to('')


def test_valid_null_content():
    test_get_token()
    payload = json.dumps({
        "title": "null content",
        "status": "publish",
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    dic_content = response_content['content']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(dic_content['raw']).is_equal_to('')


def test_valid_void_content():
    test_get_token()
    payload = json.dumps({
        "title": "void content",
        "status": "publish",
        "content": ""
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    dic_content = response_content['content']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(dic_content['raw']).is_equal_to('')


def test_valid_void_content():
    test_get_token()
    payload = json.dumps({
        "title": "void content",
        "status": "publish",
        "content": "  "
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    dic_content = response_content['content']
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(dic_content['raw']).is_not_empty()


def test_invalid_status():
    status = 'not a status'
    payload = json.dumps({
        "title": "void content",
        "status": status,
        "content": "  "
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.BAD_REQUEST)
    assert_that(response_content['data']['status']).is_equal_to(400)


def test_void_status():
    payload = json.dumps({
        "title": "void content",
        "status": "",
        "content": "test for validate the void status"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.BAD_REQUEST)
    assert_that(response_content['data']['status']).is_equal_to(400)


def test_null_status():
    test_get_token()
    payload = json.dumps({
        "title": "void content",
        "content": "test for validate the void status"
    })
    responses = CrudPage().post(payload)
    print(responses[json_response])
    response_content = responses[dict_response]
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.CREATED)
    assert_that(response_content['status']).is_equal_to('draft')


def test_invalid_token():
    invalid_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ey'
    filename = "../helpers/config.py"
    #text = open(filename).read()
    text = open(filename)
    read_text = text.read()
    open(filename, "w+").write(read_text.replace(AUTHORIZATION, 'Bearer ' + invalid_token))
    text.close()
    payload = json.dumps({
        "title": "invalid token",
        "status": "publish",
        "content": "test an invalid token"
    })
    responses = CrudPage().post(payload)
    #responses.set_token(invalid_token)
    #resp = responses.post(payload)
    #print(resp[json_response])
    print("------------------------------------------")
    print(text)
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.UNAUTHORIZED)
    get_token = test_get_token()
    #assert_that(resp[dict_response]['error_description']).is_equal_to("Incorrect JWT Format.")


def test_invalid_token():
    invalid_token = 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.ey'
    payload = json.dumps({
        "title": "invalid token",
        "status": "publish",
        "content": "test an invalid token"
    })
    responses = CrudPage().post_with_token(payload, invalid_token)
    print(responses[json_response])
    assert_that(responses[status_code]).is_equal_to(HTTPStatus.UNAUTHORIZED)
    assert_that(responses[dict_response]['error_description']).is_equal_to("Incorrect JWT Format.")
