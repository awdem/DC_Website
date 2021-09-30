import json

import awsgi
import django
import sentry_sdk
from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()


def lambda_handler(event, context):
    return awsgi.response(
        application,
        event,
        context,
        base64_content_types={
            "image/png",
            "image/x-icon",
            "image/jpeg",
            "image/jpg",
            "font/woff2",
        },
    )


def management_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    cmd = event["command"]
    args = event.get("args", [])

    sentry_sdk.set_context("event", event)

    django.setup()

    print(f"Calling {cmd} with args {args}")
    call_command(cmd, *args)

    arg_str = " ".join(args)
    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": f"{cmd} {arg_str} completed",
            }
        ),
    }
