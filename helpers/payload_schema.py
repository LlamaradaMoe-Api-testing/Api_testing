import json


def body():
    payload = json.dumps({
        "title": "Hello world1!!!",
        "status": "publish",
        "content": ""
    })
    return payload
