import json
import connection
import datetime
from uuid import UUID
from tank_story_models import Account, Summary


def lambda_handler(event, context):
    connection.connection()
    try:
        account = Account.objects.get({'_id': UUID('d2f702a1-36f8-11e9-8305-acde48001122')})
        return {
            'statusCode': 200,
            'body': json.dumps(account.summary.to_son(), default=date_decoder)
        }
    except Account.DoesNotExist:
        return {
            'statusCode': 404,
            'body': json.dumps('Account not found')
        }


def date_decoder(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()
