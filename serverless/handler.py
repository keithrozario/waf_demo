import json


def hello(event, context):
    body = {
        "message": "Successfully done",
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

