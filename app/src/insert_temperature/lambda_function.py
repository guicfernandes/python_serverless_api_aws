import json
import boto3
from datetime import datetime


'''
Event Test
{
  "deviceId": "device_moto_phone",
  "temperature": "12"
}
'''


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')

    table_temperature = dynamodb.Table('Temperatures')

    event_date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    device_id = event['deviceId']
    temperature = event['temperature']

    try:
        table_temperature.put_item(
            Item={
                'eventDateTime': event_date_time,
                'deviceId': device_id,
                'temperature': int(temperature)
            }
        )

        return {
            'status_code': 200,
            'body': json.dumps('Successfully inserted temperature.')
        }
    except Exception as e:
        print(f'Closing Lambda funcion due to an error: {e}')
        return {
            'status_code': 400,
            'body': json.dumps(f'Error saving the temperatue.\n{e}')
        }
