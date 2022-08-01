import json


def body():
    payload = json.dumps({
        "title": "Hello world1!!!",
        "status": "publish",
        "content": ""
    })
    return payload


def schema_draft():
    payload = json.dumps({
        "title": "Hello world2!!!",
        "status": "draft",
        "content": ""
    })
    return payload


def schema_trash():
    payload = json.dumps({
        "title": "Hello world2!!!",
        "status": "publish",
        "content": ""
    })
    return payload
