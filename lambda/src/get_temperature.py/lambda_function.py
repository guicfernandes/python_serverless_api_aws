import json
import boto3


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')
    table_temperatures = dynamodb.Table('Temperatures')
    response = table_temperatures.scan()

    try:
        return {
            'status_code': 200,
            'body': response['Items']
        }
    except Exception as e:
        print(f'An error occured during table {table_temperatures}.\n{e}')
        return {
            'status_code': 400,
            'body': json.dumps(f'Error fetching table {table_temperatures}.\n{e}')
        }
